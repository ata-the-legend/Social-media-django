from django.urls import path
from .views import UserFollowView

app_name = 'relations'
urlpatterns = [
    path("user-follow/<str:username>/", UserFollowView.as_view(), name="user_follow")
]

