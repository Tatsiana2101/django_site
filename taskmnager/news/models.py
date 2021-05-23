from django.db import models


class Products(models.Model):
    name = models.CharField('Название товара', max_length=200)
    image1 = models.ImageField('Изображение1', upload_to="img/")
    image2 = models.ImageField('Изображение2', upload_to="img/")
    image3 = models.ImageField('Изображение3', upload_to="img/")
    notes = models.TextField('Метки')
    article = models.CharField('Артикул', max_length=20)
    price = models.CharField('Цена', max_length=10)
    priceSale = models.CharField('Цена со скидкой', max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

