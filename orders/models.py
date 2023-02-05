from django.db import models

from customers.models import *
from tanks.models import *


class OrderStatus(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Покупатель')
    tank = models.ManyToManyField(Tank, verbose_name='Бак')
    comment = models.TextField(verbose_name='Комментарий', null=True, blank=True)
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='Статус заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'ID: {self.pk}, {self.customer}'

    # TODO: Сделать так, чтоб у заказа сохранялась история статусов с указанием даты/времени
    # TODO: Создать модель допников
    # TODO: Создать модель Производство
    # TODO: Реализовать добавление в Производство баков из заказа
    # TODO: Реализовать добавление в Производство баков из Приходного ордера (подумать)
