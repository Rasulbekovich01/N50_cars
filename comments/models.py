from django.db import models

# Create your models here.

class CommentModel(models.Model):
    comment = models.TextField()
    client = models.ForeignKey(UserModel, on_delete=CASCADE)
    status =models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

class Meta:
    base_name_plural = 'comment'
    base_name = 'comment'

def __str__(self):
    return self.comment