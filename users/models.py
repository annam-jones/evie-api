from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=50)  
    username = models.CharField(max_length=150, unique=True)
    bio = models.TextField(default="", blank=True)  

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['username']  

    def __str__(self):
        return self.email
