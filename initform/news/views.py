from django.shortcuts import render
from django.views.generic import DetailView
from .models import Articles

def news_home(request):
    # Сортировка новостей по дате (от новых к старым)
    news = Articles.objects.all().order_by('-date')  # Добавили сортировку по дате
    return render(request, 'news/news_home.html', {"news": news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/news_detail_view.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj:
            # Здесь вы можете обрабатывать ситуацию, если объект не найден
            raise Http404("Статья не найдена.")
        return obj
