# Generated by Django 2.1.7 on 2019-03-01 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversion', '0005_project_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='author',
        ),
    ]