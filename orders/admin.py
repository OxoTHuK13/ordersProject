from django.contrib import admin

from orders.models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', )
    list_filter = ('customer', 'customer__email')
    filter_horizontal = ('tank',)


admin.site.register(Order, OrderAdmin)
