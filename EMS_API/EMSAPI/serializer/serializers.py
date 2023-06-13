from rest_framework import serializers
from EMSAPI.model.employeemodels import*
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from rest_framework.validators import UniqueValidator
class Employeedataserializer(serializers.ModelSerializer):

    class Meta:
        model = Employeedata
        fields= '__all__' 
class attendanceserializer(serializers.ModelSerializer):

    class Meta:
        model = Employeedata
        fields= '__all__' 

class Employee_role_serializer(serializers.ModelSerializer):
    class Meta:
        model=Employee_role
        fields='__all__'
class salary_type_serializer(serializers.ModelSerializer):

    class Meta:
        model = salary_type
        fields= '__all__' 
class employees_type_serializer(serializers.ModelSerializer):

    class Meta:
        model = employees_type
        fields= '__all__' 

class log_entrys_api_serializer(serializers.ModelSerializer):
    class Meta:
        model=log_entrys_api
        fields= '__all__' 
    
class type_of_company_serializer(serializers.ModelSerializer):
    class Meta:
        model=type_of_company
        fields= '__all__' 
class company_name_serializer(serializers.ModelSerializer):
    class Meta:
        model=company_name
        fields= '__all__' 
class skill_serializer(serializers.ModelSerializer):
    class Meta:
        model=skill
        fields= '__all__' 
