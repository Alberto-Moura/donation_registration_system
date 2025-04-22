from django.urls import path
from .views import product_data

urlpatterns = [
    path('product/<int:pk>/', product_data, name='product_data')
]
