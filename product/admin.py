from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Product, Review, Comment, Category, Wish


# Register your models here.
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'size')


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Product, ProductModelAdmin)
admin.site.register(Review)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Comment)
admin.site.register(Wish)