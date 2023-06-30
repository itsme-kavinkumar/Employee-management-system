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

class product_view(APIView):
    def get(self,request):
      pk=request.GET.get('id')
      try:
         query=product.objects.all()
        
         serializer  = product_serializer (query, many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response(status=status.HTTP_400_BAD_REQUEST)
    def post(self,request):
        try:
            serializer=product_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response({'error':"ship type class error"},status=status.HTTP_401_UNAUTHORIZED)

class supplier_view(APIView):
    def get(self,request):
      pk=request.GET.get('id')
      try:
        query=supplier.objects.all()
        tempurchase=temrary_purchase_order.objects.all()
        tempurchase.delete()
        serializer  = supplier_serializer (query, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response(status=status.HTTP_400_BAD_REQUEST)
    def post(self,request):
        try:
            serializer=supplier_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response({'error':"ship type class error"},status=status.HTTP_401_UNAUTHORIZED)
class purchase_order_view(APIView):
    def get(self,request):
      pk=request.GET.get('id')
      try:
         query=purchase_order.objects.all()
        
         serializer  = purchase_serializer (query, many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
         function_api_log(request,str(e),e)
         return Response(status=status.HTTP_400_BAD_REQUEST)
    def post(self,request):
        try:
            serializer=purchase_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response({'error':"ship type class error"},status=status.HTTP_401_UNAUTHORIZED)
class temrary_purchase_order_view(APIView):
    def get(self,request):
      pk=request.GET.get('id')
      try:
        query=temrary_purchase_order.objects.all()
        
        # total_amnt = temrary_purchase_order.objects.aggregate(Sum('amount'))
        # query_total_amount = total_amnt.get('amount__sum')
        serializer  = temprary_purchase_serializer (query, many=True)
        
        return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
        function_api_log(request,str(e),e)
        return Response(status=status.HTTP_400_BAD_REQUEST)
      
    def post(self,request):
        try:
            serializer=temprary_purchase_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
               
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('3333333333333333',e)
            function_api_log(request,str(e),e)
            return Response({'error':"customer add class error"},status=status.HTTP_401_UNAUTHORIZED)
    def put (self,request):
        pk =request.GET.get('id')
        try:
            instance=  temrary_purchase_order.objects.get(id=pk)
            serializer= temprary_purchase_serializer(instance=instance,data=request.data)
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
                instance=  temrary_purchase_order.objects.get(id=pk)
                instance.delete()
            else:
                instance=  bills.objects.all()
                instance.delete()
                print('==--=--=--=-=dletedtem')
            return Response({'message':'data successfully deleted'},status=status.HTTP_200_OK)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response({'error':e},status=status.HTTP_401_UNAUTHORIZED)
# final purchase order--------------
class final_purchase_view(APIView):

    def get(self,request):
        fbill_pk=request.GET.get('id')
        print('-----p------',fbill_pk)
        try:
            if fbill_pk !=None:
                query=purchase_order.objects.all()
                query=query.filter(id=fbill_pk)
                # total_amnt = query.aggregate(Sum('amount'))
                # query_total_amount = total_amnt.get('amount__sum')
                # print('-----------',query)
                serializer  = purchase_serializer (query, many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                query=purchase_order.objects.all()
                # total_amnt = query.aggregate(Sum('amount'))
                # query_total_amount = total_amnt.get('amount__sum')
                serializer  = purchase_serializer (query, many=True)               
                return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

    def post(self,request):
        try:
            print('=--=-=why')
            serializer=purchase_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                print('***********',serializer.data)
                tempry_dta=temrary_purchase_order.objects.all()
                tempry_dta.delete()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('*****',e)
            function_api_log(request,str(e),e)
            return Response({'error':"customer add class error"},status=status.HTTP_401_UNAUTHORIZED)
    
    def put (self,request):
        pk =request.GET.get('id')
        try:
            instance=  purchase_order.objects.get(id=pk)
            serializer= purchase_serializer(instance=instance,data=request.data)
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
            instance=  purchase_order.objects.get(id=pk)
            instance.delete()
            
            return Response({'message':'data successfully deleted'},status=status.HTTP_200_OK)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response({'error':e},status=status.HTTP_401_UNAUTHORIZED)
        

class tempraryGRN_view(APIView):
    def get(self,request):
      pk=request.GET.get('id')
      try:
        query=tempraryGRN.objects.all()
        
        # total_amnt = temrary_purchase_order.objects.aggregate(Sum('amount'))
        # query_total_amount = total_amnt.get('amount__sum')
        serializer  = temprary_GRN_serializer (query, many=True)
        
        return Response(serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
        function_api_log(request,str(e),e)
        return Response(status=status.HTTP_400_BAD_REQUEST)
      
    def post(self,request):
        try:
            serializer=temprary_GRN_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
               
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('3333333333333333',e)
            function_api_log(request,str(e),e)
            return Response({'error':"customer add class error"},status=status.HTTP_401_UNAUTHORIZED)


class final_GRN_view(APIView):

    def get(self,request):
        fbill_pk=request.GET.get('id')
        print('-----p------',fbill_pk)
        try:
            if fbill_pk !=None:
                query=finalGRN.objects.all()
                query=query.filter(id=fbill_pk)
                # total_amnt = query.aggregate(Sum('amount'))
                # query_total_amount = total_amnt.get('amount__sum')
                # print('-----------',query)
                serializer  = final_GRN_serializer (query, many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                query=finalGRN.objects.all()
                # total_amnt = query.aggregate(Sum('amount'))
                # query_total_amount = total_amnt.get('amount__sum')
                serializer  = final_GRN_serializer (query, many=True)               
                return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

    def post(self,request):
        try:
            print('=--=-=why')
            serializer=final_GRN_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                print('***********',serializer.data)
                tempry_dta=tempraryGRN.objects.all()
                tempry_dta.delete()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('*****',e)
            function_api_log(request,str(e),e)
            return Response({'error':"customer add class error"},status=status.HTTP_401_UNAUTHORIZED)
class purchase_invoice_GRN(APIView):
    def get(self,request):
        try:
            ids=request.GET.get('id')
            querys=finalGRN.objects.all()
            querys=querys.filter(id=ids)
            print('querysquerysquerys',querys.first().amount)
            amount=querys.first().amount
            quantity=querys.first().quantity
            serializer=final_GRN_serializer(querys,many=True)
            return Response({'data':serializer.data,'amount':amount,'quantity':quantity},status=status.HTTP_200_OK)
        except Exception as e:
            print('*****',e)
            function_api_log(request,str(e),e)
            return Response({'error':"customer add class error"},status=status.HTTP_401_UNAUTHORIZED) 