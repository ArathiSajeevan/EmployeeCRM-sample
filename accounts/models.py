from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    CHOICES = (
        ('Admin', 'Admin'),
        ('Viewer', 'Viewer'),

    )
    user_type = models.CharField(max_length=20, choices=CHOICES, null=True, blank=True)
    phone = models.CharField(max_length=20,blank=True, null=True)
    username = models.CharField(unique=True ,max_length=20, blank=True, null=True)
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


    def __str__(self):
        if self.first_name and self.last_name:
            return str(self.first_name)+ " " + str(self.last_name)
        else:
            return str(self.first_name)
    