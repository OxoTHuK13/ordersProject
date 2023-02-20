import os

from django.db import models
from django.db.models.functions import math
from unidecode import unidecode


def get_path_for_sketches(instance, filename):
    try:
        # translated_path = 'brothers'
        print(instance.vehicles.name, type(instance.vehicles.name))
        translated_path = unidecode(instance.vehicles.name).lower().replace(' ', '-').replace('-', '-')
    except AttributeError:
        translated_path = 'others'
    translated_filename = unidecode(filename).lower().replace(' ', '-')
    try:
        os.remove(instance.old_sketch_path)
        print(f'ФАЙЛ {instance.old_sketch_path} БЫЛ УСПЕШНО УДАЛЕН')
    except:
        print(f'Файл {instance.old_sketch_path} не существует и потому не был удален')
    return f'sketches/{translated_path}/{translated_filename}'


class Cost(models.Model):
    welding = models.DecimalField('Цена за см шва, руб', max_digits=4, decimal_places=2)
    cut = models.DecimalField('Цена за см реза, руб', max_digits=4, decimal_places=2)
    metal = models.DecimalField('Цена кг металла, руб', max_digits=6, decimal_places=2)
    dut = models.DecimalField('Цена ДУТ ВАЗ, руб', max_digits=5, decimal_places=2)
    time_create = models.DateTimeField('Время создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Константа'
        verbose_name_plural = 'Константы'
        ordering = ['-time_create']

    def __str__(self):
        return str(self.time_create)

    def save(self, *args, **kwargs):
        super(Cost, self).save(*args, **kwargs)
        tanks = Tank.objects.all()
        for tank in tanks:
            tank.save(*args, **kwargs)


class VehicleType(models.Model):
    name = models.CharField('Тип ТС', max_length=25)

    class Meta:
        verbose_name = 'Тип ТС'
        verbose_name_plural = 'Типы ТС'

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    name = models.CharField('Наименование', max_length=150)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.SET_NULL, null=True, verbose_name='Тип ТС')

    # tanks = models.ManyToManyField('Tank', verbose_name='Наименование бака', related_name='vehicles', blank=True)

    class Meta:
        verbose_name = 'Транспортное средство'
        verbose_name_plural = 'Транспортные средства'

    def __str__(self):
        return self.name


# class VehicleModel(models.Model):
#     name = models.CharField('Наименование', max_length=150)
#     vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='ТС')
#
#     class Meta:
#         verbose_name = 'Модель Транспортного средства'
#         verbose_name_plural = 'Модель Транспортных средств'
#
#     def __str__(self):
#         return self.name


# FIXME: При создании новой записи, если выбран скетч, выпадает ошибка (т.к. путь еще не найден).
# FIXME: При удалении скетча удалить файл из папки.
class Tank(models.Model):
    name = models.CharField('Бак', max_length=255)
    gross_volume = models.DecimalField('Общий Объем, л', max_digits=5, decimal_places=2, default=0.00)
    excluded_volume = models.DecimalField('Исключаемый Объем, л', max_digits=5, decimal_places=2, default=0,
                                          help_text='Объем стенок бака и перегородок')
    volume = models.DecimalField('Полезный объем, л', max_digits=5, decimal_places=2, editable=False, null=True)
    weld_length = models.IntegerField('Длина шва, см')
    weight = models.DecimalField('Вес, кг', max_digits=3, decimal_places=1)
    description = models.TextField(blank=True, verbose_name='Описание')
    difficult_koef = models.DecimalField('Надбавка за сложность, руб', max_digits=6, decimal_places=2, null=True,
                                         blank=True, default=0.00)
    regular = models.BooleanField('Проверенный', db_index=True)
    cut_cost = models.DecimalField('Раскрой, руб', max_digits=7, decimal_places=2, null=True, editable=False)
    welding_cost = models.DecimalField('Сварка, руб', max_digits=7, decimal_places=2, null=True, editable=False)
    metal_cost = models.DecimalField('Металл, руб', max_digits=7, decimal_places=2, null=True, editable=False)
    cost = models.DecimalField('Себестоимость, руб', max_digits=7, decimal_places=2, null=True, editable=False)
    price = models.DecimalField('Цена, руб', max_digits=7, decimal_places=2, null=True, editable=False)
    vehicles = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='Транспортное средство',
                                 blank=True, null=True)
    sketch = models.ImageField('Чертеж', upload_to=get_path_for_sketches, null=True, blank=True)

    # FIXME: Придумать связи между Баком, ТС и Моделью ТС, чтоб в админке сделать инлайн у бака: ТС -- Модель ТС
    class Meta:
        verbose_name = 'Бак'
        verbose_name_plural = 'Баки'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        const = Cost.objects.first()
        self.volume = self.gross_volume - self.excluded_volume
        self.cut_cost = const.cut * self.weld_length
        self.welding_cost = const.welding * self.weld_length
        self.metal_cost = const.metal * self.weight
        self.cost = self.cut_cost + self.welding_cost + self.metal_cost
        self.price = math.Ceil((self.difficult_koef + self.cost * 2 + const.dut) / 100) * 100
        super(Tank, self).save(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super(Tank, self).__init__(*args, **kwargs)
        if self.sketch:
            self.old_sketch_path = self.sketch.path
        else:
            self.old_sketch_path = ''


class TankToVehicle(models.Model):
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE, verbose_name='Бак')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='ТС')

    # vehicle_model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE, verbose_name='Модель ТС')
    class Meta:
        verbose_name = 'ТС'
        verbose_name_plural = 'ТС'

    def __str__(self):
        return f'{self.vehicle}'
