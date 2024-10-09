from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm

from blog_app.models import User
from .forms import CustomUserCreationForm
from django.contrib.auth import logout as auth_logout

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('post_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('post_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('login')


def profile(request):
    user = request.user
    following_users = user.following.all()
    followers = user.followers.all()

    return render(request, 'accounts/profile.html', {
    'user': user,
    'following_users': following_users,
    'followers': followers,
})