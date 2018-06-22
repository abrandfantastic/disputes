from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='post_detail'),
]