# Generated by Django 3.2.3 on 2021-05-24 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='writer',
            name='type',
        ),
    ]
