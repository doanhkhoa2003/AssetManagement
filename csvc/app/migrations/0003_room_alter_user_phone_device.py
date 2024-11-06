# Generated by Django 5.1.1 on 2024-10-06 08:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_user_phone_alter_user_sex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.BooleanField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('bought_date', models.DateField()),
                ('status', models.BooleanField(null=True)),
                ('condition', models.CharField(max_length=50, null=True)),
                ('price', models.IntegerField(null=True)),
                ('cate_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.category')),
            ],
        ),
    ]