from django.shortcuts import render, redirect
from django.views import View
from django.forms import forms
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListView(View):

    def get(self, request):
        posts = Post.objects.all().order_by('-create_at')
        context = {'posts': posts}
        return render(request, 'posts/post_list.html', context)


class PostLikeView(LoginRequiredMixin ,View):

    def get(self, request, post_id):
        post = Post.objects.get(id = post_id)
        account = request.user.account.get()
        if not post.is_liked_by_user(account):
            post.like_post(account)
        else:
            pass #unlike
        return redirect('posts:post_list',)
