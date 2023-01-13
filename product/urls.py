from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import ProductAPIView, CategoryAPIView, ProductTemplateList, get_hello


router = DefaultRouter()
router.register("", ProductAPIView)
router.register("category", CategoryAPIView)


urlpatterns = [
    path('hello/', get_hello),
    path('list/', ProductTemplateList.as_view()),
    path('', include(router.urls)),
    
]