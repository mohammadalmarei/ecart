from django.urls import path, include

from .views import (
    CategoryList,
    ProductByCategory,
    ProductInventoryByWebId,
    AllProductInventory,
    SearchProductInventory,
    ProductByStock,
    AllProducts,
)

urlpatterns = [
    path("category/all/", CategoryList.as_view()),
    path(
        "products/category/<str:query>/",
        ProductByCategory.as_view(),
    ),
    path("products/all/", AllProductInventory.as_view()),
    path("product/all/", AllProducts.as_view()),
    path("<str:query>/", ProductInventoryByWebId.as_view()),
    path("product/search/<str:query>/", SearchProductInventory.as_view()),
    path("products/highest-sold/", ProductByStock.as_view()),
]
