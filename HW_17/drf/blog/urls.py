from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('posts/', views.posts, name='post_list'),
    path('posts/<int:id>/', views.post),
    path('comments/', views.comments, name='comment_list'),
    path('comments/<int:id>/', views.comment),
    path('categories/', views.categories, name='category_list'),
    path('categories/<int:id>/', views.category),
]
