from django.contrib import admin
from django.template.defaultfilters import safe

from .models import *


class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 0


class AddressInline(admin.TabularInline):
    model = Address
    extra = 0


class CityInline(admin.TabularInline):
    model = City
    extra = 0
    ordering = ['name']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_phone_numbers', 'get_city', 'status', 'discount', 'time_create', ]
    list_filter = ['status', 'discount', 'address__city__region', 'address__city']
    list_display_links = ['id', 'name']
    ordering = ['name', ]
    search_fields = ['name', 'phonenumber__number', 'address__city__name']
    search_help_text = 'Поиск по номеру телефона, городу или  ФИО с учетом регистра.'
    radio_fields = {'discount': admin.HORIZONTAL}
    inlines = [PhoneNumberInline, AddressInline, ]

    @admin.display(description='Номер телефона')
    def get_phone_numbers(self, obj):
        numbers = obj.phonenumber_set.all()
        numbers_list = [number.number for number in numbers if numbers]
        return safe('<br>'.join(numbers_list))

    @admin.display(description='Город, Регион')
    def get_city(self, obj):
        cities = obj.address_set.order_by('address')
        cities_list = [city.city.__str__() for city in cities if cities]
        return safe('<br>'.join(cities_list))


class PhoneNumberAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer', ]
    list_display = ['number', 'customer']
    search_fields = ['number', 'customer__name']
    search_help_text = 'Поиск по номеру телефона или по ФИО с учетом регистра.'


class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'region']
    list_display_links = ['name', 'region']
    list_filter = ['region']


class RegionAdmin(admin.ModelAdmin):
    inlines = [CityInline, ]


class AddressAdmin(admin.ModelAdmin):
    list_display = ['city', 'address', 'customer']
    search_fields = ['city__name', 'customer__name', 'address']
    search_help_text = 'Поиск по городу, ФИО и адресу с учетом регистра'
    list_filter = ['city', ]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Status)
admin.site.register(Discount)
admin.site.register(PhoneNumber, PhoneNumberAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Messenger)

