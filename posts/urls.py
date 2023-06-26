from django.urls import path
from .views import PostListView, PostLikeView

app_name = 'posts'
urlpatterns = [
    path("all/", PostListView.as_view(), name="post_list"),
    path('like/<int:post_id>', PostLikeView.as_view(), name='like'), 
]

