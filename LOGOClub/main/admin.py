from django.contrib import admin
# Register your models here.
# Из модуля models импортируем модель Post
from .models import Post


class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('title', 'text',) 
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('title', 'text',)
    empty_value_display = '-пусто-'


# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(Post, PostAdmin)