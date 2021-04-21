from django.db import models
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=150 , verbose_name='Новость')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True, verbose_name='Фото')
    is_published = models.BooleanField(default= True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category',on_delete=models.PROTECT , null= True, verbose_name='Категория')

    def get_absolute_url(self): #reverse строит ссылку, как и тег {% url "имя" %}, только с учетом на py файлы
        return reverse('view_news', kwargs={"news_id":self.pk}) # Вызываем функцию reverse.
        # в первый параметр передаем название маршрута, а во второй необходимый параметр для построения маршрута.
        # Используя данный метод, джанго сам выстроет ссылку

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = "Новость"
        ordering = ['-created_at']


class Category(models.Model):
    title = (models.CharField(max_length=150, db_index=True, verbose_name='Название категории'))

    def get_absolute_url(self): #reverse строит ссылку, как и тег {% url "имя" %}, только с учетом на py файлы
        return reverse('cat', kwargs={"category_id":self.pk}) # Вызываем функцию reverse.
        # в первый параметр передаем название маршрута, а во второй необходимый параметр для построения маршрута.
        # Используя данный метод, джанго сам выстроет ссылку


    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = "Категория"


# Create your models here.
