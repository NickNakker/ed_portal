from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class News(models.Model):
    title = models.CharField('Название статьи', max_length=100, unique=True)
    text = models.TextField('Основной текст статьи')
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    views = models.IntegerField('Просмотры', default=1)

    # sizes = (
    #     ('S', 'Small'),
    #     ('M', 'Medium'),
    #     ('L', 'Large'),
    #     ('XL', 'X Large'),
    # )

    # shop_sizes = models.CharField(max_length=2, choices=sizes, default='S', verbose_name='Размеры')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Tasks(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тема')
    task = models.TextField(verbose_name='Описание задания')
    answer = models.IntegerField(verbose_name='Ответ')
    date = models.DateTimeField(verbose_name='Дата')
    level = models.FloatField(verbose_name='Уровень сложности', default=1.0, help_text='Что-то')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'