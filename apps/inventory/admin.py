from django.contrib import admin

from .models import (
    Product,
    Category,
    Brand,
    ProductAttribute,
    ProductType,
    ProductAttributeValue,
    ProductInventory,
    Media,
    Stock,
    ProductAttributeValues,
    ProductTypeAttribute,
)

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductAttribute)
admin.site.register(ProductType)
admin.site.register(ProductAttributeValue)


class InventoryAdmin(admin.ModelAdmin):
    list_display = ("product", "store_price")


admin.site.register(ProductInventory, InventoryAdmin)

admin.site.register(Media)
admin.site.register(Stock)
admin.site.register(ProductAttributeValues)
admin.site.register(ProductTypeAttribute)
