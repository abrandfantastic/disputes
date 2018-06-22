from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class contactViewSitemap(Sitemap):

    def items(self):
        return ['contact']

    def location(self, item):
        return reverse(item)