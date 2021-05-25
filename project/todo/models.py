from django.db import models

# Create your models here.

PRIORITY_CHOICES = [
    ("high","Высокий"),
    ("midle","Средний"),
    ("low","Низкий")
]

STATUS_CHOICES= [
    ("pending execution","Ожидает выполнения"),
    ("completed","Выполнена"),
    ("in progress","В процессе выполнения")
]

class TodoItem(models.Model):
    created_at = models.DateTimeField("Создано",auto_now_add=True)
    finish_time = models.DateTimeField("Время оканчания")
    priority = models.CharField("Приоритет",default="midle",max_length=10,choices=PRIORITY_CHOICES)
    status = models.CharField("Статус",default="pending execution",max_length=20,choices=STATUS_CHOICES)
    name = models.CharField("Названия",max_length=244)
    description = models.TextField("Описания")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Дела"
        verbose_name_plural = "Список дел"

    
