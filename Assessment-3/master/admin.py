from django.contrib import admin
from django.contrib.auth.models import Group, User

# Register your models here.
admin.site.unregister(Group)
admin.site.unregister(User)