from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import SignUpView

router = DefaultRouter()
# router.register("path명", ViewSet클래스, basename="basename지정")

urlpatterns = [
    path("", include(router.urls)),
    path("/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
