from django.contrib.sitemaps import Sitemap
from .models import Article
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.date_modification
    


class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return [
            'home',
            'contact_us',
            'portfolio',
            'about_us',
            'privacy_policy',
        ]

    def location(self, item):
        return reverse(item)