from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns


# URLs non traduites → exclues de la traduction
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('accounts/', include('accounts.urls')), 
]

# URLs traduites → préfixées par /fr/ /en-us/ /ar/
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),     
    path('', include('blog.urls')),       
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)