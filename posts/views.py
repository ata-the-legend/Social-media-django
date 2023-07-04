from django.shortcuts import render, redirect
from django.views import View
from .forms import PostForm, MediaForm, HashtagForm
from .models import Post, Comment, Media, Hashtag
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class PostListView(View):

    def get(self, request):
        posts = Post.objects.all().order_by('-create_at')
        context = {'posts': posts}
        return render(request, 'posts/post_list.html', context)

class PostCreateView(View):
    template = 'posts/post_create.html'

    def get(self, request):
        form = PostForm(initial={'user_account': request.user.account.get()})
        media_form = MediaForm
        hashtag_form = HashtagForm
        return render(request, self.template, {'form': form, 'media_form': media_form, 'hashtag_form': hashtag_form})

    @method_decorator(login_required)
    def post(self, request):
        form = PostForm(request.POST)
        hashtag_form = HashtagForm(request.POST)
        media_form = MediaForm(request.POST, request.FILES)
        if form.is_valid() and hashtag_form.is_valid() and media_form.is_valid():
            cd = form.cleaned_data
            tag = hashtag_form.cleaned_data['tag']
            if tag:
                if not Hashtag.objects.filter(tag = tag).exists():
                    hashtag = Hashtag.objects.create(tag= tag)
                else:
                    hashtag = Hashtag.objects.get(tag = tag)
                post = Post.objects.create(user_account= cd['user_account'], description =cd['description'])
                hashtag.user_post.add(post)
            else:
                post = Post.objects.create(user_account= cd['user_account'], description =cd['description'])

            media_cd = media_form.cleaned_data
            Media.objects.create(user_media= media_cd['user_media'], is_default=media_cd['is_default'], user_post= post)

            return redirect('accounts:profile', cd['user_account'].user.username)
        return redirect('posts:new_post')
        

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