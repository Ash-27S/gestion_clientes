from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('create/', views.customer_create, name='customer_create'),
    path('update/<int:id>/', views.customer_update, name='customer_update'),
    path('delete/<int:id>/', views.customer_delete, name='customer_delete'),

    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/update/<int:id>/', views.order_update, name='order_update'),
    path('orders/delete/<int:id>/', views.order_delete, name='order_delete'),
    
    path('customer/<int:id>/orders/', views.customer_orders, name='customer_orders'),
]
