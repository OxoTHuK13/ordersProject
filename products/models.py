from django.db import models

from orders.models import Order
from tanks.models import *


class ProductStatus(models.Model):
    name = models.CharField(max_length=25, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Статус бака'
        verbose_name_plural = 'Статус баков'

    def __str__(self):
        return self.name


class Product(models.Model):
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE, verbose_name='Бак')
    status = models.ForeignKey(ProductStatus, on_delete=models.CASCADE, verbose_name='Статус')
    date = models.DateField(verbose_name='Дата')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Производство'
        verbose_name_plural = 'Производство'

    def __str__(self):
        return self.tank.name
