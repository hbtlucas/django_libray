from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Livros


def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        livros = Livros.objects.filter(usuario = usuario)
        return render(request, 'home.html',{'livros': livros})
    else: 
        return redirect('/auth/login/?status=2')
     
def ver_livros(request,id):
    if request.session.get('usuario'):
        livros = Livros.objects.get(id=id)
        if request.session.get('usuario') == livros.usuario.id:
            return render(request,'ver_livro.html',{'livro':livros})
        else:
            return HttpResponse('esse livro nao e seu')
            
