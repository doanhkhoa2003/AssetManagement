# Generated by Django 5.1.1 on 2024-10-06 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_device_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(blank=True, choices=[('Nam', 'Nam'), ('Nữ', 'Nữ')], max_length=3, null=True),
        ),
    ]
