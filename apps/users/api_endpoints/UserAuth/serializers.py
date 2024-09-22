from rest_framework import serializers

import re

from apps.users.models import User


class LoginOtpSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128)
    password = serializers.CharField(max_length=128, write_only=True)


class RegisterOtpSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13)
    username = serializers.CharField(max_length=128)
    password = serializers.CharField(max_length=128, write_only=True)


    def validate_phone_number(self, value):
        pattern = r"[0-9]{9}"

        if not re.match(pattern, value):
            raise serializers.ValidationError("The phone number is incorrect")

        return value


class ConfirmOtpSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13)
    code = serializers.CharField(max_length=6)

    def validate_phone_number(self, value):
        pattern = r"[0-9]{9}"

        if not re.match(pattern, value):
            raise serializers.ValidationError("The phone number is incorrect")

        return value


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "full_name", "username", "phone_number", "avatar", "coins", "is_deleted", "password")

    def validate_phone_number(self, value):
        pattern = r"[0-9]{9}"

        if not re.match(pattern, value):
            raise serializers.ValidationError("The phone number is incorrect")

        return value
