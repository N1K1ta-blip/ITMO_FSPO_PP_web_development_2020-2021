# Generated by Django 3.2.3 on 2021-05-30 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_likesreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likesreview',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.review', verbose_name='Статья'),
        ),
    ]