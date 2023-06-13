from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class BaseModel(models.Model):

    class meta:
        abstract = True
        
    is_active = models.BooleanField(_("Is_Active"), default= True)
    create_at = models.DateTimeField(_("Create Date"), auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(_("Update Date"), auto_now=True, auto_now_add=False)

    def archive(self):
        self.is_active = False
        self.save()

    def restore(self):
        self.is_active= True
        self.save()
