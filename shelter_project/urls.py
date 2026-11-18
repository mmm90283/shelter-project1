from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from shelter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('animals/', views.animals_view, name='animals'),
    path('rules/', views.rules, name='rules'),
    path('contacts/', views.contacts, name='contacts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)