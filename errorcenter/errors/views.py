from django.shortcuts import render
import requests

from .models import Error

def user_login(request):    
    return render(request, 'errors/user_login.html')

def user_register(request):    
    return render(request, 'errors/user_register.html')

def error_list(request):
    response = requests.get('http://127.0.0.1:8000/api/errors')
    if response.status_code >= 200 and response.status_code < 400:
        context = {
            'errors': response.json()
        }
        return render(request, 'errors/error_list.html', context=context)
    else:
        return render(request, 'errors/error_list.html', context={})
