from django.shortcuts import render, redirect
from django.views import View
from django.forms import forms
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

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
            post.unlike_post(account)
        return redirect('posts:post_list',)

class PostCommentView(LoginRequiredMixin ,View):

    def post(self, request, post_id, on):
        if on == 'post':
            user_post = Post.objects.get(id= post_id)
            user_account = request.user.account.get()
            Comment.objects.create(user_post= user_post, author= user_account, content=request.POST.get('comment_text'))
            messages.success(request, 'Comment registered succesfully.')
            return redirect('posts:post_list')
        elif on == 'reply':
            parent = Comment.objects.get(id= post_id)
            user_post = Post.objects.get(id= parent.user_post.id)
            user_account = request.user.account.get()
            Comment.objects.create(user_post= user_post, author= user_account, content=request.POST.get('comment_text'), parent=parent)
            messages.success(request, 'Comment registered succesfully.')
            return redirect('posts:post_list')
        else:
            return redirect('posts:post_list')