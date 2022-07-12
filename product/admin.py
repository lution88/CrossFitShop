from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Product, Review, Comment, Category, Wish


# Register your models here.
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'size')


class CommentInline(admin.StackedInline):
    model = Comment


class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ('id','title','rate','user','product')
    list_display_links = ('title', )
    inlines = (
        CommentInline,
    )


admin.site.register(Product, ProductModelAdmin)
admin.site.register(Review, ReviewModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
# admin.site.register(Comment)
admin.site.register(Wish)