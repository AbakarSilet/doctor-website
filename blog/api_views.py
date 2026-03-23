from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import F

from .models import Article, ArticleView
from .serializers import ArticleListSerializer, ArticleDetailSerializer
from .utils import get_client_ip


class ArticleListAPI(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer

    def get_serializer_context(self):
        return {"request": self.request} 


class ArticleDetailAPI(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'slug'

    def get_serializer_context(self):
        return {"request": self.request}

    def retrieve(self, request, *args, **kwargs):
        article = get_object_or_404(Article, slug=kwargs['slug'])
        ip = get_client_ip(request)

        if ip:
            if not ArticleView.objects.filter(
                article=article,
                ip_address=ip
            ).exists():
                ArticleView.objects.create(
                    article=article,
                    ip_address=ip
                )
                Article.objects.filter(id=article.id).update(
                    vues=F('vues') + 1
                )

        serializer = self.get_serializer(article)
        return Response(serializer.data)
