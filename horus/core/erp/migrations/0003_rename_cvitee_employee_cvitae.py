# Generated by Django 5.0.3 on 2024-03-08 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_type_employee_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='cvitee',
            new_name='cvitae',
        ),
    ]
