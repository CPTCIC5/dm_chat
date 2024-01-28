from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    is_online= models.BooleanField(default=False)

    def __str__(self):
        return self.username
    

class Message(models.Model):
    author = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    text = models.CharField(max_length=169)
    msged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['id']