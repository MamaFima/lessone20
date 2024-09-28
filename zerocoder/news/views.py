from django.shortcuts import render, redirect
from .models import News_post, Article
from .forms import News_postForm
from django.contrib.auth.models import User


def home(request):
    news = News_post.objects.all()
    articles = Article.objects.all()
    return render(request, 'news/news.html', {'news': news, 'articles': articles})


def news_add(request):
    error = ''
    if request.method == 'POST':
        form = News_postForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            if request.user.is_authenticated:
                # Если пользователь авторизован, присваиваем его
                news.user = request.user
            else:
                # Если нет авторизации, можно пропустить присвоение пользователя
                news.user = None
            news.save()
            return redirect('news_home')
        else:
            error = "Данные некорректны"

    form = News_postForm()
    return render(request, 'news/add_new_post.html', {'form': form, 'error': error})


