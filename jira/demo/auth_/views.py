from django.core.exceptions import ValidationError
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_.models import MainUser, Profile
from auth_.serializers import MainUserSerializer, LoginSerializer, ProfileSerializer
from auth_.token import get_token


class MainUserViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = MainUser.objects.all()
    http_method_names = ['post', 'get', 'delete']
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'login':
            return LoginSerializer
        return MainUserSerializer

    @action(methods=['GET'], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.login()
        return Response({'user': MainUserSerializer(user).data,
                         'token': token})


class ProfileViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return self.queryset.all()


class MainUserAPIView(APIView):

    def signup(self, request):
        serializer = MainUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def login(self, request):
        email = request.query_params.get('email')
        password = request.query_params.get('password')
        if email is None or password is None:
            raise ValidationError('Please enter credentials')
        try:
            user = MainUser.objects.get(email=email)
            if not user.check_password(password):
                raise ValidationError('Email or password incorrect')
        except MainUser.DoesNotExist:
            raise ValidationError('Email or password incorrect')
        token = get_token(user)
        return Response({'token': token})

    def get_profile(self, request):
        profile = Profile.objects.get(user_id=request.user.id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def update_profile(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)