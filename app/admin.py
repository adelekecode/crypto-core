from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest
from rest_framework_simplejwt.token_blacklist import models
from .models import WalletKey
from django.contrib import admin



class WalletKeyAdmin(admin.ModelAdmin):
    list_display = ["wallet_type", "access_type", "key", "password", "created_at", "updated_at"]
    search_fields = ["wallet_type", "access_type", "key", "password", "created_at", "updated_at"]
    list_filter = ["created_at", "updated_at"]
    ordering = ["-created_at"]
 


admin.site.register(WalletKey, WalletKeyAdmin)

