# Generated by Django 3.2.3 on 2021-05-24 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_auto_20210524_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('HIS', 'Историческая'), ('LIT', 'Литературная')], max_length=3, verbose_name='Тип')),
                ('name', models.TextField(verbose_name='Имя')),
                ('date_life', models.TextField(verbose_name='Даты жизни')),
                ('biografi', models.TextField(verbose_name='Биография')),
                ('status', models.BooleanField(default=False, verbose_name='Статус')),
                ('image', models.ImageField(blank=True, null=True, upload_to=main.models.generate_imageset_upload_to)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
            options={
                'verbose_name': 'Писатель',
                'verbose_name_plural': 'Писатели',
            },
        ),
    ]
