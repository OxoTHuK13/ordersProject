from django.contrib import admin

from products.models import Product, ProductStatus


class ProductAdmin(admin.ModelAdmin):
    list_display = ('tank', 'order', 'status', 'date')
    list_filter = ('tank', 'status')
    list_display_links = ('tank', 'order')
    list_editable = ('status', 'date')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductStatus)
