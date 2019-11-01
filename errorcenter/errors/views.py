from django.shortcuts import render
from django.shortcuts import redirect
import requests

def checkNone(s):
    if s is None:
        return ''
    return s

def user_login(request):    
    return render(request, 'errors/user_login.html')

def user_register(request):    
    return render(request, 'errors/user_register.html')

def error_list(request):

    if request.method == 'GET':
        environment = checkNone(request.GET.get('environment'))
        order_by = checkNone(request.GET.get('order_by'))
        search_for = checkNone(request.GET.get('search_for'))
        search = checkNone(request.GET.get('search'))
        filter_params = '?environment=' + environment + '&order_by=' + order_by + '&search_for=' + search_for + '&search=' + search
        response = requests.get('http://127.0.0.1:8000/api/errors' + filter_params)

    elif request.method == 'POST':
        flag = request.POST.get('button_pressed')
        errors_checked = request.POST.getlist('checkbox')

        if flag == 'Arquivar':
            for error in errors_checked:
                response = requests.patch(f'http://127.0.0.1:8000/api/errors/{error}/archive/', data={'filed': True})
        elif flag == 'Deletar':
            for error in errors_checked:
                response = requests.delete(f'http://127.0.0.1:8000/api/errors/{error}/delete/', data={'id': error})

    if response.status_code >= 200 and response.status_code < 400:
        if request.method == 'POST':
            return redirect('/list')

        context = {
            'errors': response.json()
        }
        return render(request, 'errors/error_list.html', context=context)
    else:
        return render(request, 'errors/error_list.html', context={})


def error_detail(request, error_id):

    response = requests.get(f'http://127.0.0.1:8000/api/errors/{error_id}')
    if response.status_code >= 200 and response.status_code < 400:

        error = response.json()
        # myDate = datetime.strptime(error['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
        myDate = error['created_at']
        context = {
            'error': error,
            'date': myDate
        }
        
        return render(request, 'errors/error_detail.html', context=context)
    else:
        return render(request, 'errors/error_detail.html', context=[])
