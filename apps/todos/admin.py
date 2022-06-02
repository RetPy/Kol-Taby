from django.contrib import admin

from apps.todos.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status')
    list_display_links = ('id', 'title')
