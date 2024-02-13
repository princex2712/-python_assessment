# Generated by Django 5.0.1 on 2024-02-13 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_usermodel_doctor_specialty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='doctor_specialty',
            field=models.CharField(blank=True, default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='photo',
            field=models.ImageField(blank=True, default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
