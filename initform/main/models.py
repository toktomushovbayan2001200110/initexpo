from django.db import models

# Create your models here.
# main/models.py
from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=255)
    anons = models.TextField()
    full_text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    views_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='articles_images/', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
