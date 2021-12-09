from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('all_posts/', views.all_posts, name='all_posts'),
    path('all_posts/<slug:slug>/', views.post_detail, name='post_detail'),
    path('all_category/', views.all_category, name='all_category'),
    path('all_category/<int:id>/', views.category_detail, name='category_detail'),
    path('list_post/', views.ListPost.as_view(), name='list_post'),
    path('list_post/<slug:myslug>/', views.DetailPost.as_view(), name='detail_post'),
    path('list_category/', views.ListCategory.as_view(), name='list_category'),
    path('list_category/<int:pk>', views.DetailCategory.as_view(), name='detail_category'),
]
