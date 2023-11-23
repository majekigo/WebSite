from django.urls import path
from APIApp import views

urlpatterns = [
    path('api/', views.api),
    path('api/create/<int:product_id>', views.create, name='api_create'),
    path('api/delete/<int:product_id>', views.delete, name='api_create'),
    path('api/read/<int:product_id>', views.read, name='api_read'),
    path('api/update/<int:product_id>', views.update, name='api_update'),
]