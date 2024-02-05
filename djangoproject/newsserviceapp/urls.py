from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import *


router = SimpleRouter()
router.register(r'news', NewsViewset, basename='news')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/comment/', CommentAPIView.as_view(), name='comment'),
    path('api/v1/comment/<int:pk>/', CommentDetailAPIView.as_view(), name='comment_detail'),
    path('api/v1/like/', LikeAPIView.as_view(), name='like'),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]