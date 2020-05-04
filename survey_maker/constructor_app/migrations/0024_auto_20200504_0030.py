# Generated by Django 3.0.5 on 2020-05-04 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructor_app', '0023_auto_20200504_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='structure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor_app.Structure'),
        ),
        migrations.AlterField(
            model_name='structure',
            name='department',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
