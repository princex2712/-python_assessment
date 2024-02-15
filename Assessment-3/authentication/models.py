from django.db import models

# Create your models here.
from master.models import BaseModel
from master.utils.HF_GENERATE.generate_password import generate_password

# Create your models here.
class UserModel(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,unique=True)
    contact = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    doctor_specialty = models.CharField(max_length=255,blank=True)
    role = models.CharField(max_length=50,default="patient")
    otp = models.CharField(max_length=50,default="457783")
    photo = models.ImageField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
       if not self.password:
            self.password = generate_password(8)
       super(UserModel,self).save(*args, **kwargs)

class AppointmentModel(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    doctor_id = models.CharField(max_length=255)
    gender_options = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    gender = models.CharField(max_length=20,choices=gender_options)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
