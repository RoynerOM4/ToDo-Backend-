# Generated by Django 5.0.6 on 2024-05-30 04:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('fecha_inicio', models.DateField(verbose_name='Fecha de inicio')),
                ('fecha_final', models.DateField(verbose_name='Fecha de vencimiento')),
                ('priority', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='ToDoApp.category')),
            ],
        ),
    ]