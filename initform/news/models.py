from django.db import models
from ckeditor.fields import RichTextField

class Articles(models.Model):
    title = models.CharField('Название', max_length=100, unique=True)
    anons = models.CharField('Анонс', max_length=250)
    full_text = RichTextField('Статья')  # Использование Rich Text Editor
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    image = models.ImageField('Изображение', upload_to='news_images/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
