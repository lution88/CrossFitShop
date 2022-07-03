from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from product.models import Product, Review, Comment, Category, Wish


class WishSerializer(ModelSerializer):
    class Meta:
        model = Wish
        fields = ["user", "product"]


class CategorySerializer(ModelSerializer):
    same_category_products = serializers.SerializerMethodField()
    def get_same_products(self, obj):
        product_list = []
        return {"카테고리가 같은 제품들": [product_list]}

    class Meta:
        model = Category
        fields = ["name", "product_list"]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content", ]


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ["title", "content", "rate"]


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','content','price','size','pro_img']
        extra_kwargs = {
            'pro_img': {"required":False},
            'category': {"required":False}
        }

    def create(self, validated_data):
        product = Product(
            name=validated_data['name'],
            content=validated_data['content'],
            price=validated_data['price'],
            size=validated_data['size'],
        )
        product.save()

        return product