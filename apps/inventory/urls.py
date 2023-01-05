from django.urls import path, include

from .views import (
    CategoryList,
    ProductByCategory,
    ProductInventoryByWebId,
    SearchProductInventory,
)

urlpatterns = [
    path("category/all/", CategoryList.as_view()),
    path(
        "products/category/<str:query>/",
        ProductByCategory.as_view(),
    ),
    path("<int:query>/", ProductInventoryByWebId.as_view()),
    path("<str:query>/", SearchProductInventory.as_view()),
]
