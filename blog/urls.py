# contact/urls.py
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('blog/', views.blogListView.as_view(), name='blog'),
    
]
