# Generated by Django 5.0.1 on 2024-02-18 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_appointmentmodel_patient_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentmodel',
            name='notes',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
