from rest_framework import serializers

from phonenumber_field.serializerfields import PhoneNumberField
from phonenumbers import parse, is_valid_number_for_region
from phonenumbers.phonenumberutil import NumberParseException

from django.contrib.auth import get_user_model

User = get_user_model()


def _validate_phone_number(phone_number):
    try:
        parsed_number = parse(str(phone_number), 'UZ')
        if not is_valid_number_for_region(parsed_number, 'UZ'):
            raise serializers.ValidationError("the phone number should belong only to the region of Uzbekistan")

    except NumberParseException:
        raise serializers.ValidationError("Invalid phone number")


class LoginSerializer(serializers.Serializer):
    phone_number = PhoneNumberField(required=True, region='UZ')
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        phone_number = str(attrs.get('phone_number'))
        _validate_phone_number(phone_number)
        return attrs


class LoginConfirmSerializer(serializers.Serializer):
    phone_number = PhoneNumberField(required=True, region='UZ')
    password = serializers.CharField(write_only=True, required=True)
    code = serializers.CharField(max_length=6, required=True)

    def validate(self, attrs):
        phone_number = str(attrs.get('phone_number'))
        _validate_phone_number(phone_number)
        return attrs


class RegisterSerializer(serializers.Serializer):
    phone_number = PhoneNumberField(required=True, region='UZ')

    def validate(self, attrs):
        phone_number = str(attrs.get('phone_number'))
        _validate_phone_number(phone_number)
        return attrs


class RegisterConfirmSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=6, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'phone_number', 'password', 'code', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'code': {'read_only': True}
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'phone_number', 'first_name', 'last_name', 'password', 'is_active')
        extra_kwargs = {
            'password': {'write_only': True, 'required': False}
        }

    @staticmethod
    def validate_phone_number(phone_number):
        _validate_phone_number(str(phone_number))
        return phone_number