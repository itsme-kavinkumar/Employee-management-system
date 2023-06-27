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

class shipingtype_view(APIView):
    def get(self,request):
      pk=request.GET.get('id')
      try:
         query=ship_type.objects.all()
         print('=====',query)
         serializer  = shipingtype_serializer (query, many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response(status=status.HTTP_400_BAD_REQUEST)
    def post(self,request):
        try:
            serializer=shipingtype_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                print('***********',serializer)
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response({'error':"ship type class error"},status=status.HTTP_401_UNAUTHORIZED)
class transporters_view(APIView):
    def get(self,request):
        pk=request.GET.get('id')
        try:
            query=transporters.objects.all()
            print('=====',query)
            if pk!= None:
                query=query.filter(id=pk)
            serializer  = transporters_serializer (query, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def post(self,request):
        try:
            serializer=transporters_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                print('***********',serializer)
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response({'error':"transporters  class error"},status=status.HTTP_401_UNAUTHORIZED)
    def delete (self,request,**kwargs):
        try:
            pk = request.GET.get('id')
            instance=  transporters.objects.get(id=pk)
            instance.delete()
            return Response({'message':'data successfully deleted'},status=status.HTTP_200_OK)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response({'error':e},status=status.HTTP_401_UNAUTHORIZED)
    def put (self,request):
      pk =request.GET.get('id')
      try:
         instance=  transporters.objects.get(id=pk)
         serializer= transporters_serializer(instance=instance,data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)   
         else:
            print('-----',serializer.errors)
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response({'error':serializer.errors},status=status.HTTP_401_UNAUTHORIZED)
class customer_add_view(APIView):
    def get(self,request):
      pk=request.GET.get('id')
      try:
        query=customer_add.objects.all()
        print('=====',pk)
        serializer  = customer_add_serializer (query, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response(status=status.HTTP_400_BAD_REQUEST)
      
    def post(self,request):
        try:
            serializer=customer_add_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                print('***********',serializer.data)
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response({'error':"customer add class error"},status=status.HTTP_401_UNAUTHORIZED)
class temprybill_get_edit(APIView):
    def get(self,request):
        pk=request.GET.get('id')
        try:
            query=bills.objects.all()
            print('=====',pk)
            query=query.filter(id=pk)
            serializer  = bills_serializer (query, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
class temporary_bill_view(APIView):
    def get(self,request):
      pk=request.GET.get('id')
      try:
        query=bills.objects.all()
        #print('=====',query)
        total_amnt = bills.objects.aggregate(Sum('amount'))
        #print('=======================',total_amnt)  
        query_total_amount = total_amnt.get('amount__sum')
        print('=======================',query_total_amount)
        serializer  = bills_serializer (query, many=True)
        
        return Response({'data':serializer.data,'total':query_total_amount},status=status.HTTP_200_OK)
      except Exception as e:
        function_api_log(request,str(e),e)
        return Response(status=status.HTTP_400_BAD_REQUEST)
      
    def post(self,request):
        try:
            serializer=bills_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
               
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response({'error':"customer add class error"},status=status.HTTP_401_UNAUTHORIZED)
    def put (self,request):
        pk =request.GET.get('id')
        try:
            instance=  bills.objects.get(id=pk)
            serializer= bills_serializer(instance=instance,data=request.data)
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
            print('==--=--=--=-=',pk)
            if pk != None:
                instance=  bills.objects.get(id=pk)
                instance.delete()
            else:
                instance=  bills.objects.all()
                instance.delete()
                print('==--=--=--=-=dletedtem')
            return Response({'message':'data successfully deleted'},status=status.HTTP_200_OK)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response({'error':e},status=status.HTTP_401_UNAUTHORIZED)
        
class final_bill_view(APIView):

    def get(self,request):
        fbill_pk=request.GET.get('id')
        print('-----------',fbill_pk)
        try:
            if fbill_pk !=None:
                query=final_bills.objects.all()
                query=query.filter(customer=fbill_pk)
                total_amnt = query.aggregate(Sum('amount'))
                query_total_amount = total_amnt.get('amount__sum')
                print('-----------',query)
                serializer  = final_bills_serializer (query, many=True)
                return Response({'data':serializer.data,'total':query_total_amount},status=status.HTTP_200_OK)
            else:
                query=final_bills.objects.all()
                total_amnt = query.aggregate(Sum('amount'))
                query_total_amount = total_amnt.get('amount__sum')
                serializer  = final_bills_serializer (query, many=True)               
                return Response({'data':serializer.data,'total':query_total_amount},status=status.HTTP_200_OK)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

    def post(self,request):
        try:
            print('=--=-=why')
            serializer=final_bills_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                print('***********',serializer.data)
                tempry_dta=bills.objects.all()
                tempry_dta.delete()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response({'error':"customer add class error"},status=status.HTTP_401_UNAUTHORIZED)
    
    def put (self,request):
        pk =request.GET.get('id')
        try:
            instance=  final_bills.objects.get(id=pk)
            serializer= final_bills_serializer(instance=instance,data=request.data)
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
            instance=  final_bills.objects.get(id=pk)
            instance.delete()
            
            return Response({'message':'data successfully deleted'},status=status.HTTP_200_OK)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response({'error':e},status=status.HTTP_401_UNAUTHORIZED)
        
class final_bill_edit_data(APIView):
    def get(self,request): 
        fbilledit_pk=request.GET.get('id')
        print('-----g------',fbilledit_pk)
        try:
            query=final_bills.objects.all()
            query=query.filter(id=fbilledit_pk)
            serializer = final_bills_serializer(query, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
# class bills_view(APIView):
#     def get(self,request):
#       pk=request.GET.get('id')
#       try:
#          query=bills.objects.all()
#          print('=====',query)
#          serializer  = bills_serializer (query, many=True)
#          return Response(serializer.data,status=status.HTTP_200_OK)
#       except Exception as e:
#          function_api_log(request,str(e),e)
#          return Response(status=status.HTTP_400_BAD_REQUEST)
    # def post(self,request):
    #     try:
            
    #         print('ffffffffffffffffff',request.data)
           
    #         customer=request.data.get('customer',[])
    #         trans_porter=request.data.get('trans_porter',[])
    #         type_shiping=request.data.get('type_shiping',[])
    #         amount=request.data.get('amount',[])

    #         customer = customer.replace('[', '').replace(']', '')
    #         customer = customer.replace('"', '')
    #         #-----------
    #         type_shiping = type_shiping.replace('[', '').replace(']', '')
    #         type_shiping = type_shiping.replace('"', '')
    #          #-----------
    #         trans_porter = trans_porter.replace('[', '').replace(']', '')
    #         trans_porter = trans_porter.replace('"', '')
    #         #-----------
    #         amount = amount.replace('[', '').replace(']', '')
    #         amount = amount.replace('"', '')
    #         print('----***********--',customer,trans_porter,type_shiping,amount)
    #         customer_splt=customer.split(',')  
    #         trans_porter=trans_porter.split(',') 
    #         type_shiping=type_shiping.split(',')
    #         amount=amount.split(',')
    #         for custom_splt in customer_splt:
    #             print('+++++++++++',custom_splt)
    #             for trans_porter in trans_porter:
    #                 print('+++++++++++',trans_porter)
    #                 for type_shiping in type_shiping:
    #                     print('+++++++++++',type_shiping)
    #                 for amount in amount:
    #                     print('+++++++++++',amount)

    #         bills.objects.create(customer_id=custom_splt,trans_porter_id=trans_porter,type_shiping_id=type_shiping,amount=amount)

    #         return Response({'error':"bill  created"},status=status.HTTP_201_CREATED)
       
               
    #     except Exception as e:
    #         function_api_log(request,str(e),e)
    #         return Response({'error':"customer add class error"},status=status.HTTP_401_UNAUTHORIZED)