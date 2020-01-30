from django.shortcuts import render, redirect
from .models import Article  # , Comment

# Create your views here.


def articles_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'blogapp/articles_list.html', {'articles': articles})

    # def article_create(request):
    #     return render(request, "blogapp/article_create.html")
