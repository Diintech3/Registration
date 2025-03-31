from django.contrib import admin
from .models import *

# Register your models here.

# @admin.sites.registr(signup)
    
@admin.register(signup)
class myadmin(admin.ModelAdmin):
    list_display=["first_name","last_name","Password","Mobile", "Email"]