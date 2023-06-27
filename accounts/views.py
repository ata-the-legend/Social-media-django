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
                messages.error(request, 'username or password is wrong', 'danger')
            
        return render(request, self.template, {'form':form})