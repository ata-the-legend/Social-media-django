from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from relations.models import UserFollow


class Account(models.Model):

    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE, related_name='account')
    # name = models.CharField(_("Name"), max_length=100)
    avatar = models.ImageField(_("Avatar"), upload_to='uploads/avatars/') #alt = name
    bio = models.TextField(_("Bio"), null=True, blank=True)
    # password = models.CharField(_("Password hass"), max_length=250)
    # email = models.EmailField(_("Email"), max_length=254)
    birthdate = models.DateField(_("Birthdate"))

    @property
    def user_posts(self):
        return self.posts.all()
    
    @classmethod
    def create_account(cls, username, password, avatar, bio, birthdate, **kwargs):
        user = User.objects.create(username= username, password= password, **kwargs)
        return cls.objects.create(user= user, avatar= avatar, bio= bio, birthdate= birthdate)

    def user_followers(self):
        return self.followers.all()
    
    def user_followees(self):
        return self.followees.all()

    def is_followed(self, other):
        return UserFollow.objects.filter(follower= self, followee= other).exists()

    def follow(self, other):
        if not self.is_followed(other):
            UserFollow.objects.create(follower= self, followee= other)

    def archive(self):
        self.is_active = False
        self.save()

    def restore(self):
        self.is_active= True
        self.save()

    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")

    def __str__(self):
        return f'{self.user.username}'






