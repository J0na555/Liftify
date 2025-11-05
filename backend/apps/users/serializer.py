from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'fullname', 'profile_image', 'gender', 'birth_date', 'weight', 'goal', 'height', 'goal', 'last_login', 'created_at', 'updated_at']
        read_only_fields = ['id', 'last_login', 'created_at', 'updated_at']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model=User
        fields = ['id', 'username', 'email', 'password', 'full_name', 'profile_image', 'gender', 'birth_date', 'weight', 'goal', 'height', 'goal', 'last_login', 'created_at', 'updated_at']
        read_only_fields = ['id', 'last_login', 'created_at', 'updated_at']

        def create(self, validated_data):
            user = User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password'],
                full_name=validated_data['full_name'],
                profile_image=validated_data['profile_image'],
                gender=validated_data['gender'],
                birth_date=validated_data['birth_date'],
                weight=validated_data['weight'],
                height=validated_data['height'],
                goal=validated_data['goal'],
            )
            return user
        
        # generate jwt token after registering
        def to_representation(self, instance):
            refresh = RefreshToken.for_user(instance)

            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'id': instance.id,
                'username': instance.username,
                'gender': instance.gender,
                'weight': instance.weight,
                'height': instance.height,
                'goal': instance.goal
            }
            return data
