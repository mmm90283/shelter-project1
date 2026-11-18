from django.contrib import admin
from django.utils.html import format_html
from .models import Animal, AdoptionRequest

# Настройка заголовков админки
admin.site.site_header = "Приют «Мир животных»"
admin.site.site_title = "Мир животных"
admin.site.index_title = "Панель управления приютом"

# Класс для подключения стилей админки
class AdminStyleMixin:
    class Media:
        css = {
            'all': ('css/admin.css',)
        }

@admin.register(Animal)
class AnimalAdmin(AdminStyleMixin, admin.ModelAdmin):
    list_display = ('name', 'age', 'is_adopted', 'created_at', 'photo_preview')
    list_filter = ('is_adopted',)
    search_fields = ('name', 'description')

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="width: 50px; height: 50px; border-radius: 5px;" />', obj.photo.url)
        return "Нет фото"
    photo_preview.short_description = "Фото"

@admin.register(AdoptionRequest)
class AdoptionRequestAdmin(AdminStyleMixin, admin.ModelAdmin):
    list_display = ('name', 'phone', 'animal', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone', 'email')