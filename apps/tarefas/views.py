from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from apps.tarefas.forms import LoginForms, AuditoriaForms
from apps.tarefas.models import Auditoria, Tarefa
from django.contrib import auth, messages

import io
import pandas as pd

# Create your views here.
def index(request):
    form = AuditoriaForms()
    auditorias = Auditoria.objects.all()
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/home.html', {'form':form, 'auditorias':auditorias, 'tarefas':tarefas})


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
    if request.method == 'POST':
        form = AuditoriaForms(request.POST)
        if form.is_valid():
            nova=form.save()            
            return redirect(f'auditoria/{nova.id}')

    return redirect('index')


def auditoria(request, id):
    CHOICES = ['Tarefa01',
               'Tarefa02',
               'Tarefa03',
               'Tarefa04',
               'Tarefa05',
               'Tarefa06',
               'Tarefa07']
    auditoria = get_object_or_404(Auditoria, pk=id)

    return render(request, 'tarefas/auditoria.html', {'auditoria': auditoria, 'tarefas': CHOICES})


@csrf_exempt
def addTarefa(request):
    if request.method == 'POST':        

        auditoria = request.POST.get('tarefa_auditoria')
        tarefa_auditoria = get_object_or_404(Auditoria, pk=auditoria)
        tarefa_realizada = request.POST.get('tarefa_realizada')

        if tarefa_auditoria and tarefa_realizada:
            try:
                tarefa = Tarefa.objects.create(
                    tarefa_auditoria=tarefa_auditoria,
                    tarefa_realizada=tarefa_realizada,
                )
                tarefa.save()
                return JsonResponse({'success': True, 'mensagem': 'Tarefa salva com sucesso!'})
            except Exception as e:
                return JsonResponse({'success': False, 'mensagem': f'Erro ao salvar tarefa: {e}'})
        else:
            return JsonResponse({'success': False, 'mensagem': 'Dados inválidos'})
    else:
        return JsonResponse({'success': False, 'mensagem': 'Método inválido'})
    

def finalizar(request, id):
    auditoria = get_object_or_404(Auditoria, pk=id)
    if auditoria:
        auditoria.auditoria_status = False
        auditoria.save()

    return redirect('index')

def gerarExcel(request):
    auditorias = Auditoria.objects.all()
    
    dicionario = {"Auditoria":[],
                  "Data":[],
                  "Hora":[],
                  "Nome analista":[],
                  "BU":[],
                  "Zona":[],
                  "Atividade":[],
                  "KM(final-inicial)":[],
                  "Tempo medido":[]}
    

    for auditoria in auditorias:
        tarefas = Tarefa.objects.filter(tarefa_auditoria=auditoria.id)
        ultimo = None
        for tarefa in tarefas:
            dicionario['Auditoria'].append(tarefa.tarefa_auditoria.auditoria_nome)
            dicionario['Data'].append(tarefa.tarefa_auditoria.auditoria_data.strftime('%d/%m/%Y'))
            dicionario['Hora'].append(tarefa.tarefa_auditoria.auditoria_data.strftime('%H:%M:%S'))
            dicionario['Nome analista'].append(tarefa.tarefa_auditoria.auditoria_analista)
            dicionario['BU'].append("Nenhum")
            dicionario['Zona'].append("Nenhum")
            dicionario['Atividade'].append(tarefa.tarefa_realizada)
            dicionario['KM(final-inicial)'].append('Nenhum')

            if ultimo:
                if ultimo.tarefa_auditoria.auditoria_nome == tarefa.tarefa_auditoria.auditoria_nome:
                    delta = tarefa.tarefa_data - ultimo.tarefa_data
                else:
                    delta = tarefa.tarefa_data - auditoria.auditoria_data
            else:
                delta = tarefa.tarefa_data - auditoria.auditoria_data      
            horas = delta.seconds // 3600
            minutos = (delta.seconds % 3600) // 60
            segundos = delta.seconds % 60

            dicionario['Tempo medido'].append(f'{horas:02}:{minutos:02}:{segundos:02}')
            ultimo = tarefa

    dataframe = pd.DataFrame(dicionario)
    
    output = io.BytesIO()    
    dataframe.to_excel(output, sheet_name='Auditoria', index=False)   
    output.seek(0)

    response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=auditorias.xlsx'


    return response

