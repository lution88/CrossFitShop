from django.db import models

# Create your models here.
from user.models import User


class Product(models.Model):
    name = models.CharField("제품이름", max_length=50)
    content = models.TextField("제품설명")
    price = models.IntegerField("제품가격")
    size = models.CharField("제품size", max_length=200)
    pro_img = models.ImageField("제품이미지",upload_to='images/', blank=True)
    # category = models.ManyToManyField()


class Review(models.Model):
    user = models.ForeignKey(User, verbose_name="고객명", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="제품먕", on_delete=models.CASCADE)
    title = models.CharField("리뷰 제목", max_length=50)
    content = models.TextField("리뷰 내용")
    rate = models.IntegerField("제품 평점")