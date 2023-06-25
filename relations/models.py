from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext as _


class UserFollow(BaseModel):

    follower = models.ForeignKey("accounts.Account", verbose_name=_("Follower"), on_delete=models.CASCADE, related_name='followers')
    followee = models.ForeignKey("accounts.Account", verbose_name=_("Followee"), on_delete=models.CASCADE, related_name='followees')

    class Meta:
        verbose_name = _("UserFollow")
        verbose_name_plural = _("UserFollows")

    def __str__(self):
        return self.name

class HashtagFollow(models.Model):

    follower = models.ManyToManyField("accounts.Account", verbose_name=_("Follower"), related_name='tag_followers')
    tag = models.ManyToManyField("posts.Hashtag", verbose_name=_("Hashtag"), related_name='followed_tags')

    def tag_followers(tag):
        ...

    def followed_tags(account):
        ...

    class Meta:
        verbose_name = _("HashtagFollow")
        verbose_name_plural = _("HashtagFollows")

    def __str__(self):
        return self.name





