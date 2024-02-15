# Generated by Django 5.0.1 on 2024-02-15 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_usermodel_doctor_specialty_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentmodel',
            name='doctor_id',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointmentmodel',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]