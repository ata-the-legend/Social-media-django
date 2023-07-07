from django.contrib import admin
from .models import Post, Media, Hashtag


class MediaInline(admin.TabularInline):
    model = Media
    fk_name = 'user_post'

class HashtagInline(admin.TabularInline):
    model = Hashtag.user_post.through
    # m2m_name = 'user_post'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        HashtagInline,
        MediaInline,
    ]
    list_display = ['id', 'description', 'user_account']

@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    pass
