from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class blogViewSitemap(Sitemap):

    def items(self):
        return ['blog']

    def location(self, item):
        return reverse(item)