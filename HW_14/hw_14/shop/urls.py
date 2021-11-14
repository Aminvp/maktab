from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.sayCategory),
    path('all_category/', views.All_Category)
]