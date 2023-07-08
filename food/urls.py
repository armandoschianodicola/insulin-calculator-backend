from django.urls import path, include
from .views import (
    FoodListApiView,
    FoodDetailApiView
)

urlpatterns = [
    path('api', FoodListApiView.as_view()),
    path('api/<int:food_id>', FoodDetailApiView.as_view()),
]
