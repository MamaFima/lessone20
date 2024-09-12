from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Это первая страница моего домашнего задания на Django!</h1>")

def test(request):
    return HttpResponse("<h1>Это вторая страница моего домашнего задания на Django!</h1>")
# Create your views here.
