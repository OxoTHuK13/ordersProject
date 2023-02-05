from django.db import models

from customers.models import *
from tanks.models import *


class DeliveryCompany(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Транспортная компания'
        verbose_name_plural = 'Транспортные компании'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Покупатель')
    tank = models.ManyToManyField(Tank, verbose_name='Бак')
    comment = models.TextField(verbose_name='Комментарий', null=True, blank=True)
    delivery = models.ForeignKey(DeliveryCompany, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='Доставка')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'ID: {self.pk}, {self.customer}'

    def get_status(self):
        return HistoryOrderStatus.objects.filter(order_id=self.pk).last().order_status

    def get_status_date(self):
        return HistoryOrderStatus.objects.filter(order_id=self.pk).last()


class OrderStatus(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'

    def __str__(self):
        return self.name


class HistoryOrderStatus(models.Model):
    status_date = models.DateTimeField('Время статуса', auto_now_add=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, verbose_name='Статус')

    class Meta:
        verbose_name = 'Время статуса'
        verbose_name_plural = 'Время статуса'

    def __str__(self):
        return f'{self.status_date}'

    # TODO: Создать модель допников
    # TODO: Создать модель Производство
    # TODO: Реализовать добавление в Производство баков из заказа
    # TODO: Реализовать добавление в Производство баков из Приходного ордера (подумать)
