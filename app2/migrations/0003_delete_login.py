# Generated by Django 2.2.1 on 2019-05-21 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_login'),
    ]

    operations = [
        migrations.DeleteModel(
            name='login',
        ),
    ]