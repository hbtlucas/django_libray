from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Usuario
from hashlib import sha256

def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html',{'status':status})

def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status':status}) 

def valida_cadastro(request):
    user = request.POST.get('user')
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    usuario = Usuario.objects.filter(email = email)

    if len(user.strip()) == 0 or len(email.strip()) == 0:
        return redirect ('/auth/cadastro/?status=1')

    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=2')

    try:
        password = sha256(password.encode()).hexdigest()
        usuario = Usuario(user = user, email = email, password = password)
        usuario.save()
        return redirect('/auth/cadastro?status=0')
    except:
        return redirect('/auth/cadastro?status=3')

def valida_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    password = sha256(password.encode()).hexdigest()

    usuario = Usuario.objects.filter(email=email).filter(password=password)

    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuario) >0:
        request.session['usuario'] = usuario[0].id
        return redirect(f'/livro/home/')
    
def sair(request):
    request.session.flush()
    return redirect('/auth/login/')