# Generated by Django 3.0.5 on 2020-05-07 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyuser',
            name='user_category',
        ),
        migrations.DeleteModel(
            name='UserCategory',
        ),
    ]
