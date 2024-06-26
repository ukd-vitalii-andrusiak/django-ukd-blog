from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('category/<int:category_id>/', views.post_list, name='category_posts'),
    path('post/<slug:permalink>/', views.post_detail, name='post_detail'),
]
