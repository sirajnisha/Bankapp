from django.contrib import admin

from .models import District, User, Branch
# Register your models here.

admin.site.register(District)
admin.site.register(User)
admin.site.register(Branch)