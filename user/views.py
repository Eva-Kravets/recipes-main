from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import User
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed, ValidationError, NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_201_CREATED
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['POST'], detail=False, url_path='register')
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        password = serializer.validated_data['password']
        if len(password) < 8:
            raise ValidationError({'password': ['Password is too short']})

        serializer.save()

        return Response({'message': 'success'}, status=HTTP_201_CREATED)

    @action(methods=['POST'], detail=False, url_path='login')
    def login(self, request):
        if 'email' not in request.data:
            data = {'email': ['Email must be provided']}
            if 'password' not in request.data:
                data['password'] = ['Password must be provided']
            raise ValidationError(data)
        if 'password' not in request.data:
            raise ValidationError({'password': ['Password must be provided']})

        try:
            user = User.objects.get(email=request.data.get('email'))
        except User.DoesNotExist:
            raise NotFound({'message': 'User with provided credentials does not exist'})

        if not user.is_active:
            raise AuthenticationFailed({'message': 'Email is not confirmed'})

        if not user.check_password(request.data.get('password')):
            raise AuthenticationFailed({'message': 'Incorrect password'})

        refresh = RefreshToken.for_user(user)
        update_last_login(None, user)
        response = Response()
        response.set_cookie('refresh', str(refresh))
        response.data = {'access': str(refresh.access_token)}
        return response

    @action(methods=['GET'], detail=False,
            url_path='user')
    def user(self, request):
        user = request.user
        data = UserSerializer(user).data
        return Response(data)