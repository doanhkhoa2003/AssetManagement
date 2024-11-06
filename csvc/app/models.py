from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import RESTRICT


class User(AbstractUser):
    phone = models.CharField(max_length=10, null=True, blank=True)
    GENDER_CHOICES = [
        ('Nam', 'Nam'),
        ('Nữ', 'Nữ'),
    ]
    sex = models.CharField(max_length=3, choices=GENDER_CHOICES, null=True)

    def save(self, *args, **kwargs):
        # Nếu có mật khẩu mới, hãy băm mật khẩu
        if self.pk is None or self.password != self._state.fields_cache.get('password'):
            self.set_password(self.password)  # Băm mật khẩu

        super().save(*args, **kwargs)  # Gọi phương thức save() của lớp cha

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=50, null=False)
    STATUS_CHOICES = [
        ('Trống', 'Trống'),
        ('Không trống', 'Không trống'),
    ]
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, null=True)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=50, null=False)
    code = models.CharField(max_length=10, null=True, unique=True)
    description = models.TextField(null=True, blank=True)
    bought_date = models.DateField()
    STATUS_CHOICES = [
        ('Đang sử dụng', 'Đang sử dụng'),
        ('Chưa sử dụng', 'Chưa sử dụng'),
        ('Hư', 'Hư'),
        ('Đang bảo trì', 'Đang bảo trì'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True)
    CONDITION_CHOICES = [
        ('Tốt', 'Tốt'),
        ('Hư', 'Hư'),
    ]
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, null=True)
    price = models.IntegerField(null=True)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Statistic(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(User, on_delete=RESTRICT)


class Maintenance(models.Model):
    maintenance_date = models.DateField()
    STATUS_AFTER_CHOICES = [
        ('Bình thường', 'Bình thường'),
        ('Chập chờn', 'Chập chờn'),
        ('Hư', 'Hư'),
    ]
    status_after = models.CharField(max_length=20, choices=STATUS_AFTER_CHOICES, null=True)
    note = models.TextField()
    device = models.ForeignKey(Device, on_delete=RESTRICT)


class Report(models.Model):
    description = models.TextField()
    date = models.DateField()
    device = models.ForeignKey(Device, on_delete=RESTRICT)
