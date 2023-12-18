from django.contrib import admin
from django.urls import path,include
from .views import FileUpload


urlpatterns = [
    
    path('upload/',FileUpload.as_view(),name='upload'),
]