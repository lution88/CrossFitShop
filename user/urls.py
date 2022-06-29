from django.urls import path, include

from user.views import UserAPIView

urlpatterns = [
    path("sign-up/", UserAPIView.as_view()),
]
