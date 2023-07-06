from django.db import models

# Create your models here.
import uuid

class department_model(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
