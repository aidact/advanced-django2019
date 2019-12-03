from rest_framework import serializers

from auth_.models import MainUser, Profile
from auth_.token import get_token


# class UserSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField()
#     username = serializers.CharField(max_length=100)
#     password = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
#
#     def create(self, validated_data):
#         User.objects.create_user(self.validated_data['email'],
#                                  self.validated_data['username'],
#                                  self.validated_data['password'])

class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ('email', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        return MainUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)

    def validate(self, attrs):
        try:
            user = MainUser.objects.get(username=attrs['username'])
        except:
            raise serializers.ValidationError('User dooes not exist')
        if not user.check_password(attrs['password']):
            raise serializers.ValidationError('Useer does not exist')
        attrs['user'] = user
        return attrs

    def login(self):
        user = self.validated_data['user']
        token = get_token(user)
        return user, token


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

        read_only_fields = ('user', )

    def update(self, instance, validated_data):
        instance.bio = validated_data['bio']
        instance.address = validated_data['address']
        instance.user = self.context['request'].user

        instance.save()
        return instance
