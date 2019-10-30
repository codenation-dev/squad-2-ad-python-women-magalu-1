from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserForm
import requests
import json

from .models import Error

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            payload = {
                    'username' : username,
                    'password' : password
                }
            headers = {'content-type': 'application/json'}   
            token = requests.post(
                    'http://127.0.0.1:8000/api/token-auth/', 
                    data=json.dumps(payload),
                    headers=headers
                )
            return redirect('error-list') #, {'token': token.json()['token']})
        else:
            messages.error(
                request, 
                'As credenciais do usuário estão incorretas'
            )
            return redirect('user-login')
    form_login = AuthenticationForm()
    return render(request, 'errors/user_login.html', {'form_login': form_login})


@login_required()
def deslogar_usuario(request):
    logout(request)
    return redirect('user_login')


def user_register(request):  
    if request.method == "POST":
        form_usuario = UserForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('home-page')
    else:
        form_usuario = UserForm()
    return render(
                  request,
                  'errors/user_register.html',
                  {'form_usuario': form_usuario}
                )  
    return render(request, 'errors/user_register.html')


@login_required()
def error_list(request):
    response = requests.get('http://127.0.0.1:8000/api/errors')
    if response.status_code >= 200 and response.status_code < 400:
        context = {
            'errors': response.json()
        }
        return render(request, 'errors/error_list.html', context=context)
    else:
        return render(request, 'errors/error_list.html', context={})
