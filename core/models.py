from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class BaseModel(models.Model):

    class meta:
        abstract = True
    
    is_active = models.BooleanField(_("Is_Active"), default= True)

    def archive(self):
        self.is_active = False
        self.save()

    def restore(self):
        self.is_active= True
        self.save()
