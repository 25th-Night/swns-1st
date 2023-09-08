from rest_framework import serializers
from users.models import User, Profile


class SignUpSeiralizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "fullname",
            "phone",
            "password",
            "created_at",
        )

    def create(self, validated_data):
        email = validated_data["email"]
        fullname = validated_data["fullname"]
        phone = validated_data["phone"]
        password = validated_data["password"]

        user = User.objects.create(email=email, fullname=fullname, phone=phone)
        user.set_password(password)
        user.save()

        return user


class LoginSeiralizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "fullname", "phone")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("groups", "user_permissions")
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = (
            "email",
            "is_admin",
            "following",
            "created_at",
            "updated_at",
        )

    def update(self, instance, validated_data):
        if "password" in validated_data:
            new_password = validated_data.pop("password")
            instance.set_password(new_password)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = (
            "created_at",
            "updated_at",
        )
