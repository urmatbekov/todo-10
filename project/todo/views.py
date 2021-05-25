from django.shortcuts import render
from .models import TodoItem
# Create your views here.
def todo_list(request):
    todo_items = TodoItem.objects.all()
    return render(request,"todo/todo-list.html",{"todo_items":todo_items})