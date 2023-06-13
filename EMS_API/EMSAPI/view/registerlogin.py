from django.shortcuts import render
from EMSAPI.model.employeemodels import*
from rest_framework.decorators import APIView
from EMSAPI.serializer.serializers import*
from rest_framework import status
from django.contrib.auth.models import User
from knox.models import AuthToken

from  rest_framework.response import Response
from apilogs import function_api_log
from EMSAPI.serializer.userserializer import*
from rest_framework.permissions import IsAuthenticated

class register_view(APIView):
   
   def get(self,request):
   
      try:
         query=User.objects.all()
         serializer  = create_user_serializers (query, many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':e},status=status.HTTP_401_UNAUTHORIZED)
   
   def post (self,request):
      try:
         serializer=create_user_serializers(data=request.data)
         if serializer.is_valid():
            user=serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
         else:
            error=serializer.errors
            return Response(error,status=status.HTTP_400_BAD_REQUEST) 
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':e},status=status.HTTP_401_UNAUTHORIZED)
         
         
class login_view(APIView):

   def post(self, request):
      try:
         username = request.data.get('username')
         password = request.data.get('password')
         user = authenticate(request, username=username, password=password)
         if user is not None:
            login(request, user)
            _, token=AuthToken.objects.create(user)
            return Response({'message': 'Login successful','token':token}, status=status.HTTP_200_OK)
         else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':e},status=status.HTTP_401_UNAUTHORIZED)
      