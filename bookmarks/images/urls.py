from django.urls import path
from . import views

app_name = 'images'  # Add this line

urlpatterns = [
    # Define your URL patterns here, e.g.,
    path('', views.image_list, name='image_list'),
    path('create/', views.image_create, name='create'),
]