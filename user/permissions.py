from rest_framework import permissions


# 판매자
class SellerCanWrite(permissions.BasePermission):
    """
    판매자는 상품 등록, 수정, 삭제 가능
    """
    SAFE_METHOD = ("POST", "PUT", "DELETE")

    def has_permission(self, request, view):
        if request.method in ["GET"]:
            return True
        return request.user.is_seller

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_seller


# # 구매자
# class CustomerCanReadOnly(permissions.BasePermission):
#     """
#     구매자는 상품 구경만 가능
#     """
#
#     def has_permission(self, request, view):
#         if request.method == "GET" and not request.user.is_seller:
#             return True
#         return False
#
#     def has_object_permission(self, request, view, obj):
#         if request.method == "GET" and not request.user.is_seller:
#             return True
#         return False
