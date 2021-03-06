# Generated by Django 2.0.8 on 2018-10-09 22:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=160)),
                ('telefone', models.CharField(max_length=16)),
                ('endereço', models.CharField(max_length=150)),
                ('F', models.BooleanField(verbose_name='M')),
                ('data_nasc', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('pergunta', models.TextField()),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
