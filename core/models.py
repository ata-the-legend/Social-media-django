from django.db import models
from django.utils.translation import gettext as _
# from uuid import uuid4
# Create your models here.


class SoftQuerySet(models.QuerySet):
    def archive(self):
        return self.update(is_active= False)
    
class SoftManager(models.Manager):
    def get_queryset(self):
        return SoftQuerySet(self.model, self._db).filter(is_active = True)



class BaseModel(models.Model):

    objects = SoftManager()
    class meta:
        abstract = True
        
    # id = models.UUIDField(editable=False, primary_key=True, default=uuid4)
    is_active = models.BooleanField(_("Is_Active"), default= True, editable=False)
    create_at = models.DateTimeField(_("Create Date"), auto_now=False, auto_now_add=True) # do with mixin
    update_at = models.DateTimeField(_("Update Date"), auto_now=True, auto_now_add=False) # with mixin

    def archive(self):
        self.is_active = False
        self.save()

    def restore(self):
        self.is_active= True
        self.save()


# class RecycleModel(BaseModel):
#     class Meta:
#         proxy = True