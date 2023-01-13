from django.shortcuts import render
from product.models import Product, Category
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from product.serializers import ProductSerializer, CategorySerializer
from rest_framework.decorators import api_view
import logging
from django.views.generic import ListView

logger = logging.getLogger(__name__)


class CategoryAPIView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

class ProductAPIView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


@api_view(['GET'])
def get_hello(request):
    logger.info(request.user)
    # print(request.hello)
    return Response("Example")


class ProductTemplateList(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'