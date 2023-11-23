from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('APIApp.urls')),
    path('', include('CartApp.urls')),
    path('', include('CatalogApp.urls')),
    path('', include('UserAccountApp.urls')),
]
