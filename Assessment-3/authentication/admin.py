from django.contrib import admin
from .models import UserModel,AppointmentModel
# Register your models here.

admin.site.register(UserModel)
admin.site.register(AppointmentModel)
