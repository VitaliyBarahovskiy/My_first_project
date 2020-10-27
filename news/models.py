from django.db import models
from django.urls import reverse
from django.contrib.auth.models import *

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True,verbose_name='Контент')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateField(auto_now=True, verbose_name='Обновленно')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категориия',
    related_name='get_news')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})


    def __str__(self):
        return self.title



    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"
        ordering = ['title']
