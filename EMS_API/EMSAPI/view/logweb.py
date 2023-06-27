from django.shortcuts import render
from EMSAPI.model.employeemodels import*
from rest_framework.decorators import APIView
from EMSAPI.serializer.serializers import*
from rest_framework import status
from django.contrib.auth.models import User
from knox.models import AuthToken
from  rest_framework.response import Response
from apilogs import function_api_log
class web_log_view(APIView):
    def post (self,request):
      try:
         serializer=log_entrys_api_serializer(data=request.data)
         if serializer.is_valid():
            user=serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
         else:
            error=serializer.errors
            return Response(error,status=status.HTTP_400_BAD_REQUEST) 
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':e},status=status.HTTP_401_UNAUTHORIZED)