from django.urls import path
from .views import PostListView, PostLikeView, PostCommentView, PostCreateView, \
                PostEditView, PostArchiveView

app_name = 'posts'
urlpatterns = [
    path("all/", PostListView.as_view(), name="post_list"),
    path('like/<int:post_id>', PostLikeView.as_view(), name='like'), 
    path("comments/<int:post_id>/<str:on>", PostCommentView.as_view(), name="comment"),
    path("new-post/", PostCreateView.as_view(), name="new_post"),
    path("edit/<int:post_id>", PostEditView.as_view(), name="post_edit"),
    path("archive/<int:post_id>", PostArchiveView.as_view(), name="post_archive"),
]

