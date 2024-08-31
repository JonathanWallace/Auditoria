from django.shortcuts import render, redirect
from apps.tarefas.forms import LoginForms, AuditoriaForms
from apps.tarefas.models import Auditoria
from django.contrib import auth, messages

# Create your views here.
def index(request):
    form = AuditoriaForms()
    auditorias = Auditoria.objects.all()

    if request.method == 'POST':
        form = AuditoriaForms(request.POST)
        if form.is_valid():
            form.save()                   
        

    return render(request, 'tarefas/home.html', {'form':form, 'auditorias':auditorias})


def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(request, username=nome, password=senha)
        
        if usuario is not None:
            auth.login(request, usuario)
            return redirect('index')
        else:
            messages.error(request, f'Dados incorretos!')
            return redirect('login')

    return render(request, 'tarefas/login.html', {'form':form})

def novaAuditoria(request):
    return render(request, 'tarefas/auditoria.html')
