from django.db import models

# Create your models here.

class Auditoria(models.Model):

    auditoria_nome = models.CharField(max_length=100, null=False, blank=False)
    auditoria_data = models.DateTimeField(auto_now=True)
    auditoria_representante = models.CharField(max_length=100, null=False, blank=False)
    auditoria_cidade = models.CharField(max_length=100, null=False, blank=False)
    auditoria_analista = models.CharField(max_length=100, null=False, blank=False)
    auditoria_visitas_previstas= models.CharField(max_length=100, null=False, blank=False)
    

    def __str__(self) -> str:
        return self.auditoria_nome