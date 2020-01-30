from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log the user in (will do later)
            return redirect('articles: list')
# "articles is the name of the app from blogapp/urls
# list is the name of path. I suppose that the error is connected with not rendering article (means no endpoint to show)
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm()
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {'form': form})
