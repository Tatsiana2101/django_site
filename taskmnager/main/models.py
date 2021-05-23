from django.db import models


class Task(models.Model):
    title = models.CharField('Ваше имя', max_length=100)
    task = models.TextField('Отзыв')
    price = models.IntegerField('Количество звезд')

    def __str__(self):
        return self.task

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'



