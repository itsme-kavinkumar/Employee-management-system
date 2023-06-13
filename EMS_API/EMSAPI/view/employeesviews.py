from django.shortcuts import render
from EMSAPI.model.employeemodels import*
from rest_framework.decorators import APIView
from EMSAPI.serializer.serializers import*
from rest_framework import status
from django.contrib.auth.models import User
from knox.models import AuthToken
from  rest_framework.response import Response
from apilogs import function_api_log
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class EmployeedataView(APIView):
   
   def get(self,request):
      try:
         query=Employeedata.objects.all()
         serializer  = Employeedataserializer (query, many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response(status=status.HTTP_400_BAD_REQUEST)
          
    
   def post (self,request):
      try: 
         serializer=Employeedataserializer(data=request.data)  
          
         if serializer.is_valid():
            serializer.save() 
            print('-----------------')
            empdata=serializer.data
            skil=request.data.get('skills')
            spl_skil=skil.split(',')  
            for skil in spl_skil:
               Employee_skill.objects.create(employeeId_id=empdata['id'],skill_id=skil)                
            
            return Response({'data':serializer.data},status=status.HTTP_201_CREATED)
         else:
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':serializer.errors},status=status.HTTP_401_UNAUTHORIZED)
   
      
   def put (self,request):
      pk =request.GET.get('id')
      try:
         instance=  Employeedata.objects.get(id=pk)
         serializer= Employeedataserializer(instance=instance,data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)   
         else:
            print('-----',serializer.errors)
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':serializer.errors},status=status.HTTP_401_UNAUTHORIZED)
       
   def delete (self,request,**kwargs):
      try:
         pk = request.GET.get('id')
         instance=  Employeedata.objects.get(id=pk)
         instance.delete()
         return Response({'message':'data successfully deleted'},status=status.HTTP_200_OK)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':e},status=status.HTTP_401_UNAUTHORIZED)
class netsalary_view(APIView):
   
   def put(self,request):
      nt_salary=request.GET.get('Netsalary')
      try:
         salarydata=Employeedata.objects.all()
         print('------------',salarydata.Netsalary)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':e},status=status.HTTP_401_UNAUTHORIZED)
class onleave_list_view(APIView):
   def get(self,request):
      try:
         query=Employeedata.objects.filter(on_leave=True)
         serializer=Employeedataserializer(query,many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)

      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':e},status=status.HTTP_401_UNAUTHORIZED)
   


class attendance_view(APIView):
    
   def get(self,request):
      pk =request.GET.get('id')
   
      try:
         instance = Employeedata.objects.get(id=pk)
         # instance = Employeedata.objects.all()
         serializer = Employeedataserializer(instance)
         return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':serializer.errors},status=status.HTTP_401_UNAUTHORIZED)
      
class type_of_company_view(APIView):
   def get(self,request):
      pk=request.GET.get('id')
      try:
         query=type_of_company.objects.all()
         print('=====',query)
         serializer  = type_of_company_serializer (query, many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response(status=status.HTTP_400_BAD_REQUEST)
   def post(self,request):
      try:
         serializer=type_of_company_serializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            print('***********',serializer)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
         else:
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':"employee role class error"},status=status.HTTP_401_UNAUTHORIZED)
class company_name_view(APIView):
   def get(self,request):
      pk=request.GET.get('id')
      try:
         query=company_name.objects.all()
         serializer  = company_name_serializer (query, many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response(status=status.HTTP_400_BAD_REQUEST)
   def post(self,request):
      try:
         serializer=company_name_serializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data},status=status.HTTP_201_CREATED)
         else:
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':"employee role class error"},status=status.HTTP_401_UNAUTHORIZED)

class Employee_role_view(APIView):
   def get(self,request):
      try:
         query=Employee_role.objects.all()
         serializer  = Employee_role_serializer (query, many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response(status=status.HTTP_400_BAD_REQUEST)
   def post(self,request):
      try:
         serializer=Employee_role_serializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data},status=status.HTTP_201_CREATED)
         else:
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':"employee role class error"},status=status.HTTP_401_UNAUTHORIZED)
class salary_type_view(APIView):
   def get(self,request):
      try:
         query=salary_type.objects.all()
         serializer  = salary_type_serializer (query, many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response(status=status.HTTP_400_BAD_REQUEST)
   def post(self,request):
      try:
         serializer=salary_type_serializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            
            return Response({'data':serializer.data},status=status.HTTP_201_CREATED)
         else:
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':serializer.errors},status=status.HTTP_401_UNAUTHORIZED)
class employees_type_view(APIView):
   def get(self,request):
      try:
         query=employees_type.objects.all()
         serializer  = employees_type_serializer (query, many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response(status=status.HTTP_400_BAD_REQUEST)
   def post(self,request):
      try:
         serializer=employees_type_serializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            
            return Response({'data':serializer.data},status=status.HTTP_201_CREATED)
         else:
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':"employee type class error"},status=status.HTTP_401_UNAUTHORIZED)

class companytype_filter_viewapi(APIView):
   def get(self,request):
      pk=request.GET.get('id')
      try:
         employee_filter=Employeedata.objects.filter(Role__company_name__company_type=pk)
         serializer  = Employeedataserializer (employee_filter, many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':"company type filter class error"},status=status.HTTP_401_UNAUTHORIZED)

class companyname_filter_view(APIView):
   def get(self,request):
      pk=request.GET.get('id')
      try:
         cmpnyname=  Employeedata.objects.filter( Role__company_name=pk)    
         serializer  = Employeedataserializer (cmpnyname, many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':"company type filter class error"},status=status.HTTP_401_UNAUTHORIZED)
   
class companyrole_filter_view(APIView):
   def get(self,request):
      pk=request.GET.get('id')
      print('----------',pk)
      try:  
         employee_filter=Employeedata.objects.filter(Role=pk)
         serializer  = Employeedataserializer (employee_filter, many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':"company type filter class error"},status=status.HTTP_401_UNAUTHORIZED)  

# Double filter function
class multifilter_view(APIView):
   def get(self,request):
      
      name_pk=request.GET.get("idn")
      role_pk=request.GET.get("idr")
      print('-------',name_pk,role_pk)
      employee_list=Employeedata.objects.all()
      try:
         if name_pk!= None: 
            employee_list=employee_list.filter(Role__company_name=name_pk)
         if role_pk !=None:
            employee_list=employee_list.filter(Role=role_pk)
         serializer  = Employeedataserializer (employee_list, many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
            function_api_log(request,str(e),e)
            return Response({'error':" Multi filter class error"},status=status.HTTP_401_UNAUTHORIZED)
class Employee_skill_view(APIView):
   def get(self,request):
      try:
         query=skill.objects.all()
         serializer  = skill_serializer (query, many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response(status=status.HTTP_400_BAD_REQUEST)
   def post(self,request):
      try:
         serializer=skill_serializer(data=request.data)
         if serializer.is_valid():
            serializer.save() 
            return Response({'data':serializer.data},status=status.HTTP_201_CREATED)
         else:
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':serializer.errors},status=status.HTTP_401_UNAUTHORIZED)
       
          