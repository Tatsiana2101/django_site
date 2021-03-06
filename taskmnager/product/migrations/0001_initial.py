# Generated by Django 3.2.3 on 2021-05-19 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название товара')),
                ('image1', models.ImageField(upload_to='img/', verbose_name='Изображение1')),
                ('image2', models.ImageField(upload_to='img/', verbose_name='Изображение2')),
                ('image3', models.ImageField(upload_to='img/', verbose_name='Изображение3')),
                ('notes', models.TextField(verbose_name='Метки')),
                ('article', models.CharField(max_length=20, verbose_name='Артикул')),
                ('price', models.CharField(max_length=10, verbose_name='Цена')),
                ('priceSale', models.CharField(max_length=10, verbose_name='Цена со скидкой')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
