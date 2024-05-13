from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario']).user
        
        return HttpResponse(f'ola {usuario} ')
    else: 
        return redirect('/auth/login/?status=2')
     