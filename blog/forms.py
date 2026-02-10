from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu', 'image', 'video']

    def clean(self):
        cleaned_data = super().clean()
        image = cleaned_data.get('image')
        video = cleaned_data.get('video')

        if image and video:
            raise forms.ValidationError(_('Un article ne peut pas contenir à la fois une image et une vidéo'))

        return cleaned_data

