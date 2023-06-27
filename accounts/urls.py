from django.urls import path
from .views import ProfileView, LoginView, LogoutView

app_name = 'accounts'
urlpatterns = [
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout")
]