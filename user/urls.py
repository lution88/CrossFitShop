from django.urls import path, include

from user.views import UserApiView, UserLoginApiView

urlpatterns = [
    path("", UserApiView.as_view()),
    # path("", UserApiView.as_view()),
    # path("sign-up/", UserSignUpApiView.as_view()),
    path("login/", UserLoginApiView.as_view()),
]
