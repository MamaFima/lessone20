from django.db import models
from django.contrib.auth.models import User  

class News_post(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)  # Поле user с опцией null=True
    title = models.CharField('Название новости', max_length=200)
    short_description = models.CharField('Краткое описание новости', max_length=250)
    text = models.TextField('Текст новости')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Article(models.Model):
    title = models.CharField('Название статьи', max_length=200)
    short_description = models.CharField('Краткое описание статьи', max_length=250)
    text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


