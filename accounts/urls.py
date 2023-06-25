from django.urls import path
from .views import profile_view

app_name = 'accounts'
urlpatterns = [
    path('<str:username>/', profile_view, name='profile'),
]