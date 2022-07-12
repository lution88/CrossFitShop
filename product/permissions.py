from rest_framework.permissions import BasePermission

# class YouCanReadOnly(BasePermission):
#     """
#     구매자는 조회만 가능
#     """
#     SAFE_METHOD = ['GET',]
#     message = "접근 권한이 없습니다."
#
#     def has_permission(self, request, view):
#         user = request.user
#         if request.method in self.SAFE_METHOD and user.is_seller == "False":
#