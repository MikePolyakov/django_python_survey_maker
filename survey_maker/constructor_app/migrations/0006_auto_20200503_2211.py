# Generated by Django 3.0.5 on 2020-05-03 22:11

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('constructor_app', '0005_auto_20200503_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='structure',
            name='code',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='structure',
            name='head_of_department',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='structure',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='constructor_app.Structure'),
        ),
        migrations.AddField(
            model_name='structure',
            name='workers',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.RemoveField(
            model_name='structure',
            name='department',
        ),
        migrations.AddField(
            model_name='structure',
            name='department',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
