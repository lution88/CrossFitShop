from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import UserSerializer

from user.models import User


class UserAPIView(APIView):
    def get(self, request):
        user = UserSerializer(User.objects.all(), many=True).data
        return Response(user, status=status.HTTP_200_OK)
