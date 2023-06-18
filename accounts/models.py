from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext as _



class Account(BaseModel):

    name = models.CharField(_("Name"), max_length=100)
    avatar = models.ImageField(_("Avatar"), upload_to='uploads/avatars/', height_field=None, width_field=None, max_length=None) #alt = name
    bio = models.TextField(_("Bio"))
    password = models.CharField(_("Password hass"), max_length=250)
    email = models.EmailField(_("Email"), max_length=254)
    birthdate = models.DateField(_("Birthdate"), auto_now=False, auto_now_add=False)

    @property
    def user_posts(self):
        ...
    
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return f'{self.name}'






