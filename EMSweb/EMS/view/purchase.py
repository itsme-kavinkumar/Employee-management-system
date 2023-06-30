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
def purchase_home(request):

    return render(request,"purchase.html")  
def purchase_order(request):
    supplier=requests.get("{url}/supplier_url/".format(url=url)).json()
    item=requests.get("{url}/product_url/".format(url=url)).json()
    current_date = date.today()
    return render(request,"purchase_order.html",{'supplier_lst':supplier,'item_lst':item,'curnt_date':current_date}) 

def temprary_purchase(request):
    if request.method=="POST":
        supplier=request.POST.get("supplier")
        quantity=request.POST.get("quantity")
        product=request.POST.get("product")
        Amount=request.POST.get("Amount")
        date=request.POST.get("date")
        data={'supplier':supplier,'quantity':quantity,'product':product,'amount':Amount,'Date':date}
        purchase_order=requests.post("{url}/temrary_purchase_order/".format(url=url),json=data)
        print('----------------',purchase_order.status_code)
        if purchase_order.status_code==201:
            purchase_order=requests.get("{url}/temrary_purchase_order/".format(url=url)).json()
            datas={'purchase_bill':purchase_order}
            return JsonResponse(datas)
def Delete_tempurchase(request):
    try:
        if request.method == "POST":
            billid= request.POST.get("billid")
            params={"id":billid}
            delete_data= requests.delete("{url}/temrary_purchase_order/".format(url=url),params=params)
            if delete_data.status_code==200:
                purchase_order =requests.get("{url}/temrary_purchase_order/".format(url=url)).json()
                msg="Bill deleted"
                datas={'purchase_bill':purchase_order}     
                return JsonResponse(datas)
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
def Edit_temprypurchase(request):
    try: 
        purchaseid= request.GET.get("purchaseid")
       
        params={'id':purchaseid}
        temporaryy_purchase= requests.get("{url}/temrary_purchase_order/".format(url=url),params=params).json()
        data={'edit_data':temporaryy_purchase}
       
        return JsonResponse(temporaryy_purchase[0])
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
def temprary_purchase_update(request):
    try: 
        if request.method=="POST": 
            purchseid=request.POST.get("purchseid")
            supplier=request.POST.get("supplier")
            quantity=request.POST.get("quantity")
            product=request.POST.get("product")
            Amount=request.POST.get("Amount")
            date=request.POST.get("date")
            data={'supplier':supplier,'quantity':quantity,'product':product,'amount':Amount,'Date':date}
            params={'id':purchseid}
            purchase_order=requests.put("{url}/temrary_purchase_order/".format(url=url),params=params,json=data)
            print('----------update------',purchase_order.status_code)
            if purchase_order.status_code==200:
                purchase_order=requests.get("{url}/temrary_purchase_order/".format(url=url)).json()
                datas={'purchase_bill':purchase_order}
                return JsonResponse(datas)
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')    
def final_purchase_order(request):
    try: 
        current_date = date.today()
        purchase_order=requests.get("{url}/temrary_purchase_order/".format(url=url)).json() 
        print('------get--',purchase_order)
        for purchasedata in purchase_order:

            data={'supplier':purchasedata.get('supplier'),'quantity':purchasedata.get('quantity'),
                'product':purchasedata.get('product'),'amount':purchasedata.get('amount'),'remaining_qty':purchasedata.get('quantity'),'Date':str(current_date)}
            purchase_order=requests.post("{url}/final_purchase_order/".format(url=url),json=data)
            print('----------final------',purchase_order.status_code)
            if purchase_order.status_code==201:
                # purchase_order=requests.delete("{url}/temrary_purchase_order/".format(url=url)).json()
                # datas={'purchase_bill':purchase_order}
                messages.info(request,"purchase Order created")
                return redirect('purchase_order')
    except Exception as e:
        print('////////',e)
        function_log(request,str(e),e)
        
        return redirect('error_page')    
    


def pending_purchlist(request):
    purchase_lst=requests.get("{url}/final_purchase_order/".format(url=url)).json() 
    
    return render(request,"pending_purchase_lst.html",{'pending_lst':purchase_lst})
def pending_lst_delete(request):
    try: 
        deleteid=request.POST.get('deleteid')
        params={'id':deleteid}
        purchase_lst=requests.delete("{url}/final_purchase_order/".format(url=url),params=params)
        if purchase_lst.status_code==200:
            purchase_lst=requests.get("{url}/final_purchase_order/".format(url=url)).json() 
            datas={'purchase_lst':purchase_lst}
            return JsonResponse(datas)

        return render(request,"GRN.html")
    except Exception as e:
        print('////////',e)
        function_log(request,str(e),e)
        
        return redirect('error_page')    
    
