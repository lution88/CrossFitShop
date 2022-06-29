from rest_framework.serializers import ModelSerializer

from product.models import Product, Review, Comment, Category, Wish


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
        return product