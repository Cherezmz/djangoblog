from django.shortcuts import render, redirect
from .models import Article  # , Comment

# Create your views here.


def articles_list(request):
    # articles = Article.object.all().order_by('date')
    return render(request, 'blogapp/articles_list.html')
    # , {'articles': articles})
