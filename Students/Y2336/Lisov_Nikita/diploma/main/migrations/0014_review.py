# Generated by Django 3.2.3 on 2021-05-26 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0013_alter_books_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Название')),
                ('discription', models.TextField(verbose_name='Описание')),
                ('minus_rating', models.IntegerField(verbose_name='Отрицательный рейтинг')),
                ('plus_rating', models.IntegerField(verbose_name='Положительный рейтинг')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.books', verbose_name='Книга')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
            options={
                'verbose_name': 'Рецензия',
                'verbose_name_plural': 'Рецензии',
            },
        ),
    ]
