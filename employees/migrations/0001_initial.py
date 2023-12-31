# Generated by Django 4.2.3 on 2023-07-21 05:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_user', models.CharField(editable=False, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_user', models.CharField(blank=True, max_length=50, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('employee_no', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=50, null=True)),
                ('skills', models.CharField(blank=True, max_length=50, null=True)),
                ('join_date', models.DateField(blank=True, null=True)),
                ('emp_start_date', models.DateField(blank=True, null=True)),
                ('emp_end_date', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('department_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.tbl_department')),
                ('designation_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.designation')),
                ('emp_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_customuser', to=settings.AUTH_USER_MODEL)),
                ('location_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.location')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
