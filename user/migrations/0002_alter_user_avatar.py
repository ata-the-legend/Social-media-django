# Generated by Django 4.2.2 on 2023-06-13 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(upload_to='avatars', verbose_name='Avatar'),
        ),
    ]
