from django.shortcuts import render
from .models import News_post, Article

def home(request):
    news = News_post.objects.all()
    articles = Article.objects.all()
    return render(request, 'news/news.html', {'news': news, 'articles': articles})

