from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from product.views import ProductView

urlpatterns = [
    path('', ProductView.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)