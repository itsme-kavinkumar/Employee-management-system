from telnetlib import LOGOUT
from django.shortcuts import render,redirect
from django.utils import timezone
from datetime import datetime as dt
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout
import requests
from weblogs import*
url='http://127.0.0.1:8000/'
def management(request):
    companytype=requests.get("{url}/type_of_company/".format(url=url)).json()                                   

    return render(request,"manage.html",{'cmpny_typefilter':companytype})
def add_company(request):
    try:
        if request.method=="POST":
            cmptype_id=request.POST['cmptype_id']
            company_name=request.POST['company_name']
            data={'company_type':cmptype_id,'company_name':company_name}
            response = requests.post("{url}/company_name/".format(url=url), json=data)

            print('---=---',response.status_code)
            if response.status_code == 200:
                messages.info(request,"company created")
                return render(request,"manage.html")
            elif response.status_code==401:
                messages.info(request,"company not created") 
                return render(request,"manage.html")
        companytype=requests.get("{url}/type_of_company/".format(url=url)).json() 
        return render(request,"manage.html",{'cmpny_typefilter':companytype})
    except Exception as e:
        function_log(request,str(e),e)
        return redirect('error_page')