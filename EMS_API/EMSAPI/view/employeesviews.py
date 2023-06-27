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
from django.db.models import Sum
from knox.auth import TokenAuthentication
from rest_framework.authtoken.models import Token
# Create your views here.
class EmployeedataView(APIView):
   authentication_classes = [TokenAuthentication]
   permission_classes = [IsAuthenticated] 
   def get(self,request):
      try:
         if request.user:
            print('oe9745876',request.user)
           
            query=Employeedata.objects.filter(created_by=request.user)
           
            serializer  = Employeedataserializer (query, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
         else:
                return Response({"message": "User is not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response(status=status.HTTP_400_BAD_REQUEST)
          
    
   def post(self, request):
      try:
         serializer = Employeedataserializer(data=request.data)
         if serializer.is_valid():
            employee = serializer.save(created_by=request.user)

            skills = request.data.get('skills')
            if skills:
               skill_list = skills.split(',')
               for skill in skill_list:
                  Employee_skill.objects.create(employeeId=employee, skill_id=skill, created_by=request.user)

               return Response(serializer.data, status=status.HTTP_201_CREATED)

         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      except Exception as e:
            function_api_log(request, str(e), e)
            return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
      
   def put (self,request):
      pk =request.GET.get('id')
      print('pkkkkkkkkkkkkkkkkkkk',pk)
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
         print('eeeeeeeeeeeee',e)
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
   authentication_classes = [TokenAuthentication]
   permission_classes = [IsAuthenticated]
   def get(self,request):
      try:
         if request.user:
            salarydata=Employeedata.objects.filter(created_by=request.user)
            for salary_data in salarydata:
               days = 26
               Addamount =  salary_data.HRA+ salary_data.MedicalAllowance +salary_data.Coveneyance + salary_data.General
               lessamount = (salary_data.Professionaltax + salary_data.RD+ salary_data.PF + salary_data.ESI)
               daysalary = int(salary_data.Basicsalary) / days
               leavesalary = daysalary * (salary_data.leave_count - salary_data.Casualleave)
         # netsalary =  (salary_data.get('Basicsalary') + Addamount ) -(lessamount + leavesalary)
               Netsalary = (salary_data.Basicsalary + Addamount ) -(lessamount + leavesalary)
               salary_data.Netsalary=Netsalary
               salary_data.save()
               print('----------',Netsalary)
            total_amnt = salarydata.aggregate(Sum('Netsalary'))
            query_total_amount = total_amnt.get('Netsalary__sum')
            serializer=Employeedataserializer(salarydata,many=True)
            return Response({'data':serializer.data,'totalsalary':query_total_amount},status=status.HTTP_200_OK)

      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':e},status=status.HTTP_401_UNAUTHORIZED)
class onleave_list_view(APIView):
   authentication_classes = [TokenAuthentication]
   permission_classes = [IsAuthenticated] 
   def get(self,request):
      try:
         if request.user:
            query=Employeedata.objects.filter(created_by=request.user)
            query=query.filter(on_leave=True)
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
   authentication_classes = [TokenAuthentication]
   permission_classes = [IsAuthenticated] 
   def get(self,request):
      pk=request.GET.get('id')
      try:
         if request.user:
            query=type_of_company.objects.all()
            query=query.filter(created_by_id=request.user)
            print('=====',query)
            serializer  = type_of_company_serializer (query, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response(status=status.HTTP_400_BAD_REQUEST)
   def post(self,request):
      try:
         print('--------',request.data)
         serializer=type_of_company_serializer(data=request.data)
         if serializer.is_valid():
            serializer.validated_data['created_by']=request.user
            serializer.save()
            print('***********',serializer)
            #type_of_company.objects.create(created_by_id=request.user.id)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
         else:
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':"company type class error"},status=status.HTTP_401_UNAUTHORIZED)
class company_name_view(APIView):
   authentication_classes = [TokenAuthentication]
   permission_classes = [IsAuthenticated] 
   def get(self,request):
      pk=request.GET.get('id')
      try:
         if request.user:
            query=company_name.objects.all()
            query=query.filter(created_by=request.user)
            serializer  = company_name_serializer (query, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response(status=status.HTTP_400_BAD_REQUEST)
   def post(self,request):
      try:
         serializer=company_name_serializer(data=request.data)
         if serializer.is_valid():
            serializer.validated_data['created_by']=request.user
            serializer.save()
            return Response({'data':serializer.data},status=status.HTTP_201_CREATED)
         else:
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':"employee role class error"},status=status.HTTP_401_UNAUTHORIZED)

class Employee_role_view(APIView):
   authentication_classes = [TokenAuthentication]
   permission_classes = [IsAuthenticated] 
   def get(self,request):
      role_pk=request.GET.get('name_id')
      
      try:
         if request.user:
            query=Employee_role.objects.all()
            query=query.filter(created_by=request.user)
            if role_pk != None:
               query=query.filter(company_name=role_pk)
               print('@@@@@@@@@@@@@@@@@@@@@@',role_pk,'------',query)
               
            serializer  = Employee_role_serializer (query, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response(status=status.HTTP_400_BAD_REQUEST)
   def post(self,request):
      try:
         serializer=Employee_role_serializer(data=request.data)
         if serializer.is_valid():
            serializer.validated_data['created_by']=request.user
            serializer.save()
            return Response({'data':serializer.data},status=status.HTTP_201_CREATED)
         else:
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':"employee role class error"},status=status.HTTP_401_UNAUTHORIZED)
class salary_type_view(APIView):
   authentication_classes = [TokenAuthentication]
   permission_classes = [IsAuthenticated] 
   def get(self,request):
      try:
         query=salary_type.objects.all()
         query=query.filter(created_by_id=request.user)
         serializer  = salary_type_serializer (query, many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response(status=status.HTTP_400_BAD_REQUEST)
   def post(self,request):
      try:
         serializer=salary_type_serializer(data=request.data)
         if serializer.is_valid():
            serializer.validated_data['created_by']=request.user
            serializer.save()
            
            return Response({'data':serializer.data},status=status.HTTP_201_CREATED)
         else:
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':serializer.errors},status=status.HTTP_401_UNAUTHORIZED)
class employees_type_view(APIView):
   authentication_classes = [TokenAuthentication]
   permission_classes = [IsAuthenticated] 
   def get(self,request):
      try:
         query=employees_type.objects.all()
         query=query.filter(created_by=request.user)
         serializer  = employees_type_serializer (query, many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response(status=status.HTTP_400_BAD_REQUEST)
   def post(self,request):
      try:
         serializer=employees_type_serializer(data=request.data)
         if serializer.is_valid():
            serializer.validated_data['created_by']=request.user
            serializer.save()
            
            return Response({'data':serializer.data},status=status.HTTP_201_CREATED)
         else:
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':"employee type class error"},status=status.HTTP_401_UNAUTHORIZED)


# Double filter function
class multifilter_view(APIView):
   authentication_classes = [TokenAuthentication]
   permission_classes = [IsAuthenticated] 
   
   def get(self,request):
      type_pk=request.GET.get("idt")
      name_pk=request.GET.get("idn")
      role_pk=request.GET.get("idr")
      # print('-------',type_pk,name_pk,role_pk)
      employee_list=Employeedata.objects.all()
      employee_list=employee_list.filter(created_by=request.user)
      try:
         
         if type_pk!= '0': 
            employee_list=employee_list.filter(Role__company_name__company_type=type_pk)
         if name_pk!= '0': 
            employee_list=employee_list.filter(Role__company_name=name_pk)
         if role_pk !='0':
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
         query=query.filter(created_by=request.user)
         serializer  = skill_serializer (query, many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response(status=status.HTTP_400_BAD_REQUEST)
   def post(self,request):
      try:
         serializer=skill_serializer(data=request.data)
         if serializer.is_valid():
            serializer.validated_data['created_by']=request.user
            serializer.save() 
            return Response({'data':serializer.data},status=status.HTTP_201_CREATED)
         else:
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':serializer.errors},status=status.HTTP_401_UNAUTHORIZED)
       
          