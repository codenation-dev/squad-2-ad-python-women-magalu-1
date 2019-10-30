from django.shortcuts import render
from datetime import datetime
import requests

from .models import Error, User

def user_login(request):    
    return render(request, 'errors/user_login.html')

def user_register(request):    
    return render(request, 'errors/user_register.html')

def error_list(request):
    return render(request, 'errors/error_list.html')

def error_detail(request, error_id):

    response = requests.get(f'http://127.0.0.1:8000/api/errors/{error_id}')
    if response.status_code >= 200 and response.status_code < 400:

        error = response.json()
        # print(error['created_at'])
        # myDate = datetime.strptime(error['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
        # # myDate = myDate.strftime('%d-%m-%Y')
        # # datetime.strptime(error['created_at'], '%b %d %Y %I:%M%p')
        # # myDate = ''
        context = {
            'error': error,
            'date': error['created_at']
        }
        
        return render(request, 'errors/error_detail.html', context=context)
    else:
        return render(request, 'errors/error_detail.html', context=[])
