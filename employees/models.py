import uuid
from django.db import models

from master.models import tbl_department, Location, Designation

# Create your models here.

class Employee(models.Model):
    employee_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_user = models.CharField(max_length=50, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_user = models.CharField(max_length=50, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    employee_no = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    status = models.CharField(max_length=50, null=True, blank=True, choices=STATUS_CHOICES)
    skills = models.CharField(max_length=50, null=True, blank=True)
    join_date = models.DateField(null=True, blank=True)
    emp_start_date = models.DateField(null=True, blank=True)
    emp_end_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    department_name = models.ForeignKey(tbl_department, on_delete=models.SET_NULL, null=True, blank=True)
    location_name = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    designation_name = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.name)
    

