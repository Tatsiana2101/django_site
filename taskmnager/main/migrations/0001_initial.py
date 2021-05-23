# Generated by Django 3.2.3 on 2021-05-17 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Назыывние')),
                ('task', models.TextField(verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
        ),
    ]
