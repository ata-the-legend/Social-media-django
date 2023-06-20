from django.contrib import admin
from .models import Account
from django.contrib.auth.models import User

# admin.site.unregister(User)
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'bio', 'birthdate']
