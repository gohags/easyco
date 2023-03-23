from django.contrib import admin
from .models import Account
from django.apps import apps

# Register your models here.
admin.site.register(Account)