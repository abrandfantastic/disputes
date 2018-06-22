from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class faqViewSitemap(Sitemap):

    def items(self):
        return ['faq']

    def location(self, item):
        return reverse(item)