from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from blog import views as blog_views
from blog.sitemaps import ArticleSitemap, StaticSitemap

sitemaps = {
    'articles': ArticleSitemap,
    'static': StaticSitemap,
}
# URLs non traduites → exclues de la traduction
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('accounts/', include('accounts.urls')), 
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', blog_views.robots_txt, name='robots_txt')
]

# URLs traduites → préfixées par /fr/ /en-us/ /ar/
urlpatterns += i18n_patterns(
    path('gestion_articles/', admin.site.urls),     
    path('', include('blog.urls')),   
        
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)