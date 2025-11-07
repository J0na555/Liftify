from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.exceptions import AuthenticationFailed


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'full_name', 'profile_image', 'gender', 'birth_date', 'weight', 'goal', 'height', 'last_login', 'created_at', 'updated_at']
        read_only_fields = ['id', 'last_login', 'created_at', 'updated_at']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'full_name', 'profile_image', 'gender', 'birth_date', 'weight', 'goal', 'height', 'last_login', 'created_at', 'updated_at']
        read_only_fields = ['id', 'last_login', 'created_at', 'updated_at']

    def create(self, validated_data):
        # remove password from validated_data then hash and save
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.password = make_password(password)
        user.save()
        return user

    # generate jwt token after registering
    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)

        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'id': str(instance.id),
            'username': instance.username,
            'gender': instance.gender,
            'weight': instance.weight,
            'height': instance.height,
            'goal': instance.goal
        }
        return data


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = User.objects.filter(username=username).first()
        if not user:
            user = User.objects.filter(email=username).first()

        if not user:
            raise AuthenticationFailed('No active account found with the given credentials')

        if not check_password(password, user.password):
            # Fallback for existing users who may have been stored with plain text passwords:
            # if stored password equals provided password, accept it and migrate to a hashed password.
            if user.password == password:
                # re-hash and save
                user.password = make_password(password)
                user.save()
            else:
                raise AuthenticationFailed('No active account found with the given credentials')

        # attach user so view can use it
        attrs['user'] = user
        return attrs

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
