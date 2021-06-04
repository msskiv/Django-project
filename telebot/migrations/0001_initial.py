# Generated by Django 3.2 on 2021-04-28 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Telesettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tlg_token', models.CharField(max_length=200, verbose_name='Токен')),
                ('tlg_chat', models.CharField(max_length=200, verbose_name='ID чата')),
                ('tlg_message', models.CharField(max_length=200, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
            },
        ),
    ]