from django.contrib import admin
from .models import Articles

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')  # Поля, которые будут отображаться в списке
    search_fields = ('title',)  # Поля для поиска
    list_filter = ('date',)  # Фильтры по дате

admin.site.register(Articles, ArticlesAdmin)
