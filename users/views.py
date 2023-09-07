from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.request import Request

from django_filters import rest_framework as filters

from users.models import User
from users.permissions import CustomReadOnly
from users.serializers import SignUpSeiralizer, LoginSeiralizer, UserSerializer


class SignUpView(APIView):
    serializer_class = SignUpSeiralizer
    permission_classes = [AllowAny]

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)

            return Response(
                {
                    "user": serializer.data,
                    "message": "register successs",
                    "token": {"access": access_token, "refresh": refresh_token},
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    serializer_class = LoginSeiralizer
    permission_classes = [AllowAny]

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)

        if user is not None:
            serializer = self.serializer_class(user)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)

            return Response(
                {
                    "user": serializer.data,
                    "message": "login successs",
                    "token": {"access": access_token, "refresh": refresh_token},
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": "login failed"}, status=status.HTTP_401_UNAUTHORIZED
        )


class UserFilter(filters.FilterSet):
    email = filters.CharFilter(field_name="email", lookup_expr="icontains")
    fullname = filters.CharFilter(field_name="fullname", lookup_expr="icontains")
    phone = filters.CharFilter(field_name="phone", lookup_expr="icontains")

    class Meta:
        model = User
        fields = ["email", "fullname", "phone", "is_active"]


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [CustomReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter

    def list(self, request: Request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request: Request, *args, **kwargs):
        return Response(
            data={"message": "Create operation is not supported"},
            status=status.HTTP_404_NOT_FOUND,
        )
