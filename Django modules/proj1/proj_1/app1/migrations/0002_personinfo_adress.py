# Generated by Django 5.1.4 on 2025-01-17 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personinfo',
            name='adress',
            field=models.TextField(blank=True, default='', max_length=100),
        ),
    ]
