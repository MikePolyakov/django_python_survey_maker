# Generated by Django 3.0.5 on 2020-05-04 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor_app', '0026_user_usercategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=1, max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
