from django.shortcuts import render, get_object_or_404, redirect 
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from .forms import LoginForm, RegisrerForm
from .models import Account
from django.db import IntegrityError
# Create your views here.

class ProfileView(View):
    def get(self, request, username):
        user = User.objects.get(username=username)
        account = get_object_or_404(Account, user=user)
        posts = account.user_posts
        followed = request.user.account.get().is_followed(account)
        context = {'account': account, "user": user, 'posts': posts, 'followed': followed}
        return render(request, 'accounts/account.html', context)

class LoginView(View):
    template = 'accounts/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password= cd['password'])
            if user is not None:
                login(request ,user)
                messages.success(request, f"{cd['username']} logged in", 'success')
                return redirect('posts:post_list')
            else:
                messages.error(request, 'username or password is wrong', 'warning')
            
        return render(request, self.template, {'form':form})
    
class LogoutView(View):
    
    def get(self, request):
        logout(request)
        messages.success(request, "logged out", 'success')
        return redirect('posts:post_list')
    
class RegisterView(View):

    form_class = RegisrerForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/register.html', {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                account = Account.create_account(
                    username=cd['username'], 
                    password = cd['password'], 
                    first_name=cd['first_name'], 
                    last_name=cd['last_name'], 
                    bio=cd['bio'],
                    birthdate=cd['birthdate'], 
                    avatar=cd['avatar']
                )
            except IntegrityError:
                messages.error(request, 'this username was taken', 'warning')
                user = None
            else:
                user = account.user
            if user is not None:
                login(request ,user)
                messages.success(request, f"{cd['username']} regesterd successfully", 'success')
                return redirect('accounts:profile', cd['username'])
            else:
                messages.error(request, 'this error', 'warning')
            
        return render(request, 'accounts/register.html', {'form':form})