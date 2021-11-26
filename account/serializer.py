from rest_framework import  serializers
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password')
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],     password = validated_data['password'] )
        return user
    
class UpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    repassword = serializers.CharField(write_only=True, required=True)
    
    def validate(self, attrs):
        if attrs['password'] != attrs['repassword']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs
    class Meta:
        model = User
        fields = ('id','username','password','repassword')
        extra_kwargs = {
            'password':{'write_only': True},
            'repassword':{'write_only': True}
        }
    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()
        
        return instance
# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'