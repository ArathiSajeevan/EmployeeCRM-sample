from django.db import models

# Create your models here.
import uuid

class tbl_department(models.Model):
    department_id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    created_user = models.CharField(max_length=50, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_user = models.CharField(max_length=50, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    department_name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)


    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.department_name
    

class Designation(models.Model):
    designation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_user = models.CharField(max_length=50, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_user = models.CharField(max_length=50, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    department_name = models.ForeignKey(tbl_department, on_delete=models.CASCADE, null=True, blank=True)
    designation_name = models.CharField(max_length=50, null=True, blank=True, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.designation_name
    

class Location(models.Model):
    location_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_user = models.CharField(max_length=50, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_user = models.CharField(max_length=50, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    location_name = models.CharField(max_length=50, null=True, blank=True, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.location_name
    