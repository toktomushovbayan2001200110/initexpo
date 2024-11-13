from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Including URLs from the main app
    path('news/', include('news.urls')),
    path('expo/', include('expo.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Corrected MEDIA_ROOT
