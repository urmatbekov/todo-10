# Generated by Django 3.2.3 on 2021-05-25 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todoitem_priority'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todoitem',
            options={'verbose_name': 'Дела', 'verbose_name_plural': 'Список дел'},
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создано'),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='description',
            field=models.TextField(verbose_name='Объеснение'),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='finish_time',
            field=models.DateTimeField(verbose_name='Время оканчания'),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='name',
            field=models.CharField(max_length=244, verbose_name='Названия'),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='priority',
            field=models.CharField(choices=[('high', 'Высокий'), ('midle', 'Средний'), ('low', 'Низкий')], default='midle', max_length=10, verbose_name='Пиаритет'),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='status',
            field=models.CharField(choices=[('pending execution', 'Ожидает выполнения'), ('completed', 'Выполнена'), ('in progress', 'В процессе выполнения')], default='pending execution', max_length=20, verbose_name='Статус'),
        ),
    ]
