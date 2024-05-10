from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario

def login(request):
    return render(request, '')

def cadastro(request):
    return render(request, 'cadastro.html')

def valida_cadastro(request):
    user = request.POST.get('user')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirmpassword = request.POST.get('confirmpassword')
    return HttpResponse(f'{user} {email} {password} {confirmpassword}')