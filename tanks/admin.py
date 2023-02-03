from django.contrib import admin

from .models import *


class VehicleInline(admin.TabularInline):
    model = Tank.vehicles.through
    fields = ['vehicle', ]
    extra = 0


class TankAdmin(admin.ModelAdmin):
    readonly_fields = ['volume', 'cut_cost', 'welding_cost', 'metal_cost', 'cost', 'price', ]
    fieldsets = [
        ('Параметры для расчета',
         {'fields': ['name', 'gross_volume', 'weld_length', 'excluded_volume', 'weight', 'difficult_koef', 'description', ],
          'classes': ['collapse']}),
        (None, {'fields': ['regular', 'cut_cost', 'welding_cost', 'metal_cost', 'cost', 'volume', 'price', 'sketch', ]})
    ]
    list_display = ['name', 'weight', 'price', 'regular']
    list_editable = ['regular']
    inlines = [VehicleInline, ]
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

admin.site.site_title = 'Админ-панель ВсеБаки'
admin.site.site_header = 'Админ-панель ВсеБаки'
