from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class expertiseViewSitemap(Sitemap):

    def items(self):
        return ['expertise']

    def location(self, item):
        return reverse(item)