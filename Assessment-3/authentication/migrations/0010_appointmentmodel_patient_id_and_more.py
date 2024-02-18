# Generated by Django 5.0.1 on 2024-02-18 02:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_alter_usermodel_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentmodel',
            name='patient_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authentication.usermodel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointmentmodel',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('pending', 'Pending'), ('completed', 'Completed')], default='active', max_length=20),
        ),
    ]