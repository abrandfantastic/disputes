from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class aboutViewSitemap(Sitemap):
    changfreq = 'always'


    def items(self):
        return ['about']

    def location(self, item):
        return reverse(item)

