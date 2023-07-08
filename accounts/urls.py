from django.urls import path
from .views import ProfileView, LoginView, LogoutView, RegisterView, \
    EditProfileView, AccountArchiveView

app_name = 'accounts'
urlpatterns = [
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("edit-profile/", EditProfileView.as_view(), name="edit_profile"),
    path("<slug:username>/archive", AccountArchiveView.as_view(), name="account_archive")
]