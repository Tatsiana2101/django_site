
from django.db import models


class Positions(models.Model):
    name = models.CharField('Название товара', max_length=200)
    image1 = models.ImageField('Изображение1', upload_to="img/")
    image2 = models.ImageField('Изображение2', upload_to="img/")
    image3 = models.ImageField('Изображение3', upload_to="img/")
    notes = models.TextField('Метки')
    article = models.CharField('Артикул', max_length=20)
    price = models.CharField('Цена', max_length=10)
    priceSale = models.CharField('Цена со скидкой', max_length=10)

    @property
    def photo_url(self):
        if self.image1 and hasattr(self.image1, 'url'):
            return self.image1.url

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Свадебное платье'
        verbose_name_plural = 'Свадебные платья'


class Evening(models.Model):
    name = models.CharField('Название товара', max_length=200)
    image1 = models.ImageField('Изображение1', upload_to="'static/img'")
    image2 = models.ImageField('Изображение2', upload_to="'static/img'")
    image3 = models.ImageField('Изображение3', upload_to="'static/img'")
    article = models.CharField('Артикул', max_length=20)
    price = models.CharField('Цена', max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вечернее платье'
        verbose_name_plural = 'Вечерние платья'


class Shoes(models.Model):
    name = models.CharField('Название товара', max_length=200)
    image1 = models.ImageField('Изображение1', upload_to="'static/img'")
    article = models.CharField('Артикул', max_length=20)
    price = models.IntegerField('Цена')
    type = models.IntegerField('Тип обуви')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Обувь'
        verbose_name_plural = 'Обувь'


class Veil(models.Model):
    name = models.CharField('Название товара', max_length=200)
    image1 = models.ImageField('Изображение1', upload_to="'static/img'")
    article = models.CharField('Артикул', max_length=20)
    price = models.IntegerField('Цена')
    type = models.IntegerField('Тип фаты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фата'
        verbose_name_plural = 'Фата'


class Accessories(models.Model):
    name = models.CharField('Название товара', max_length=200)
    image1 = models.ImageField('Изображение1', upload_to="'static/img'")
    article = models.CharField('Артикул', max_length=20)
    price = models.IntegerField('Цена')
    type = models.IntegerField('Тип аксессуара')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Аксессуар'
        verbose_name_plural = 'Аксессуары'


class Sale(models.Model):
    name = models.CharField('Название товара', max_length=200)
    image1 = models.ImageField('Изображение1', upload_to="img/")
    image2 = models.ImageField('Изображение2', upload_to="img/")
    image3 = models.ImageField('Изображение3', upload_to="img/")
    notes = models.TextField('Метки')
    article = models.CharField('Артикул', max_length=20)
    price = models.IntegerField('Цена')
    priceSale = models.IntegerField('Цена со скидкой')

    @property
    def photo_url(self):
        if self.image1 and hasattr(self.image1, 'url'):
            return self.image1.url

    def __str__(self):
        return self.name


class Wedding(models.Model):
    name = models.CharField('Название товара', max_length=200)
    image1 = models.ImageField('Изображение1', upload_to="img/")
    image2 = models.ImageField('Изображение2', upload_to="img/")
    image3 = models.ImageField('Изображение3', upload_to="img/")
    notes = models.TextField('Метки')
    article = models.CharField('Артикул', max_length=20)
    price = models.IntegerField('Цена')
    priceSale = models.IntegerField('Цена')
    type = models.IntegerField('Тип платья')
    color = models.IntegerField('Цвет платья')

    @property
    def photo_url(self):
        if self.image1 and hasattr(self.image1, 'url'):
            return self.image1.url

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Свадебное платье'
        verbose_name_plural = 'Свадебные платья'


class EveningDress(models.Model):
    name = models.CharField('Название товара', max_length=200)
    image1 = models.ImageField('Изображение1', upload_to="'static/img'")
    image2 = models.ImageField('Изображение2', upload_to="'static/img'")
    image3 = models.ImageField('Изображение3', upload_to="'static/img'")
    article = models.CharField('Артикул', max_length=20)
    price = models.IntegerField('Цена')
    type = models.IntegerField('Тип платья')
    color = models.IntegerField('Цвет платья')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вечернее платье'
        verbose_name_plural = 'Вечерние платья'