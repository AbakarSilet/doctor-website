from django.contrib import admin
from .models import Article , ContactMessage



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_creation')
    prepopulated_fields = {'slug': ('titre',)}


admin.site.register(Article, ArticleAdmin)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'sujet', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('nom', 'email', 'sujet')