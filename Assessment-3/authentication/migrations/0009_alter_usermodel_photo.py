# Generated by Django 5.0.1 on 2024-02-15 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_rename_doctor_specialty_usermodel_doctor_speciality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='photo',
            field=models.ImageField(blank=True, upload_to='user_photos/'),
        ),
    ]
