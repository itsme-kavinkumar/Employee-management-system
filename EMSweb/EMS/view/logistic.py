from telnetlib import LOGOUT
from django.shortcuts import render,redirect
from django.utils import timezone
from datetime import datetime as dt
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout
import requests
from weblogs import*
from django.http import JsonResponse
from django.db.models import Sum
from datetime import date
from datetime import datetime
url='http://127.0.0.1:8000/'
def logistics_page(request):
    
    shiptype_lst=requests.get("{url}/shipingtype/".format(url=url)).json()
    transporters_lst=requests.get("{url}/transporters/".format(url=url)).json()
    customer_lst=requests.get("{url}/customer_add/".format(url=url)).json()
    temporaryy_bill=requests.get("{url}/temporary_bill/".format(url=url)).json()
    
    return render(request,"logistic.html",{'shiptype_lst':shiptype_lst,'transporters_lst':transporters_lst,
                               'customer_lst':customer_lst,'temporaryy_bill':temporaryy_bill.get('data'),'totalamount':temporaryy_bill.get("total")})

# def temprry_billget_ajax(request):
#     temporaryy_bill=requests.get("{url}/temporary_bill/".format(url=url)).json()
#     print('te5-----------',temporaryy_bill)
#     data={'bill_data':temporaryy_bill.get('data'),'totalAmount':temporaryy_bill.get("total")}
#     return JsonResponse(data)



def temprry_bil_clear(request):
    
    temporaryy_bill=requests.delete("{url}/temporary_bill/".format(url=url)).json()
    shiptype_lst=requests.get("{url}/shipingtype/".format(url=url)).json()
    transporters_lst=requests.get("{url}/transporters/".format(url=url)).json()
    customer_lst=requests.get("{url}/customer_add/".format(url=url)).json()
    temporaryy_bill=requests.get("{url}/temporary_bill/".format(url=url)).json()
    
    return render(request,"logistic.html",{'shiptype_lst':shiptype_lst,'transporters_lst':transporters_lst,
                            'customer_lst':customer_lst,'temporaryy_bill':temporaryy_bill.get('data'),'totalamount':temporaryy_bill.get("total")})

def logistic(request):
    try:
        print('6456444745757')
        if request.method == "POST":
            print('-----',request.POST)
            customer = request.POST.get("customer")
            transporter = request.POST.get("transporter")
            shipping_type = request.POST.get("shipping_type")
            amount = request.POST.get("amount")
            
            data={'customer':customer,'trans_porter':transporter,'type_shiping':shipping_type,'amount':amount}
            print('-----------------------',data)
            customer_lst=requests.post("{url}/temporary_bill/".format(url=url),json=data)
           
            
            if customer_lst.status_code== 201:
                #msg={'message':"service Added"}
                #return JsonResponse(msg)
                #messages.info(request,"service added")
                temporaryy_bill=requests.get("{url}/temporary_bill/".format(url=url)).json()
                print('te5-----------',temporaryy_bill)
                msg="Bill Added"
                data={'bill_data':temporaryy_bill.get('data'),'totalAmount':temporaryy_bill.get("total"),'message':msg}
                return JsonResponse(data)

                #return redirect('logistics_page')
            print('--------------',customer_lst.status_code)
            # return JsonResponse("bill created")
        return render(request,"logistic.html")
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
    

def finalbill_function(request):
    try:
        print('=========run =======',)
        temporaryy_bill=requests.get("{url}/temporary_bill/".format(url=url)).json()
        temporaryy_bill=temporaryy_bill.get('data')
        print('----------------finallllllllll-------------',temporaryy_bill)
        
        for temporaryybill in temporaryy_bill:
            data={'customer':temporaryybill.get('customer'),'trans_porter':temporaryybill.get('customer'),
                'type_shiping':temporaryybill.get('type_shiping'),'amount':temporaryybill.get('amount')}
            final_bill=requests.post("{url}/final_bill/".format(url=url),json=data)
            print('--------#------------',final_bill.status_code)
        if final_bill.status_code==201:
            messages.info(request,"success")
            return redirect('logistics_page')
        else:
            messages.info(request,"Failed") 
            return redirect('temprry_bil_clear')
       
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
def final_bill_func(request):
    customer_lst=requests.get("{url}/customer_add/".format(url=url)).json()
    bill_lst=requests.get("{url}/final_bill/".format(url=url)).json()
    totalAmount=bill_lst.get('total')
    bill_lst=bill_lst.get('data')
    
    print('=-------',totalAmount,bill_lst)
    return render(request,"bill_list.html",{'customer_lst':customer_lst,'data1':bill_lst,'totalamount':totalAmount})
