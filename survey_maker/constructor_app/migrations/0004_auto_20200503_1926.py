# Generated by Django 3.0.5 on 2020-05-03 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor_app', '0003_auto_20200502_0103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('code', models.PositiveIntegerField(null=True)),
                ('workers', models.PositiveIntegerField(null=True)),
                ('head_of_department', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='structure',
            name='code',
        ),
        migrations.RemoveField(
            model_name='structure',
            name='department',
        ),
        migrations.RemoveField(
            model_name='structure',
            name='workers',
        ),
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='companies'),
        ),
        migrations.AddField(
            model_name='structure',
            name='departments',
            field=models.ManyToManyField(to='constructor_app.Department'),
        ),
    ]
