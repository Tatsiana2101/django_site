# Generated by Django 3.2.3 on 2021-05-19 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterField(
            model_name='task',
            name='price',
            field=models.IntegerField(verbose_name='Количество звезд'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task',
            field=models.TextField(verbose_name='Отзыв'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Ваше имя'),
        ),
    ]
