from django.urls import path
from . import views

urlpatterns = [
    path('published/', views.Published, name='publish'),
]