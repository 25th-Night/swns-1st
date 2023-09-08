from django_filters import rest_framework as filters

from users.models import User, Profile


class UserFilter(filters.FilterSet):
    email = filters.CharFilter(field_name="email", lookup_expr="icontains")
    fullname = filters.CharFilter(field_name="fullname", lookup_expr="icontains")
    phone = filters.CharFilter(field_name="phone", lookup_expr="icontains")
    is_active = filters.BooleanFilter(field_name="is_public", lookup_expr="exact")

    class Meta:
        model = User
        fields = ["email", "fullname", "phone", "is_active"]


class ProfileFilter(filters.FilterSet):
    nickname = filters.CharFilter(field_name="nickname", lookup_expr="icontains")
    is_active = filters.BooleanFilter(field_name="is_public", lookup_expr="exact")

    class Meta:
        model = Profile
        fields = ["nickname", "is_active"]
