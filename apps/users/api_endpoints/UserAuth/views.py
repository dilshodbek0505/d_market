from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView

from apps.users.api_endpoints.UserAuth.serializers import LoginOtpSerializer, ConfirmOtpSerializer, UserSerializer, RegisterOtpSerializer
from apps.users.api_endpoints.UserAuth.utils import generate_code
from apps.users.models import User

from django.core.cache import cache
from django.contrib.auth import authenticate


class LoginOtp(APIView):

    def post(self, request):
        serializer = LoginOtpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(request, username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        if not user:
            return Response({"data": "user not found"}, status=404)

        code = generate_code()
        print(code)

        if cache.get(f'otp_{user.phone_number}'):
            return Response({"data": "sms_already_sent"}, status=400)

        cache.set(f'otp_{user.phone_number}', code, 60 * 2)

        return Response({"data": "sms_sent", "phone_number": user.phone_number}, status=200)


class RegisterOtp(APIView):

    def post(self, request):
        serializer = RegisterOtpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if User.objects.filter(phone_number = serializer.validated_data["phone_number"], username=serializer.validated_data['username']).exists():
            return Response({"data": "user_already_exists"}, status=400)

        code = generate_code()
        print(code)

        if cache.get(f"otp_{serializer.validated_data['phone_number']}"):
            return Response({"data":"sms_already_sent"}, status=400)

        cache.set(f"otp_{serializer.validated_data['phone_number']}", code, 60 * 2)

        return Response({"data": "sms_sent"}, status=200)


class ConfirmOtp(APIView):

    def post(self, request):
        serializer = ConfirmOtpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        code_in_cache = cache.get(f'otp_{serializer.validated_data["phone_number"]}')

        if code_in_cache != serializer.validated_data["code"]:
            return Response({"data": "wrong_code"}, status=400)

        cache.delete(f'otp_{serializer.validated_data["phone_number"]}')

        return Response({"data": "ok"}, status=200)


class UserDetail(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class Register(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


__all__ = [
    "Register",
    "UserDetail",
    "LoginOtp",
    "RegisterOtp",
    "ConfirmOtp",
]