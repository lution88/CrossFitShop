from django.urls import path, include

from user.views import UserAPIView

urlpatterns = [
    path("", UserAPIView.as_view()),
]
