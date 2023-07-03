from django.shortcuts import render, redirect
from django import urls
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Account
from django.contrib.auth.models import User
from accounts.views import ProfileView
# Create your views here.


class UserFollowView(LoginRequiredMixin ,View):

    def get(self, request, username):
        user = User.objects.get(username=username)
        followee = Account.objects.get(user= user)
        follower = Account.objects.get(user = request.user)
        if not follower.is_followed(followee):
            follower.follow(followee)
        else:
            follower.unfollow(followee)
        return redirect(urls.reverse('accounts:profile', args=[username]))
        # return render(request, request.META.get('HTTP_REFERER'))
