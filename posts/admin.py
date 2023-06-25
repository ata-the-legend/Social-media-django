from django.contrib import admin
from .models import Post, Media


class MediaInline(admin.TabularInline):
    model = Media
    fk_name = 'user_post'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        MediaInline,
    ]


