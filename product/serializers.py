from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from product.models import Product, Review, Comment, Category, Wish


class CategorySerializer(ModelSerializer):
    same_category_products = serializers.SerializerMethodField()

    def get_same_category_products(self, obj):
        product_list = []
        for product in obj.product_set.all():
            product_list.append(product.name)
        return {"카테고리가 같은 제품들": [product_list]}

    class Meta:
        model = Category
        fields = ["name", "same_category_products"]


class ProductSerializer(ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    get_category = serializers.ListField(required=False)

    class Meta:
        model = Product
        fields = ['name', 'content', 'price', 'size', 'pro_img', 'category', 'get_category']
        extra_kwargs = {
            'pro_img': {"required": False},
            'category': {"required": False}
        }

    def create(self, validated_data):
        category = int(validated_data.pop('get_category')[0])
        product = Product(**validated_data)
        product.save()
        product.category.add(category)
        product.save()

        return product

    def update(self, instance, validated_data):
        category = int(validated_data.pop('get_category')[0])

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        instance.category.clear()
        instance.category.add(category)
        instance.save()
        return instance


class CommentSerializer(ModelSerializer):
    def create(self, validated_data):
        comment = Comment(**validated_data)
        comment.user = self.context['user']
        comment.review = self.context['review']
        comment.save()
        return comment

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    class Meta:
        model = Comment
        fields = ["id", "user", "review", "content"]
        extra_kwargs = {
            'user' : {'required':False}
        }


class ReviewSerializer(ModelSerializer):
    comment_review = CommentSerializer(many=True, required=False)

    def create(self, validated_data):
        review = Review(**validated_data)
        review.user = self.context['user']
        review.product = self.context['product']
        review.save()
        return review

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    class Meta:
        model = Review
        fields = ["user", "product", "title", "content", "rate", "comment_review"]
        extra_kwargs = {
            'comment': {"required": False},
        }


class WishSerializer(ModelSerializer):
    class Meta:
        model = Wish
        fields = ["user", "product"]