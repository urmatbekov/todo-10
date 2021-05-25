# Generated by Django 3.2.3 on 2021-05-25 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('finish_time', models.DateTimeField()),
                ('priority', models.CharField(choices=[('high', 'Высокий'), ('midle', 'Средний'), ('low', 'Низкий')], max_length=10)),
                ('name', models.CharField(max_length=244)),
                ('description', models.TextField()),
            ],
        ),
    ]