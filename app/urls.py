from django.urls import path
from . import views

urlpatterns = [
    # Categorias
    path('category/', views.category_list, name='category_list'),
    path('new/category/', views.category_create, name='category_create'),
    path('edit/category/<int:pk>/', views.category_update, name='category_update'),
    path('delete/category/<int:pk>/', views.category_delete, name='category_delete'),

    # Itens
    path('items/', views.item_list, name='item_list'),
    path('new/item/', views.item_create, name='item_create'),
    path('edit/item/<int:pk>/', views.item_update, name='item_update'),
    path('delete/item/<int:pk>/', views.item_delete, name='item_delete'),

    # Autores
    path('authors/', views.author_list, name='author_list'),
    path('new/authors/', views.author_create, name='author_create'),
    path('edit/authors/<int:pk>/', views.author_update, name='author_update'),
    path('delete/authors/<int:pk>/', views.author_delete, name='author_delete'),

    # Editoras
    path('publishers/', views.publisher_list, name='publisher_list'),
    path('new/publishers/', views.publisher_create, name='publisher_create'),
    path('edit/publishers/<int:pk>/', views.publisher_update, name='publisher_update'),
    path('delete/publishers/<int:pk>/', views.publisher_delete, name='publisher_delete'),
]
