# Generated by Django 3.0.5 on 2020-05-07 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0002_auto_20200507_0219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyuser',
            name='company',
        ),
        migrations.RemoveField(
            model_name='surveyuser',
            name='name',
        ),
    ]
