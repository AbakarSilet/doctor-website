from django.contrib.sitemaps import Sitemap
from .models import Article
from django.utils.translation import activate
from django.urls import reverse

class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    i18n = True
    languages = ['fr', 'en', 'ar']

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.date_modification



class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    i18n = True  # génère une entrée par langue automatiquement
    languages = ['fr', 'en', 'ar']
    alternates = True

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