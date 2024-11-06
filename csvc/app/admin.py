from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'sex', 'phone', 'email', 'username', 'password', 'is_superuser', 'is_staff', 'is_active', 'last_login']
    search_fields = ['username']
    list_filter = ['is_staff']


class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status']
    search_fields = ['name']
    list_filter = ['status']


class DeviceAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'description', 'bought_date', 'condition', 'price']
    search_fields = ['code', 'name']


admin.site.site_header = "Quản lý cơ sở vật chất Admin"
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Device, DeviceAdmin)