from django.db import models

# Create your models here.
class News_post(models.Model):
    title = models.CharField('Название новости', max_length=200)
    short_description = models.CharField('Краткое описание новости', max_length=250)
    text = models.TextField('Текст новости')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
