# Generated by Django 5.1.1 on 2024-10-06 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_device_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='code',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
