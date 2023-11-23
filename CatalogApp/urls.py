from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog2/', views.catalog2, name='catalog2'),
    path('product_withdrawal/', views.product_withdrawal, name='product_withdrawal'),
    path('feedback/', views.feedback, name='feedback'),

]
