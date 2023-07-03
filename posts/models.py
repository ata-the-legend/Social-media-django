from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext as _



class Post(BaseModel):

    # title = models.CharField(_("Title"), max_length=100)
    description = models.TextField(_("Description"))
    user_account = models.ForeignKey("accounts.Account", 
                                     verbose_name=_("User ID"), 
                                     on_delete=models.CASCADE, 
                                     related_name='posts'
                                     )
    # is_liked = models.BooleanField(_("Is liked"), default=False)
    
    def is_any_like(self):
        return self.like_set.all().exists()

    def is_liked_by_user(self, account):
        return self.like_set.filter(user_account = account).exists()
    
    def like_post(self, account):
        if not self.is_liked_by_user(account):
            return Like.objects.create(user_account= account ,user_post= self ,is_like=True)
        
    def unlike_post(self, account):
        if self.is_liked_by_user(account):
            return Like.objects.get(user_account= account ,user_post= self ).delete()

    def post_likes(self):
        return self.like_set.all().count()

    def post_media(self):
        return self.media_set.all()

    def post_comments(self):
        return self.comment_set.all()
    
    def post_hashtags(self):
        return self.tags.all()

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.description



class Comment(BaseModel):

    user_post = models.ForeignKey("Post", 
                                  verbose_name=_("Post ID"), 
                                  on_delete=models.CASCADE
                                  )
    author = models.ForeignKey("accounts.Account", 
                               verbose_name=_("Author"), 
                               on_delete=models.CASCADE
                               )
    content = models.TextField(_("Comment"))
    parent = models.ForeignKey("self", 
                               verbose_name=_("Parent"), 
                               on_delete=models.CASCADE, 
                               null=True, 
                               blank=True
                               )
    

    class Meta:
        verbose_name = _("Comments")
        verbose_name_plural = _("Commentss")

    def __str__(self):
        return self.author.user.username



class Media(BaseModel):

    user_media = models.FileField(_("Media"), 
                                  upload_to='uploads/medias/'
                                  )
    alt = models.CharField(_("Alter"), 
                           max_length=100, 
                           default='not found'
                           )
    is_default = models.BooleanField(_("Is Default"), 
                                     default=False
                                     )
    user_post = models.ForeignKey("Post", 
                                  verbose_name=_("Post"), 
                                  on_delete=models.CASCADE
                                  )
    

    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Media")

    def __str__(self):
        return self.alt




class Like(BaseModel):

    user_account = models.ForeignKey("accounts.Account", 
                                     verbose_name=_("User"), 
                                     on_delete=models.DO_NOTHING)
    user_post = models.ForeignKey("Post", 
                                  verbose_name=_("Post"), 
                                  on_delete=models.CASCADE
                                  )
    is_like = models.BooleanField(_("like/dislike"), default=True)

    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")

    def __str__(self):
        return f"{self.user_account.user.username} liked {self.user_post.user_account.user.username}'s post"



class Hashtag(BaseModel):

    tag = models.SlugField(_("Hashtag"))
    user_post = models.ManyToManyField("Post", 
                                       verbose_name=_("Post"), 
                                       related_name='tags'
                                       )

    @classmethod
    def hashtag_posts(cls, tag: str):
        hashtag = cls.objects.get(tag = tag)
        return hashtag.user_post.all()

    class Meta:
        verbose_name = _("Hashtag")
        verbose_name_plural = _("Hashtags")

    def __str__(self):
        return self.tag




