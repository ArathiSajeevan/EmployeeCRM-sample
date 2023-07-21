# Generated by Django 4.2.3 on 2023-07-20 06:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_user', models.CharField(editable=False, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_user', models.CharField(blank=True, max_length=50, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('location_name', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='tbl_department',
            fields=[
                ('department_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_user', models.CharField(editable=False, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_user', models.CharField(blank=True, max_length=50, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('department_name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('designation_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_user', models.CharField(editable=False, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_user', models.CharField(blank=True, max_length=50, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('designation_name', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('department_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tbl_department')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
