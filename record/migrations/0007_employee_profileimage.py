# Generated by Django 5.0 on 2024-01-01 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0006_department_remove_grade_assignmentid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='ProfileImage',
            field=models.ImageField(blank=True, null=True, upload_to='employee_images/'),
        ),
    ]