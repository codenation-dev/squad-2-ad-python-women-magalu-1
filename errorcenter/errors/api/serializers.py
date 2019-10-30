from rest_framework import serializers

from ..models import User, Error


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')


class ErrorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Error
        fields = '__all__'
