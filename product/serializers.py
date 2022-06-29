from rest_framework.serializers import ModelSerializer

from product.models import Product, Review, Comment, Category, Wish


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','content','price','size','pro_img']
