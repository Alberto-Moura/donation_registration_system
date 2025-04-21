from django.urls import path
from .views import institution_data

urlpatterns = [
    path('institution/<int:pk>/', institution_data, name='institution_data'),
]