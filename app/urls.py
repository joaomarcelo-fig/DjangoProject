from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('new/category', views.category_create, name='category_create'),
    path('edit/category/<int:pk>/', views.category_update, name='category_update'),
    path('delete/category/<int:pk>/', views.category_delete, name='category_delete'),
    #path('', views.item_list, name='item_list'),
    path('new/item', views.item_create, name='item_create'),
    path('edit/item/<int:pk>/', views.item_update, name='item_update'),
    path('delete/item/<int:pk>/', views.item_delete, name='item_delete'),

 ]
