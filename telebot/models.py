from django.db import models

# Create your models here.
class Telesettings(models.Model):
    tlg_token = models.CharField(max_length=200, verbose_name='Токен')
    tlg_chat = models.CharField(max_length=200, verbose_name='ID чата')
    tlg_chatname = models.CharField(max_length=200, null=True, blank=True, verbose_name='Название чата')
    tlg_message = models.TextField(verbose_name='Сообщение')


    def __str__(self):
        return self.tlg_chatname

    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'