from django.db import models
from master.utils.HF_DATETIME.get_curr_time import get_current_time
# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = self.updated_at = get_current_time()
        else:
            self.updated_at = get_current_time()
        super().save(*args, **kwargs)
