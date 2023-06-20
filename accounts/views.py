from django.shortcuts import render, get_object_or_404 
from .models import Account
from django.contrib.auth.models import User

# Create your views here.


def profile_view(request, username):
    user = User.objects.get(username=username)
    print(user)
    account = get_object_or_404(Account, user=user)
    context = {'account': account, "user": user}
    return render(request, 'accounts/account.html', context)