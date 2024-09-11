from django.urls import path
from apps.tarefas.views import index, login, novaAuditoria, auditoria, addTarefa, finalizar, gerarExcel

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('nova_auditoria', novaAuditoria, name='nova'),
    path('auditoria/<int:id>', auditoria, name='auditoria'),
    path('auditoria/add_tarefa', addTarefa, name='tarefa'),
    path('finalizar/<int:id>', finalizar, name="finalizar"),
    path('excel', gerarExcel, name='excel')
]