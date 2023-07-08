from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Account, AccountRecycle
from django.contrib.auth.models import User
from posts.models import PostRecycle

# admin.site.unregister(User)
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'bio', 'birthdate']

@admin.register(AccountRecycle)
class AccountRecycleAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'bio', 'birthdate']
    actions = ['restore']

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return AccountRecycle.archived.filter(is_active= False)

    @admin.action(description='Restore Archived Accounts')
    def restore(self, request, queryset):
        for account in queryset:
            account.user.is_active = True
            account.user.save()
            PostRecycle.archived.filter(user_account= account).update(is_active= True)
        queryset.update(is_active=True)
