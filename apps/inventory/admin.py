from django.contrib import admin

from .models import Product, Category, ProductInventory

admin.site.register(Product)
admin.site.register(Category)


class InventoryAdmin(admin.ModelAdmin):
    list_display = ("product", "store_price")


admin.site.register(ProductInventory, InventoryAdmin)
