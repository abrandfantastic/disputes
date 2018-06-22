"""disputes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from about.sitemaps import aboutViewSitemap
from contacts.sitemaps import contactViewSitemap
from blog.sitemaps import blogViewSitemap
from faq.sitemaps import faqViewSitemap
from disputes.sitemaps import disputesViewSitemap
from expertise.sitemaps import expertiseViewSitemap

sitemaps = {
    'about': aboutViewSitemap,
    'blog': blogViewSitemap,
    'contact': contactViewSitemap,
    'disputes': disputesViewSitemap,
    'expertise': expertiseViewSitemap,
    'faq': faqViewSitemap,

}

from .import views

urlpatterns = [

    path('', include('about.urls')),
    path('', include('blog.urls')),
    path('', include('contacts.urls')),
    path('', include('expertise.urls')),
    path('', include('faq.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('success', views.success, name='success'),
]
