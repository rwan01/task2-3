# from django.contrib import admin # type: ignore
# from .models import Product

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ("name", "price", "stock", "created_at")

# admin.site.register(Product)


from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at')
    # readonly_fields = ('created_at',)  #

admin.site.register(Product, ProductAdmin)