#GRN create-------------
def grn_page(request):
    current_date = date.today()
    return render(request,"GRN.html",{'currentdte':current_date})
def grn_create(request,pk):
    try:
        param={'id':pk}
        purchase_lst=requests.get("{url}/final_purchase_order/".format(url=url),params=param).json() 
        
        return render(request,"GRN.html",{'purchaseGRN_lst':purchase_lst})
    except Exception as e:
        print('////////',e)
        function_log(request,str(e),e)
        
        return redirect('error_page')
def GRN_temprary_create(request):
    try:
        if request.method=="POST":
            purchseid=request.POST.get("purchseid")
            supplier=request.POST.get("supplier")
            quantity=request.POST.get("quantity")
            product=request.POST.get("product")
            Amount=request.POST.get("Amount")
            date=request.POST.get("date")
            purchase_lst=requests.get("{url}/final_purchase_order/".format(url=url)).json() 
            data={'supplier':supplier,'quantity':quantity,'product':product,'amount':Amount,'Date':date,'purchaseid':purchseid}
            purchase_grn=requests.post("{url}/tempraryGRN/".format(url=url),json=data)
            print('----------------',purchase_grn.status_code)
            if purchase_grn.status_code==201:
                purchase_grn=requests.get("{url}/tempraryGRN/".format(url=url)).json()
                datas={'purchase_grn':purchase_grn}
                return JsonResponse(datas)
        
       
        
        return render(request,"GRN.html",{'purchaseGRN_lst':purchase_lst})
    except Exception as e:
        print('////////',e)
        function_log(request,str(e),e)
        return redirect('error_page')
def final_GRN(request):
    try: 
        current_date = date.today()
        purchase_grn=requests.get("{url}/tempraryGRN/".format(url=url)).json()
        print('------get--',purchase_grn)
        for grndata in purchase_grn:

            data={'supplier':grndata.get('supplier'),'quantity':grndata.get('quantity'),'purchaseid':grndata.get('purchaseid'),
                'product':grndata.get('product'),'amount':grndata.get('amount'),'Date':str(current_date)}
            final_GRN=requests.post("{url}/final_GRN/".format(url=url),json=data)
            print('----------final------',final_GRN.status_code)

            param={'id':grndata.get('purchaseid')}
            purchase_order=requests.get("{url}/final_purchase_order/".format(url=url),params=param).json()

            for prchdata in purchase_order:
                qty=prchdata.get('remaining_qty')
                RQty=qty-grndata.get('quantity')
                print('-------RQTY------',qty)
                print('-------RQTY------',RQty)
                data={'remaining_qty':RQty,}
                purchase_order=requests.put("{url}/final_purchase_order/".format(url=url),params=param,json=data).json() 

            if final_GRN.status_code==201:
                
                messages.info(request,"GRN created")
                return redirect('grn_page')
    except Exception as e:
        print('////////',e)
        function_log(request,str(e),e)
        
        return redirect('error_page')    
#GRN----------LIST
def grn_list_page(request):
    try:   
        GRN_lst=requests.get("{url}/final_GRN/".format(url=url)).json()   
        return render(request,"pending_GRN_lst.html",{'GRN_lists':GRN_lst})
    except Exception as e:
        print('////////',e)
        function_log(request,str(e),e)
        return redirect('error_page')
def purchaseinvoice_function(request):
    try:
        GRN_data=[]
        GRN_amount=[]
        GRN_Quantity=[]
        current_date = date.today()
        current_time = datetime.now().time()
        if request.method=="POST":
            checkedid=request.POST.get("selected_values")
            print('---------------check-------',checkedid)
            checkedid=checkedid.split(',')
            for checkID in checkedid:
                param={'id':checkID}
                print('---------------checkID-------',checkID)
                GRN_invoice=requests.get("{url}/purchase_invoice_GRN/".format(url=url),params=param).json()
                GRN_data.append(GRN_invoice.get('data'))
                GRN_amount.append(GRN_invoice.get('amount'))
                GRN_Quantity.append(GRN_invoice.get('quantity'))
                print('------checkvalues--------',GRN_invoice)
            return render(request,"purchase_invoice.html",{'date':current_date,
                        'current_time':current_time,'GRN_invoice':GRN_data[0],'GRN_amount':sum(GRN_amount),'GRN_Quantity':sum(GRN_Quantity)})
    except Exception as e:
        print('////////',e)
        function_log(request,str(e),e)
        return redirect('error_page')