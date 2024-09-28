from . models import News_post, Article
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class News_postForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название новости'
            }),
            "short_description": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое описание новости'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст новости'
            }),
        }
