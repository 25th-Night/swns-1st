from rest_framework import serializers
from users.models import User


class SignUpSeiralizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "fullname", "phone", "password")

    def create(self, validated_data):
        email = validated_data["email"]
        fullname = validated_data["fullname"]
        phone = validated_data["phone"]
        password = validated_data["password"]

        user = User.objects.create(email=email, fullname=fullname, phone=phone)
        user.set_password(password)
        user.save()

        return user
