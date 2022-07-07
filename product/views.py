from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product, Category, Review
from product.serializers import ProductSerializer, ReviewSerializer


class ProductView(APIView):
    def get(self, request):
        product = ProductSerializer(Product.objects.all(), many=True).data
        return Response(product, status=status.HTTP_200_OK)

    def post(self, request):
        product_serializer = ProductSerializer(data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, product_id):
        product = Product.objects.get(id=product_id)
        product_serializer = ProductSerializer(product, data=request.data, partial=True)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id):
        product = Product.objects.get(id=product_id)
        product.delete()
        return Response({"message":"삭제 완료!!"})


class ReviewApiView(APIView):
    def get(self, request):
        reviews = ReviewSerializer(Review.objects.all(), many=True).data
        return Response(reviews, status=status.HTTP_200_OK)


class ReviewPostView(APIView):
    def post(self, request, product_id):
        user = request.user
        product = Product.objects.get(id=product_id)
        reviews_serializer = ReviewSerializer(data=request.data, context={'user': user, 'product': product})
        if reviews_serializer.is_valid():
            reviews_serializer.save()
            return Response(reviews_serializer.data, status=status.HTTP_200_OK)
        return Response(reviews_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetailApiView(APIView):
    def get(self, request, review_id):
        reviews = ReviewSerializer(Review.objects.get(id=review_id)).data
        return Response(reviews, status=status.HTTP_200_OK)

    def put(self, request, review_id):
        product = Review.objects.get(id=review_id)
        reviews_serializer = ReviewSerializer(product, data=request.data, partial=True)
        if reviews_serializer.is_valid():
            reviews_serializer.save()
            return Response(reviews_serializer.data, status=status.HTTP_200_OK)
        return Response(reviews_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, review_id):
        review = Review.objects.get(id=review_id)
        review.delete()
        return Response({"message": "삭제가 완료되었습니다."})
