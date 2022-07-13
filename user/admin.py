from django.contrib import admin
from .models import User
# Register your models here.


class UserAmin(admin.ModelAdmin):
    list_display = ('id','username','fullname','email','phone')


admin.site.register(User, UserAmin)