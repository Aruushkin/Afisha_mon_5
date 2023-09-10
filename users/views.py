import random
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import UserCreateSerializer
from .models import UserProfile  # Предполагается, что у вас есть модель UserProfile

class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.create_user(username=username, password=password, is_active=False)
        verification_code = ''.join(random.choice('0123456789') for _ in range(6))
        user_profile = UserProfile.objects.create(user=user, verification_code=verification_code)
        message = {"message": "ok",
                   "verification_code": verification_code}
        return Response(status=status.HTTP_201_CREATED,
                        data={'message': message, 'user_id': user.id})

class AuthorizationAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            return Response(data={'key': token.key})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED,
                            data={'message': 'User credentials not correct'})

class ConfirmUserAPIView(APIView):
    def post(self, request):
        verification_code = request.data.get('verification_code')
        username = request.data.get('username')

        try:
            user_profile = UserProfile.objects.get(user__username=username, verification_code=verification_code)
        except UserProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Verification code not found'})

        user = user_profile.user
        user.is_active = True
        user.save()

        return Response(status=status.HTTP_200_OK, data={'message': 'User confirmed'})
