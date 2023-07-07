from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Post, Media, Hashtag, PostRecycle


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

@admin.register(PostRecycle)
class PostRecycleAdmin(admin.ModelAdmin):
    inlines = [
        HashtagInline,
        MediaInline,
    ]
    list_display = ['id', 'description', 'user_account']

    actions= ['restore']

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return PostRecycle.archived.filter(is_active= False)
    
    @admin.action(description='Restore Archived Item')
    def restore(self, request, queryset):
        queryset.update(is_active= True)


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    pass
