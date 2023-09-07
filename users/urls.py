from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import SignUpView

router = DefaultRouter()
# router.register("path명", ViewSet클래스, basename="basename지정")

urlpatterns = [
    path("", include(router.urls)),
    path("signup/", SignUpView.as_view(), name="signup"),
]
