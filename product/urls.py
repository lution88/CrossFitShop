from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from product.views import ProductView, ReviewApiView, ReviewDetailApiView, ReviewPostView, CommentApiView

urlpatterns = [
    path('list/', ProductView.as_view()),
    path('list/<int:product_id>/', ProductView.as_view()),

    path('review/', ReviewApiView.as_view()),
    path('review/<int:product_id>/', ReviewPostView.as_view()),

    path('review/detail/<int:review_id>/', ReviewDetailApiView.as_view()),
    path('review/detail/<int:review_id>/comment/', CommentApiView.as_view()),
    path('review/detail/<int:review_id>/comment/<int:comment_id>/', CommentApiView.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
