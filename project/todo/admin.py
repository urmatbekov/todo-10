from django.contrib import admin
from .models import TodoItem

# Register your models here.


class TodoItemAdmin(admin.ModelAdmin):
    list_display = ["name","priority","created_at","finish_time","status"]
    list_editable = ["priority","status"]
    search_fields = ["name","description"]
    list_filter = ["priority","status"]
    list_per_page = 15

admin.site.register(TodoItem,TodoItemAdmin)