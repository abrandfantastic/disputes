from django.urls import path

from . import views

urlpatterns = [
    path('expertise/', views.expertise, name='expertise'),

]