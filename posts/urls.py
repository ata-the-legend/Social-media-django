from django.urls import path
from .views import PostListView

app_name = 'posts'
urlpatterns = [
    path("all/", PostListView.as_view(), name="post_list")
]

