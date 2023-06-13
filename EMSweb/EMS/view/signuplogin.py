from telnetlib import LOGOUT
from django.shortcuts import render,redirect
from django.utils import timezone
from datetime import datetime as dt
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout
import requests
from weblogs import*
url='http://127.0.0.1:8000/'
# Create your views here.
def error_page(request):
    return render(request,'error.html')
def home_pagee(request):
    return render(request,"index.html")

def signup(request):
    try:
        if request.method=="POST":
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            confirm_password=request.POST['confirm_password']
        
            if password == confirm_password:
                data={'first_name':first_name,'last_name':last_name,'username':username,'email':email,'password':password}
                response = requests.post("{url}/register/".format(url=url), json=data)
                response_data=response.json()
                print('=====',response_data)
                
                if response.status_code == 201: 
                    return redirect('login_user') 
                
                elif response.status_code== 400:

                    if 'username' in response_data:
                        msg=response_data.get('username')
                        messages.info(request,"Username Not Available")
                        #return redirect('signup')
                        return render(request,"signup.html",{'data':data})  

                    elif 'msg' in response_data:
                        msgg=response_data.get('msg')
                       
                        messages.info(request,msgg[0])
                        return render(request,"signup.html",{'data':data})        
            else:
                messages.info(request,"enter correct confirm password") 
                return render(request,"signup.html",{'data':data})            
        return render(request,"signup.html")  
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
def  login_user(request):
    try:
        if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            data={'username':username,'password':password}
            response = requests.post("{url}/login/".format(url=url), json=data)  
            print('---=---',response.status_code)
            if response.status_code == 200:
                return redirect('employee-page')
            elif response.status_code==401:
                messages.info(request,"invalid Username or password") 
                return render(request,"signup.html",{'data':data})
  
        return render(request,"signup.html")
    except Exception as e:
        function_log(request,str(e),e)
        return redirect('error_page')
      
   

def logout_user(request):
    logout(request)
    return redirect('login_user')
