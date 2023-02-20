from django.contrib import admin

from .models import *


class TankToVehicleInline(admin.TabularInline):
    model = TankToVehicle
    fields = ['vehicle', ]
    extra = 0
    # list_select_related = ['vehicle', 'vehicle_type']


class TankAdmin(admin.ModelAdmin):
    readonly_fields = ['volume', 'cut_cost', 'welding_cost', 'metal_cost', 'cost', 'price', ]
    fieldsets = [
        ('Параметры для расчета',
         {'fields': ['name', 'gross_volume', 'weld_length', 'excluded_volume', 'weight', 'difficult_koef', 'description', ],
          'classes': ['collapse']}),
        (None, {'fields': ['regular', 'cut_cost', 'welding_cost', 'metal_cost', 'cost', 'volume', 'price', 'sketch', 'vehicles']})
    ]
    list_display = ['name', 'weight', 'price', 'regular']
    list_editable = ['regular']
    inlines = [TankToVehicleInline, ]
    list_filter = ['regular', 'vehicles__vehicle_type', 'vehicles', ]


class VehicleAdmin(admin.ModelAdmin):
    # filter_horizontal = ['tanks', ]
    list_filter = ['vehicle_type', ]
    list_display = ['name', 'vehicle_type', ]
    ordering = ['vehicle_type', 'name', ]


admin.site.register(Tank, TankAdmin)
admin.site.register(Cost)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleType)
# admin.site.register(VehicleModel)

admin.site.site_title = 'Админ-панель ВсеБаки'
admin.site.site_header = 'Админ-панель ВсеБаки'
