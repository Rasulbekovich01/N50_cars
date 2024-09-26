from django.db import models

# Create your models here.

class UserModel(models.Model):
    username = models.CharField(max_length=55)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    password = models.CharField(max_length=55)
    email = models.EmailField(unique=True)
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        base_name = 'user'
        base_name_plural= 'user'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'