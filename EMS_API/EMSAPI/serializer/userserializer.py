from rest_framework import serializers
from EMSAPI.model.employeemodels import*
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from rest_framework.validators import UniqueValidator
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name', 'username', 'email', 'password')
class create_user_serializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','first_name','last_name', 'username', 'email', 'password')
        extra_kwargs = {'password': {'required': True}}
        error_messages={'user_name':'username already exist'}
        
                       
        email=serializers.EmailField()
        username=serializers.CharField()
    def validate(self,data):
        email=data.get('email')
        username=data.get('username')
        if User.objects.filter(email=email).exists():
            
            raise serializers.ValidationError({'msg':"email already exist"})
        elif User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'msg':self.error_messages['user_name']})
        
        return data
    def create(self,validated_data):
        user=User.objects.create_user(first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'],
                                        username=validated_data['username'],
                                        email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
class login_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'username','password')
        extra_kwargs = {'password': {'required': True}
         }