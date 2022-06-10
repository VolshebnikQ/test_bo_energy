from django.db import models

from datetime import date
from django.contrib.auth.models import User


class Request(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField('Дата', default=date.today)
    request = models.TextField(blank=True, null=True, verbose_name='Запрос')
    response = models.TextField(blank=True, null=True, verbose_name='Ответ')

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    def __str__(self):
        return f'{self.user}-{self.date}'