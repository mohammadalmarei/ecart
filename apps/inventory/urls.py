from django.urls import path, include
from .views import CategoryList

urlpatterns = [
    path("category/all/", CategoryList.as_view()),
]
