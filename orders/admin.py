from django.contrib import admin

from orders.models import *


class HistoryOrderStatusInline(admin.TabularInline):
    model = HistoryOrderStatus
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'status_date', 'delivery')
    list_filter = ('customer', 'status')
    filter_horizontal = ('tank',)
    inlines = (HistoryOrderStatusInline,)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderStatus)
admin.site.register(DeliveryCompany)