def final_bill_filter(request):
    customer_id= request.GET.get("customer_id")
    print('----',customer_id)
    params={'id':customer_id}
    bill_lst=requests.get("{url}/final_bill/".format(url=url),params=params).json()
    fbill_lst=bill_lst.get('data')
    totalAmount=bill_lst.get("total")
    print('============',fbill_lst)
    print('============',totalAmount)
    data={'bill_data':fbill_lst,'totalAmount':totalAmount}
    return JsonResponse(data)

def fbill_print(request,pk):
    params={'id':pk}
    current_date = date.today()
    current_time = datetime.now().time()
    customer_lst=requests.get("{url}/customer_add/".format(url=url)).json()
    temporaryy_bill=requests.get("{url}/final_bill/".format(url=url),params=params ).json()
    # cus_id_gwt=temporaryy_bill.get("data")
    # params={'id':cus_id_gwt[0].get('id')}
    # print('--12----',cus_id_gwt[0].get('id'))
    # customer_lst=requests.get("{url}/customer_add/".format(url=url),params=params).json()
    print('------++++++++--------',temporaryy_bill)
    customername=temporaryy_bill.get('data')
    return render(request,"invoice.html",{'temporaryy_bill':temporaryy_bill.get('data'),'totalamount':temporaryy_bill.get("total"),'date':current_date,'current_time':current_time,'customer_lst':customer_lst,'customername':customername[0]})
def fbill_delete(request,pk):
    try:
        params={"id":pk}
        
        delete_data= requests.delete("{url}/final_bill/".format(url=url),params=params)
        if delete_data.status_code==200:
            messages.info(request," bill deleted")
            return redirect ('final_bill_func')
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')

    
def fbill_edit(request,pk):
    try:
        params={'id':pk}
        final_bill=requests.get("{url}/final_bill_edit/".format(url=url),params=params).json()
        shiptype_lst=requests.get("{url}/shipingtype/".format(url=url)).json()
        transporters_lst=requests.get("{url}/transporters/".format(url=url)).json()
        customer_lst=requests.get("{url}/customer_add/".format(url=url)).json()
       
        print('---sd------',final_bill)
        return render(request,"bill_list_edit.html",{'final_bill':final_bill[0],'shiptype_lst':shiptype_lst,'transporters_lst':transporters_lst,'customer_lst':customer_lst})
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
def fbill_update(request,pk):
    try:
        if request.method == "POST":
                print('-----',request.POST)
                customer = request.POST.get("customer")
                shipping_type = request.POST.get("shipping_type")
                transporter = request.POST.get("transporter")
                amount = request.POST.get("amount")
                
                data={'customer':customer,'trans_porter':shipping_type,
                'type_shiping':transporter,'amount':amount}
                params={'id':pk}
                edit=requests.put("{url}/final_bill/".format(url=url),params=params,json=data)
                if edit.status_code==200:
                    messages.info(request,"successfully updated")
                    return redirect('final_bill_func')
                else:   
                    messages.info(request,"Failed")
                    return redirect('final_bill_func')
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
    
def customerAdd(request):
    try:
        if request.method == "POST":
            Customer = request.POST.get("Customer")
            mobile = request.POST.get("mobile")
           
            datas={'custome_name':Customer,'mobile':mobile}
            print('--------------',datas)
            customer_lst=requests.post("{url}/customer_add/".format(url=url),json=datas)
        if customer_lst.status_code==201:
            messages.info(request,"customer successsfully Added")
            return redirect('logistics_page')
        else:
            messages.info(request," failed")
            return redirect('logistics_page')
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
def Delete_bill(request):
    try:
        if request.method == "POST":
            billid= request.POST.get("billid")
            print('---deleteid--',billid)
            params={"id":billid}
            delete_data= requests.delete("{url}/temporary_bill/".format(url=url),params=params)
            if delete_data.status_code==200:
                temporaryy_bill=requests.get("{url}/temporary_bill/".format(url=url)).json()
                print('delete-----------',temporaryy_bill)
                msg="Bill deleted"
                data={'bill_data':temporaryy_bill.get('data'),'totalAmount':temporaryy_bill.get("total"),'message':msg}
                return JsonResponse(data)
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
def Edit_bill(request):
    try: 
        customerid= request.GET.get("customerid")
        print('--------id------',customerid)
        params={'id':customerid}
        temporaryy_bill= requests.get("{url}/temprybill_get_edit/".format(url=url),params=params).json()
        data={'edit_data':temporaryy_bill}
        #temporaryy_bill=temporaryy_bill.get('data')
        print('=====',temporaryy_bill)
        return JsonResponse(temporaryy_bill[0])
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
    
