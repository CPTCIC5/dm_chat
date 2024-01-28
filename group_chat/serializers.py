from rest_framework import serializers
from .models import UserModel

class CreateUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model=UserModel
        fields = ('username','email','password','confirm_password')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        print('xyz',validated_data)
        return UserModel.objects.create_user(**validated_data)
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id','username','email','is_online','is_active','is_staff','is_superuser']
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()