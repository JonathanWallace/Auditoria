from django import forms
from apps.tarefas.models import Auditoria

class AuditoriaForms(forms.ModelForm):
    class Meta:
        model = Auditoria
        exclude = ['auditoria_status']

        labels = {
            'auditoria_nome':'Nome',
            'auditoria_data':'Data',
            'auditoria_representante':'Representante',
            'auditoria_cidade':'Cidade',
            'auditoria_analista':'Analista',
            'auditoria_visitas_previstas':'Visitas Previstas',
        }

        widgets = {
            'auditoria_nome':forms.TextInput(attrs={"class":"form-control"}),
            'auditoria_data':forms.DateTimeInput(),
            'auditoria_representante':forms.TextInput(attrs={"class":"form-control"}),
            'auditoria_cidade':forms.TextInput(attrs={"class":"form-control"}),
            'auditoria_analista':forms.TextInput(attrs={"class":"form-control"}),
            'auditoria_visitas_previstas':forms.TextInput(attrs={"class":"form-control"}),            
        }

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Login', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite seu usuário"
            }
        )
    )
    
    senha = forms.CharField(
        label='Senha',
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )