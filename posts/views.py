from django.shortcuts import render
from django.views import View
from django.forms import forms
from .models import Post



class PostListView(View):

    def get(self, request):
        posts = Post.objects.all().order_by('-create_at')
        context = {'posts': posts}
        return render(request, 'posts/post_list.html', context)




