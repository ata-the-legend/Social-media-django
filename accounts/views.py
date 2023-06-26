from django.shortcuts import render, get_object_or_404, redirect 
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View
from .forms import LoginForm

# Create your views here.

class ProfileView(View):
    def get(self, request, username):
        user = User.objects.get(username=username)
        account = get_object_or_404(Account, user=user)
        posts = account.user_posts
        context = {'account': account, "user": user, 'posts': posts}
        return render(request, 'accounts/account.html', context)

