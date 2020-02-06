from django.urls import path
from .views import BottleList, BottleListDetail

urlpatterns = [
    path('bottles/', BottleList.as_view(), name='bottle_list'),
    path('bottles/<int:pk>/', BottleListDetail.as_view(), name='bottle_list'),
]