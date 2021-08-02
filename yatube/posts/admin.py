"""
Не уверен, что правильно выполнил импорты, но вроде как под эти параметры подходит:
1. Стандартные библиотеки
2. Сторонние библиотеки (django)
3. Локальные библиотеки (views)

Между этими группами пробел.
"""

from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
