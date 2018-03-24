from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'full_name', 'email', 'role', 'role_name')


class AuthTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key',)


class UserSerializer(serializers.ModelSerializer):
    auth_token = AuthTokenSerializer(many=False, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name',
                  'patronymic', 'email', 'auth_token', 'full_name',
                  'role', 'role_name')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        generated_password = User.objects.make_random_password()
        user_data.update({'password': generated_password})

        user = User.objects.create(**user_data)
        user.set_password(generated_password)
        user.save()

        return user


class TokenSerializer(serializers.ModelSerializer):
    user = UserTokenSerializer(many=False, read_only=True)

    class Meta:
        model = Token
        fields = ('key', 'user')
