from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _



class Account(models.Model):

    user = models.ForeignKey("User", verbose_name=_("User"), on_delete=models.CASCADE, related_name='account')
    # name = models.CharField(_("Name"), max_length=100)
    avatar = models.ImageField(_("Avatar"), upload_to='uploads/avatars/', height_field=None, width_field=None, max_length=None) #alt = name
    bio = models.TextField(_("Bio"), null=True, blank=True)
    # password = models.CharField(_("Password hass"), max_length=250)
    # email = models.EmailField(_("Email"), max_length=254)
    birthdate = models.DateField(_("Birthdate"), auto_now=False, auto_now_add=False)

    @property
    def user_posts(self):
        ...
    
    def create_account():
        ...

    def follow(self, other):
        relation

    def archive(self):
        self.is_active = False
        self.save()

    def restore(self):
        self.is_active= True
        self.save()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return f'{self.name}'






