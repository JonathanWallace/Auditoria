from django.urls import path
from apps.tarefas.views import index, login, novaAuditoria

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('auditoria', novaAuditoria, name='nova')
]