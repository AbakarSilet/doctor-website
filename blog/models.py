from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.text import slugify
from django.core.exceptions import ValidationError
import os
from ckeditor.fields import RichTextField


def validate_image_size(value):
    if value.size > 10 * 1024 * 1024:
        raise ValidationError(_('La taille de l\'image ne doit pas dépasser 10MB'))


def validate_video_size(value):
    if value.size > 20 * 1024 * 1024:
        raise ValidationError(_('La taille de la vidéo ne doit pas dépasser 20MB'))


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    valid_video_extensions = ['.mp4', '.mov', '.avi']
    if ext.lower() not in valid_image_extensions + valid_video_extensions:
        raise ValidationError(_('Format de fichier non supporté'))


class Article(models.Model):
    titre = models.CharField(max_length=500)
    contenu = RichTextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, max_length=500)
    vues = models.PositiveIntegerField(default=0)
    image = models.ImageField(
        upload_to='articles/images/',
        null=True,
        blank=True,
        validators=[validate_image_size, validate_file_extension]
    )
    video = models.FileField(
        upload_to='articles/videos/',
        null=True,
        blank=True,
        validators=[validate_video_size, validate_file_extension]
    )

    def clean(self):
        if self.image and self.video:
            raise ValidationError(_('Un article ne peut pas contenir à la fois une image et une vidéo'))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        self.clean()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def total_likes(self):
        return self.likes.count()

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ['-date_creation']

    def __str__(self):
        return self.titre


class ArticleView(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name= _("views")
    )
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('article', 'ip_address')
    

class ContactMessage(models.Model):
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    sujet = models.CharField(max_length=255)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _("Message de contact")
        verbose_name_plural = _("Messages de contact")

    def __str__(self):
        return f"{self.nom} - {self.sujet}"
