from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext as _



class Post(BaseModel):

    title = models.CharField(_("Title"), max_length=100)
    description = models.TextField(_("Description"))
    user_id = models.ForeignKey("user.User", verbose_name=_("User ID"), on_delete=models.CASCADE, related_name='posts')
    # is_liked = models.BooleanField(_("Is liked"), default=False)
    
    def is_liked_by_user(self, user):
        return self.like_set.filter(user_id = user).exists()

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title



class Comments(BaseModel):

    post_id = models.ForeignKey("Post", verbose_name=_("Post ID"), on_delete=models.CASCADE)
    author = models.ForeignKey("user.User", verbose_name=_("Author"), on_delete=models.CASCADE)
    content = models.TextField(_("Comment"))
    parent = models.ForeignKey("self", verbose_name=_("Parent"), on_delete=models.CASCADE, null=True, blank=True)
    

    class Meta:
        verbose_name = _("Comments")
        verbose_name_plural = _("Commentss")

    def __str__(self):
        return self.content



class Media(BaseModel):

    media = models.FileField(_("Media"), upload_to='uploads/medias/')
    alt = models.CharField(_("Alter"), max_length=100)
    is_default = models.BooleanField(_("Is Default"), default=False)
    post_id = models.ForeignKey("Post", verbose_name=_("Post"), on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Media")

    def __str__(self):
        return self.alt




class Like(BaseModel):

    user_id = models.ForeignKey("user.User", verbose_name=_("User"), on_delete=models.DO_NOTHING)
    post_id = models.ForeignKey("Post", verbose_name=_("Post"), on_delete=models.CASCADE)
    is_like = models.BooleanField(_("like/dislike"))

    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")

    def __str__(self):
        return self.name



class Hashtag(BaseModel):

    tag = models.SlugField(_("Hashtag"), unique=True)
    post_id = models.ManyToManyField("Post", verbose_name=_("Post"), on_delete=models.CASCADE, related_name='tags')

    class Meta:
        verbose_name = _("Hashtag")
        verbose_name_plural = _("Hashtags")

    def __str__(self):
        return self.name



