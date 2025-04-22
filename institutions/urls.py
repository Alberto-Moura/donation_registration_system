from django.urls import path
from .views import institution_data, institution_by_type

urlpatterns = [
    path('institution/<int:pk>/', institution_data, name='institution_data'),
    path('institution/type/<int:type_id>/', institution_by_type, name='institution_by_type')
]
