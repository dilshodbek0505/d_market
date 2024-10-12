from rest_framework.generics import GenericAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.user.api_endpoints.Auth.serializers import LoginSerializer, \
    LoginConfirmSerializer, RegisterSerializer, RegisterConfirmSerializer, UserSerializer
from apps.user.utils import generate_code

from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password
from django.core.cache import cache

User = get_user_model()


class UserLoginApi(GenericAPIView):
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data['phone_number']
        password = serializer.validated_data['password']
        print(phone_number, password)

        try:
            user = User.objects.get(phone_number=phone_number)
            if not user.check_password(password):
                return Response('password did not match', status=400)
        except User.DoesNotExist:
            return Response('user not found')

        phone_number = user.phone_number.national_number

        if cache.get(f'otp_{phone_number}'):
            return Response({'sms already sent'}, status=400)

        code = generate_code()
        cache.set(f'otp_{phone_number}', code, timeout=60 * 2)

        print(code)

        return Response({'success'}, status=200)


class UserLoginConfirmApi(GenericAPIView):
    serializer_class = LoginConfirmSerializer
    queryset = User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        code = serializer.validated_data['code']
        user = authenticate(self.request, phone_number=serializer.validated_data['phone_number'], password=serializer.validated_data['password'])


        if user and cache.get(f'otp_{user.phone_number.national_number}'):
            confirm_code = cache.get(f'otp_{user.phone_number.national_number}')

            if code != confirm_code:
                return Response({'code did not match'}, status=400)

            cache.delete(f'otp_{user.phone_number.national_number}')

            return Response({'success'}, status=200)

        return Response({'user not found'}, status=404)


class RegisterApi(GenericAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data['phone_number']

        try:
            user = User.objects.get(phone_number=phone_number)
            return Response({'user already exists'}, status=400)
        except User.DoesNotExist:
            code = generate_code()

            if cache.get(f'otp_{phone_number}'):
                return Response({'sms already sent'}, status=400)

            cache.set(f'otp_{phone_number}', code, timeout=60 * 2)

            print(code)

        return Response({'success'}, status=200)


class RegisterConfirmApi(CreateAPIView):
    serializer_class = RegisterConfirmSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        code = serializer.validated_data['code']
        user = serializer.save()
        confirm_code = cache.get(f'otp_{user.phone_number.national_number}')

        if code != confirm_code:
            return Response({'code did not match'}, status=400)

        cache.delete(f'otp_{user.phone_number.national_number}')

        data = {
            'id': user.id,
            'token': user.token
        }

        return Response(data, status=201)


class UserDetailsApi(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class RefreshTokenApi(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(self.request.user.token, status=200)


__all__ = [
    'UserLoginConfirmApi',
    'RegisterConfirmApi',
    'RegisterApi',
    'UserLoginApi',
    'RefreshTokenApi',
    'UserDetailsApi',
]