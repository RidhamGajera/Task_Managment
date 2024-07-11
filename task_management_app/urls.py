from django.urls import path, include  # Add 'include' import for including other app URLs
from django.contrib import admin  # Add 'admin' import for Django admin site

from . import views  # Import views from your app

urlpatterns = [
    path('', views.home, name='home'),  # Adjust 'home' to your view function
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),  # Include your app's URLs here
]
