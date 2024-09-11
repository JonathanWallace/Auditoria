from django.db import models

# Create your models here.

class Auditoria(models.Model):

    auditoria_nome = models.CharField(max_length=100, null=False, blank=False)
    auditoria_data = models.DateTimeField(auto_now_add=True, editable=False)
    auditoria_representante = models.CharField(max_length=100, null=False, blank=False)
    auditoria_cidade = models.CharField(max_length=100, null=False, blank=False)
    auditoria_analista = models.CharField(max_length=100, null=False, blank=False)
    auditoria_visitas_previstas= models.CharField(max_length=100, null=False, blank=False)
    auditoria_status = models.BooleanField(default=True)
    

    def __str__(self) -> str:
        return self.auditoria_nome
    

class Tarefa(models.Model):

    CHOICES = [('TAREFA01', 'Tarefa01'),
               ('TAREFA02', 'Tarefa02'),
               ('TAREFA03', 'Tarefa03'),
               ('TAREFA04', 'Tarefa04'),
               ('TAREFA05', 'Tarefa05'),
               ('TAREFA06', 'Tarefa06'),
               ('TAREFA07', 'Tarefa07')]

    tarefa_auditoria = models.ForeignKey(to=Auditoria, on_delete=models.CASCADE, null=False, blank=False, related_name='auditoria')
    tarefa_realizada = models.CharField(max_length=100, choices=CHOICES, default='')
    tarefa_data = models.DateTimeField(auto_now_add=True, editable=False)

    def str(self):
        return self.tarefa_realizada
