# Generated by Django 2.0.8 on 2018-10-09 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_per'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='per',
            name='endereço',
        ),
        migrations.AddField(
            model_name='per',
            name='deh_publi',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]