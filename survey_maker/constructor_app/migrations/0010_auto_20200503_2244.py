# Generated by Django 3.0.5 on 2020-05-03 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor_app', '0009_auto_20200503_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='surveys',
        ),
        migrations.AddField(
            model_name='company',
            name='surveys',
            field=models.ManyToManyField(to='constructor_app.Survey'),
        ),
    ]
