from django.shortcuts import render

from .models import Error

def user_login(request):    
    return render(request, 'errors/user_login.html')

def user_register(request):    
    return render(request, 'errors/user_register.html')

def error_list(request):
    return render(request, 'errors/error_list.html')
