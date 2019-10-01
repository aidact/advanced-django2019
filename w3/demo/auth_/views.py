from auth_.models import User
from auth_.serializers import UserSerializer
from auth_.token import get_token
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.create()
    return Response(serializer.data)


@api_view(['GET'])
def login(request):
    email = request.query_params.get('email')
    password = request.query_params.get('password')
    if email is None or password is None:
        raise ValidationError('Please enter credentials')
    try:
        user = User.objects.get(email=email)
        if not user.check_password(password):
            raise ValidationError('Email or password incorrect')
    except User.DoesNotExist:
        raise ValidationError('Email or password incorrect')
    token = get_token(user)
    return Response({'token': token})
