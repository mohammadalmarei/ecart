from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from elasticsearch_dsl import Q

from .models import Category, Product, ProductInventory
from .documents import ProductInventoryDocument
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ProductInventorySerializer,
    ProductInventorySearchSerializer,
)


class CategoryList(APIView):
    """
    Return a list of all categories
    """

    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class ProductByCategory(APIView):
    """
    Return product by category
    """

    def get(self, request, query=None):
        queryset = ProductInventory.objects.filter(product_id__category_id__slug=query)
        serializer = ProductInventorySerializer(queryset, many=True)
        return Response(serializer.data)


class ProductInventoryByWebId(APIView):
    """
    Return Sub Product by WebId
    """

    def get(self, request, query=None):
        queryset = ProductInventory.objects.filter(product__web_id=query)
        serializer = ProductInventorySerializer(queryset, many=True)
        return Response(serializer.data)


class AllProductInventory(APIView):
    """
    Return Sub Product by WebId
    """

    def get(self, request):
        queryset = ProductInventory.objects.all()[:20]
        serializer = ProductInventorySerializer(queryset, many=True)
        return Response(serializer.data)


class AllProducts(APIView):
    """
    Return Sub Product by
    """

    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductByStock(APIView):
    """
    Return Product by Stock
    """

    def get(self, request):
        queryset = ProductInventory.objects.all().order_by(
            "product_inventory__units_sold"
        )[:3]
        serializer = ProductInventorySerializer(queryset, many=True)
        return Response(serializer.data)


class SearchProductInventory(APIView, LimitOffsetPagination):
    productinventory_serializer = ProductInventorySearchSerializer
    search_document = ProductInventoryDocument

    def get(self, request, query=None):
        try:
            q = Q(
                "multi_match",
                query=query,
                fields=["product.name", "product.web_id", "brand.name"],
                fuzziness="auto",
            ) & Q(
                should=[
                    Q("match", is_default=True),
                ],
                minimum_should_match=1,
            )

            search = self.search_document.search().query(q)
            response = search.execute()

            results = self.paginate_queryset(response, request, view=self)
            serializer = self.productinventory_serializer(results, many=True)
            return self.get_paginated_response(serializer.data)

        except Exception as e:
            return HttpResponse(e, status=500)
