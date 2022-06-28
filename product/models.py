from django.db import models

# Create your models here.
from user.models import User


class Product(models.Model):
    name = models.CharField("제품이름", max_length=50)
    content = models.TextField("제품설명")
    price = models.IntegerField("제품가격")
    size = models.CharField("제품size", max_length=200)
    pro_img = models.ImageField("제품이미지", upload_to='images/', blank=True)
    category = models.ManyToManyField('Category', verbose_name="카테고리")

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE, related_name="review_user")
    product = models.ForeignKey(Product, verbose_name="제품이름", on_delete=models.CASCADE, related_name="review_product")
    title = models.CharField("리뷰 제목", max_length=50)
    content = models.TextField("리뷰 내용")
    rate = models.IntegerField("제품 평점")
    comment = models.ForeignKey('Comment', verbose_name="댓글", on_delete=models.CASCADE, related_name="review_comment")

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.CharField("코멘트", max_length=250)
    user = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE, related_name="comment_user")

    def __str__(self):
        return f'{self.user}: {self.content[:15]}'


class Category(models.Model):
    name = models.CharField("카테고리", max_length=50)

    def __str__(self):
        return self.name


class Wish(models.Model):
    user = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE, related_name="wish_user")
    product = models.ForeignKey(Product, verbose_name="제품", on_delete=models.CASCADE, related_name="wish_product")
