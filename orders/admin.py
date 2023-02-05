from django.contrib import admin

from orders.models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status',)
    list_filter = ('customer', 'status',)
    filter_horizontal = ('tank',)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderStatus)
