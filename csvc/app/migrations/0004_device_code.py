# Generated by Django 5.1.1 on 2024-10-06 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_room_alter_user_phone_device'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='code',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
