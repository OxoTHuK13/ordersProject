from django.db import models


class Customer(models.Model):
    name = models.CharField('ФИО', max_length=255)
    passport = models.CharField('Паспорт', max_length=11, blank=True, null=True)
    email = models.EmailField('Email', max_length=50, blank=True, null=True)
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True, verbose_name='Статус')
    discount = models.ForeignKey('Discount', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Скидка')
    time_create = models.DateTimeField('Время создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField('Город', max_length=255)
    region = models.ForeignKey('Region', on_delete=models.CASCADE, verbose_name='Регион')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['region', 'name', ]

    def __str__(self):
        return f'{self.name}, {self.region}'


class Region(models.Model):
    name = models.CharField('Регион', max_length=150, unique=True)

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'
        ordering = ['name', ]

    def __str__(self):
        return self.name


class Address(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, verbose_name='Клиент')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город, Регион')
    address = models.CharField('Адрес', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return f'{self.city}, {self.address}'


class Status(models.Model):
    name = models.CharField('Наименование', max_length=50)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name


class Discount(models.Model):
    amount = models.PositiveSmallIntegerField('Размер скидки', unique=True)

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self):
        return f'{self.amount}%'


class PhoneNumber(models.Model):
    number = models.CharField('Номер телефона', max_length=11, unique=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, verbose_name='ФИО')
    messenger = models.ForeignKey('Messenger', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Мессенджер')

    class Meta:
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номера телефонов'

    def __str__(self):
        return f'{self.number}'


class Messenger(models.Model):
    name = models.CharField(max_length=15, verbose_name='Мессенджер')

    class Meta:
        verbose_name = 'Мессенджер'
        verbose_name_plural = 'Мессенджеры'

    def __str__(self):
        return f'{self.name}'
