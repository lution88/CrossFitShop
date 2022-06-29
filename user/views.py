from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import UserSerializer

from user.models import User


class UserApiView(APIView):
    def get(self, request):
        user = UserSerializer(User.objects.all(), many=True).data
        return Response(user, status=status.HTTP_200_OK)

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        user = request.user
        print(user)
        if user.is_anonymous:
            return Response({"error": "로그인 후 이용하세요"}, status=status.HTTP_400_BAD_REQUEST)

        user_serializer = UserSerializer(user, data=request.data, partial=True)
        if user_serializer.is_valid():
            return Response({"message": "정상 수정 되었습니다"}, status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginApiView(APIView):
    def post(self, request):
        username = request.data.get('username', '')
        print(username)
        password = request.data.get('password', '')
        print(password)

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "로그인 실패"}, status=status.HTTP_400_BAD_REQUEST)
        login(request, user)
        return Response({"message": "로그인 성공"}, status=status.HTTP_200_OK)