from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class todoApiModel(BaseModel):
    task = models.CharField(null=False,max_length=255)
    description = models.TextField()
    