from django.urls import path
# from .views import 

urlpatterns = [
    path('api/v1/', MyView.as_view(),name='my_view')
]

