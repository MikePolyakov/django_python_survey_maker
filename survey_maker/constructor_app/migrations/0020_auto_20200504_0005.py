# Generated by Django 3.0.5 on 2020-05-04 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor_app', '0019_structure_head_of_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='structure',
            name='head_of_department',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
