# Generated by Django 5.1 on 2024-09-08 15:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarefa_realizada', models.CharField(choices=[('TAREFA01', 'Tarefa01'), ('TAREFA02', 'Tarefa02'), ('TAREFA03', 'Tarefa03'), ('TAREFA04', 'Tarefa04'), ('TAREFA05', 'Tarefa05'), ('TAREFA06', 'Tarefa06'), ('TAREFA07', 'Tarefa07')], default='', max_length=100)),
                ('tarefa_auditoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auditoria', to='tarefas.auditoria')),
            ],
        ),
    ]