def temprybill_update(request):
    try:
        if request.method == "POST":
            print('-----',request.POST)
            billid = request.POST.get("billid")
            customer = request.POST.get("customer")
            transporter = request.POST.get("transporter")
            shipping_type = request.POST.get("shipping_type")
            amount = request.POST.get("amount")
            params={'id':billid}
            data={'customer':customer,'trans_porter':transporter,'type_shiping':shipping_type,'amount':amount}
            
            edit=requests.put("{url}/temporary_bill/".format(url=url),params=params,json=data)
            if edit.status_code==200:
                temporaryy_bill=requests.get("{url}/temporary_bill/".format(url=url)).json()
                print('te5-----------',temporaryy_bill)
                msg="Bill Added"
                data={'bill_data':temporaryy_bill.get('data'),'totalAmount':temporaryy_bill.get("total"),'message':msg}
                return JsonResponse(data)
            else:   
                messages.info(request,"Failed")
                return redirect('tranporter_func')
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')


def tranporter_func(request):
    transporter_lst=requests.get("{url}/transporters/".format(url=url)).json()
    return render(request,"transporters.html",{'transporter_lst':transporter_lst})
 
def tranporter_add(request):
    try:
        if request.method == "POST":
            print('-----',request.POST)
            trans_porter = request.POST.get("trans_porter")
            Mobile = request.POST.get("Mobile")
            email = request.POST.get("email")
            address = request.POST.get("address")
            
            data={'transporter':trans_porter,'mobile':Mobile,'email':email,'address':address}
            print('-----------------------',data)
            transporter_lst=requests.post("{url}/transporters/".format(url=url),json=data)
            if transporter_lst.status_code== 201:
                messages.info(request,"transporter added")
                return redirect('tranporter_func') 
                
            else:
                messages.info(request,"Failed")
                return redirect('tranporter_func')
            # return JsonResponse("bill created")
        return render(request,"transporters.html") 
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
def Delete_transporter(request,pk):
    try:
        params={"id":pk}
        delete_data= requests.delete("{url}/transporters/".format(url=url),params=params)
        if delete_data.status_code==200:
            messages.info(request," successfully deleted")
            return redirect ('tranporter_func')
        else:
            messages.info(request," Failed") 
            return redirect ('tranporter_func')
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')

def edit_tranporter(request,pk): 
    params={"id":pk}
    transporter_lst=requests.get("{url}/transporters/".format(url=url),params=params).json()
    print('----------',transporter_lst)
    return render(request,"transporter_edit.html",{'transporter_edit':transporter_lst[0]})
def tranporter_update(request,pk):
    try:
        if request.method == "POST":
            print('-----',request.POST)
            trans_porter = request.POST.get("trans_porter")
            Mobile = request.POST.get("Mobile")
            email = request.POST.get("email")
            address = request.POST.get("address")
            
            data={'transporter':trans_porter,'mobile':Mobile,'email':email,'address':address}
            params={'id':pk}
            edit=requests.put("{url}/transporters/".format(url=url),params=params,json=data)
            if edit.status_code==200:
                messages.info(request,"successfully updated")
                return redirect('tranporter_func')
            else:   
                messages.info(request,"Failed")
                return redirect('tranporter_func')
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
def invoice_function(request):
    current_date = date.today()
    current_time = datetime.now().time()
    customer_lst=requests.get("{url}/customer_add/".format(url=url)).json()
    temporaryy_bill=requests.get("{url}/temporary_bill/".format(url=url)).json()
    # cus_id_gwt=temporaryy_bill.get("data")
    # params={'id':cus_id_gwt[0].get('id')}
    # print('--12----',cus_id_gwt[0].get('id'))
    # customer_lst=requests.get("{url}/customer_add/".format(url=url),params=params).json()
    customername=temporaryy_bill.get('data')
    
    return render(request,"invoice.html",{'temporaryy_bill':temporaryy_bill.get('data'),'totalamount':temporaryy_bill.get("total"),'date':current_date,'current_time':current_time,'customer_lst':customer_lst,'customername':customername[0]})