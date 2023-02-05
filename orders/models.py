from django.db import models

from customers.models import *
from tanks.models import *


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Покупатель')
    tank = models.ManyToManyField(Tank, verbose_name='Бак')
    comment = models.TextField(verbose_name='Комментарий', null=True, blank=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'ID: {self.pk}, {self.customer}'

    # TODO: Создать модель со статусами заказа и добавить в форму заказа
    # TODO: Создать модель допников
    # TODO: Создать модель Производство
    # TODO: Реализовать добавление в Производство баков из заказа
    # TODO: Реализовать добавление в Производство баков из Приходного ордера (подумать)
