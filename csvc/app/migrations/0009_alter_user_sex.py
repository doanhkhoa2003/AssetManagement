# Generated by Django 5.1.1 on 2024-10-06 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_user_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('Nam', 'Nam'), ('Nữ', 'Nữ')], max_length=3, null=True),
        ),
    ]