from django.db import models

# Create your models here.

class ServiceModel(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

class Meta:
    base_name_plural = 'service'
    base_name = 'service'

def __str__(self):
    return self.service