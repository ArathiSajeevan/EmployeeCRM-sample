# Generated by Django 4.2.3 on 2023-07-15 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='join_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
