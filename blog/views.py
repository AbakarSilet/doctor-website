from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models import F  
from django.db import transaction



from .utils import get_client_ip
from accounts.models import User
from .forms import ArticleForm
from .models import Article, ArticleView, ContactMessage


def is_admin(user):
    return user.groups.filter(name='Admin').exists()


# Décorateur pour vérifier si l'utilisateur est admin
def admin_required(view_func):
    decorated_view = user_passes_test(is_admin, login_url='403')(view_func)
    return decorated_view


def custom_404(request):
    return render(request, '404.html', status=404)


def custom_403(request):
    return render(request, '403.html', status=403)


@login_required
@admin_required
def transition_page(request):
    # Récupérer les statistiques
    nombre_articles = Article.objects.count()
    nombre_utilisateurs = User.objects.count()
    dernier_article = Article.objects.order_by('-date_creation').first()

    context = {
        'nombre_articles': nombre_articles,
        'nombre_utilisateurs': nombre_utilisateurs,
        "dernier_article": dernier_article,
    }
    return render(request, 'transition.html', context)


def home(request):
    articles = Article.objects.all()[:5]  # Affiche les 5 derniers articles
    return render(request, 'index.html',{'articles': articles})


def about(request):
    return render(request, 'about.html')


def portfolio(request):
    return render(request, 'work.html')


def contact(request):
    return render(request, 'contact.html')



def send_email(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            nom=request.POST.get('nom'),
            email=request.POST.get('email'),
            sujet=request.POST.get('sujet'),
            message=request.POST.get('message'),
        )

        messages.success(
            request,
            _("Votre message a bien été envoyé. Nous vous répondrons bientôt 🙏")
        )
        return redirect('home')

    return render(request, 'contact.html')



def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/articles_list.html', {'articles': articles})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    
    ip = get_client_ip(request)

    if ip:
        with transaction.atomic():
            vue_creee, created = ArticleView.objects.get_or_create(
                article=article,
                ip_address=ip
            )

            if created:
                Article.objects.filter(id=article.id).update(
                    vues=F('vues') + 1
                )
                article.refresh_from_db()

    if request.LANGUAGE_CODE != "fr":
        return redirect(f"/fr/article/{slug}/")
    
    return render(request, 'blog/article_detail.html', {
        'article': article,
    })


@admin_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                article = form.save(commit=False)
                article.save()
                messages.success(request, _('Article créé avec succès!'))
                return redirect('article_detail', slug=article.slug)
            except ValidationError as e:
                messages.error(request, str(e))
                return render(request, 'blog/article_form.html', {'form': form})
    else:
        form = ArticleForm()
    return render(request, 'blog/article_form.html', {'form': form})


@admin_required
def article_update(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            try:
                article = form.save()
                messages.success(request, _('Article mis à jour avec succès!'))
                return redirect('article_detail', slug=article.slug)
            except ValidationError as e:
                messages.error(request, str(e))
                return render(request, 'blog/article_form.html', {'form': form})
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/article_form.html', {'form': form})


@admin_required
def article_delete(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        article.delete()
        messages.success(request, _('Article supprimé avec succès!'))
        return redirect('article_list')
    return render(request, 'blog/article_confirm_delete.html', {'article': article})

