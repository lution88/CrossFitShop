from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Product, Review, Comment, Category, Wish


# Register your models here.
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size')


admin.site.register(Product, ProductModelAdmin)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Wish)