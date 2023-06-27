from telnetlib import LOGOUT
from django.shortcuts import render,redirect
from django.utils import timezone
from datetime import datetime as dt
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout
import requests
from weblogs import*
from django.http import JsonResponse
from django.conf import settings
from knox.models import AuthToken
url='http://127.0.0.1:8000/'

def homepage (request):
    try: 
        
        print('---helo---',settings.TOKEN)
        
     
        header = {
            'Authorization':f'Token {settings.TOKEN}'
         }
        lists=requests.get("{url}/employees/".format(url=url),headers=header)
        print('response',lists.status_code)
       
        total_employees=len(lists.json())
        onleave_list=requests.get("{url}/onleave_list/".format(url=url),headers=header).json()
        onleave_lists=len(onleave_list)
        Salarydata =requests.get("{url}/net_salary/".format(url=url),headers=header).json()
        
        return render(request,"index.html",{'total_employees':total_employees,'onleave_list':onleave_lists,'totalsalary':Salarydata.get('totalsalary')})
    except Exception as e:
        function_log(request,str(e),e)
        return redirect('error_page')

# def homepage(request):
#     try:
#         if not request.user.is_authenticated:
#             print(request.user)
#             return redirect('login_user')  
        
#         user_token = AuthToken.objects.get(user=request.user)
#         header = {
#             'Authorization': f'Token {user_token.token}'
#         }
        
#         employee_response = requests.get("{url}/employees/", headers=header)
#         print('Employee response:', employee_response.status_code)
#         total_employees = len(employee_response.json())

#         onleave_response = requests.get("{url}/onleave_list/", headers=header)
#         onleave_lists = len(onleave_response.json())

#         salary_response = requests.get("{url}/net_salary/", headers=header)
#         salary_data = salary_response.json()
#         totalsalary = salary_data.get('totalsalary')

#         print('Salary data:', salary_data)
        
#         return render(request, "index.html", {
#             'total_employees': total_employees,
#             'onleave_list': onleave_lists,
#             'totalsalary': totalsalary
#         })
#     except Exception as e:
#         print('=-=-==----=-=-=-=-=--=-=-',e)
#         function_log(request, str(e), e)
#         return redirect('error_page')


def newemployee (request):
    try:
        header = {
            'Authorization':f'Token {settings.TOKEN}'
         }
        emp_role=requests.get("{url}/Employee_role/".format(url=url),headers=header).json()
        emp_salarytype=requests.get("{url}/salary_type/".format(url=url),headers=header).json()
        emp_type=requests.get("{url}/employees_type/".format(url=url),headers=header).json()
        skill_type=requests.get("{url}/Employeeskill/".format(url=url),headers=header).json()
      
        return render (request,"pages/forms/basic_elements.html",{'emp_role':emp_role,'emp_salarytype':emp_salarytype,'emp_type':emp_type,'skill_type':skill_type})
    except Exception as e:
        function_log(request,str(e),e)
        return redirect('error_page')
def emplist (request):
    return render (request,'pages/tables/basic-table.html')

def insertemployee(request):
    try:
        
        if request.method == "POST":
            empname = request.POST.get("empname")
            dob = request.POST.get("dob")
            genderr = request.POST.get("genderr")
            bloodgroup = request.POST.get("bloodgroup")
            datejoin = request.POST.get("datejoin")
            email = request.POST.get("email")
            mobile = request.POST.get("mobile")
            address = request.POST.get("address")
            role = request.POST.get("role")
            employee_type=request.POST.get('employee_type')
            salarytype = request.POST.get("salarytype")
            workinghour = request.POST.get("workinghour")
            overtime = request.POST.get("overtime")
            cassualleave = request.POST.get("cassualleave")
        
            basicsalary = request.POST.get("basicsalary")
            hra = request.POST.get("hra")
            medicalallowance = request.POST.get("medicalallowance")
            conveyanceallowance = request.POST.get("conveyanceallowance")
            generalallowance = request.POST.get("generalallowance")
            professionaltax = request.POST.get("professionaltax")
            rd = request.POST.get("rd")
            pf = request.POST.get("pf")
            esi = request.POST.get("esi")
            skill=request.POST.get("skill")
             

            header={
            'Authorization':f'Token {settings.TOKEN}'
             }
            print(f'Token assigned: {settings.TOKEN}')
            data={'Name':empname,'DOB':dob,'Gender':genderr,'Bloodgroup':bloodgroup,
                'Datejoininng':datejoin,'Email':email,'Mobile':mobile,
                'Address':address,'Role':role,'employee_type':employee_type,'Salarytype':salarytype,
                'Workinghour':workinghour,'Overtime':overtime,'Casualleave':cassualleave,'Basicsalary':basicsalary,
                'HRA':hra,'MedicalAllowance':medicalallowance,'Coveneyance':conveyanceallowance,
                'General':generalallowance,'Professionaltax':professionaltax,'RD':rd,'PF':pf,'ESI':esi,'skills':skill}
            postdata = requests.post("{url}/employees/".format(url=url),headers=header, json=data)
            print('----------',data)
            print('---------',postdata.status_code)
            if postdata.status_code==201:
                return redirect('newemployee')
            elif postdata.status_code==400:
                emp_role=requests.get("{url}/Employee_role/".format(url=url),headers=header).json()
                emp_salarytype=requests.get("{url}/salary_type/".format(url=url),headers=header).json()
                emp_type=requests.get("{url}/employees_type/".format(url=url),headers=header).json()
                skill_type=requests.get("{url}/Employeeskill/".format(url=url),headers=header).json()
                return render (request,"pages/forms/basic_elements.html",{'Emp_data':data,'emp_role':emp_role,'emp_salarytype':emp_salarytype,'emp_type':emp_type,'skill_type':skill_type})
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')



def Deletedata(request,pk):
    try:
        header={
            'Authorization':f'Token {settings.TOKEN}'
        }
        params={"id":pk}
        delete_data= requests.delete("{url}/employees/".format(url=url),headers=header,params=params)
        if delete_data.status_code==200:
            return redirect ('showpage')
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
def Editpage(request,pk):
    try:
        params={'id':pk}
        header={
            'Authorization':f'Token {settings.TOKEN}'
        }
        edit_data= requests.get("{url}/employees/".format(url=url),headers=header,params=params).json()
        print(edit_data)
        return render(request, 'editpage.html', {'key2': edit_data[0]})
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
def UpdateData(request, pk):
    try:
        if request.method == "POST":
            empname = request.POST.get("empname")
            dob = request.POST.get("dob")
            genderr = request.POST.get("genderr")
            bloodgroup = request.POST.get("bloodgroup")
            datejoin = request.POST.get("datejoin")
            email = request.POST.get("email")
            mobile = request.POST.get("mobile")
            address = request.POST.get("address")
            role = request.POST.get("role")
            salarytype = request.POST.get("salarytype")
            workinghour = request.POST.get("workinghour")
            overtime = request.POST.get("overtime")
            cassualleave = request.POST.get("cassualleave")
            basicsalary = request.POST.get("basicsalary")
            hra = request.POST.get("hra")
            medicalallowance = request.POST.get("medicalallowance")
            conveyanceallowance = request.POST.get("conveyanceallowance")
            generalallowance = request.POST.get("generalallowance")
            professionaltax = request.POST.get("professionaltax")
            rd = request.POST.get("rd")
            pf = request.POST.get("pf")
            esi = request.POST.get("esi")
            data={'Name':empname,'DOB':dob,'Gender':genderr,'Bloodgroup':bloodgroup,
                'Datejoininng':datejoin,'Email':email,'Mobile':mobile,
                'Address':address,'Role':role,'Salarytype':salarytype,
                'Workinghour':workinghour,'Overtime':overtime,'Casualleave':cassualleave,'Basicsalary':basicsalary,
                'HRA':hra,'MedicalAllowance':medicalallowance,'Coveneyance':conveyanceallowance,
                'General':generalallowance,'Professionaltax':professionaltax,'RD':rd,'PF':pf,'ESI':esi} 
            
            params={'id':pk}
            header={
            'Authorization':f'Token {settings.TOKEN}'
        }
            edit=requests.put("{url}/employees/".format(url=url),headers=header,params=params,json=data)
            print(data)
            if edit.status_code==200:
                return redirect('showpage')
            else:   
                return redirect('showpage')
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')

   
    
def attandance (request):
    try:
        header={'Authorization':f'Token {settings.TOKEN}'}
        current_date = timezone.now().date()
        now=dt.now()
        Time = now.strftime("%I:%M %p")
        empdata2 =requests.get("{url}/employees/".format(url=url),headers=header).json()               
        return render(request,'Attendance.html',{'date':current_date,'Adata':empdata2,'time':Time})
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
def leave_status(request, pk):
    try:
        header={'Authorization':f'Token {settings.TOKEN}'}
        print(header)
        params={'id':pk}
        empdata1 =requests.get("{url}/attendance_status_data/".format(url=url),headers=header,params=params)          
        empdata=empdata1.json()

        print('empdata',empdata)
        print('-----------',empdata.get('on_leave'))
        if empdata.get('on_leave'):
            
            alterdata=empdata.get('on_leave')
            alterdata = False
            present_count=empdata.get('present_count')
            present_countt = present_count + 1
            print('************',present_countt)
            data={'on_leave':alterdata,'present_count':present_countt}
            data = requests.put("{url}/employees/".format(url=url),headers=header,params=params,json=data)
            return redirect('empattandance2')
        else:
            alterdata=empdata.get('on_leave')
            leave_count=empdata.get('leave_count')
            leave_countt = leave_count + 1
            print('+++++++++++++++++++++',leave_count)
            alterdata = True
            data={'on_leave':alterdata,'leave_count':leave_countt}
            data = requests.put("{url}/employees/".format(url=url),headers=header,params=params,json=data)
    
            return redirect('empattandance2')
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
   
def empsalary(request):
    try:
        header={'Authorization':f'Token {settings.TOKEN}'}
        Salarydata =requests.get("{url}/employees/".format(url=url),headers=header).json()
  
        return render(request,'pages/salary.html',{'data':Salarydata})
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
#checkin  checkout===================================================

def checkin_checkout(request, pk):
    try:
        header={'Authorization':f'Token {settings.TOKEN}'}
        params={'id':pk}
        now = dt.now()
        #now=now.strftime('%Y-%m-%d %I:%M %p') 
        data = requests.get("{url}/employees/".format(url=url),headers=header,params=params).json()
        checkin_checkout_data=data[0]
        print(type(now))
        if checkin_checkout_data.get('Checkin_status')==True:           
            checkin=checkin_checkout_data.get('Checkin_status')
            checkin =False 
            update_data={'Checkin_status':checkin,'Check_in':str(now)}     
            update=requests.put("{url}/employees/".format(url=url),headers=header,params=params,json=update_data)  
            return redirect('empattandance2')       
        else: 
            checkin=checkin_checkout_data.get('Checkin_status')  
            checkout = True
            update_data={'Checkin_status':checkout,'Check_out':str(now)}   
            update=requests.put("{url}/employees/".format(url=url),headers=header,params=params,json=update_data).json()
            return redirect('empattandance2')
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
def employeelist(request):
    try:
        
        header = {
            'Authorization':f'Token {settings.TOKEN}'
         }
        lists=requests.get("{url}/employees/".format(url=url),headers=header).json()
        
        companyname=requests.get("{url}/company_name/".format(url=url),headers=header).json() 
     
        companyrole=requests.get("{url}/Employee_role/".format(url=url),headers=header).json() 
       
        companytype=requests.get("{url}/type_of_company/".format(url=url),headers=header).json()  
                                    
        # data={"data1":lists,'cmpny_typefilter':companytype,
        #       'companynamefilter':companyname,
        #       'cmpny_rolefilter':companyrole}
        return render(request,'pages/tables/basic-table.html',{"data1":lists,'cmpny_typefilter':companytype,'companynamefilter':companyname,'cmpny_rolefilter':companyrole})
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')

def multi_filter(request):
    try:
        header={'Authorization':f'Token {settings.TOKEN}'}
        cmptype_id= request.GET.get("cmptype_id")
        cmprole_id= request.GET.get("cmprole_id")
        cmpname_id= request.GET.get("cmpname_id")
        
       # print('---------------------',cmptype_id,cmpname_id,cmprole_id)
        post_id={'idt':cmptype_id,'idn':cmpname_id,'idr':cmprole_id}
        role_id={'name_id':cmpname_id}
       
        
        multifilter_data=requests.get("{url}/multi_filter/".format(url=url),headers=header,params=post_id).json()
        

        companyname=requests.get("{url}/company_name/".format(url=url),headers=header).json()
        companytype=requests.get("{url}/type_of_company/".format(url=url),headers=header).json() 
        companyrole=requests.get("{url}/Employee_role/".format(url=url),headers=header,params=role_id).json()
        params={'id':cmprole_id}
        data={"data1":multifilter_data,"datan":params,
              'companynamefilter':companyname,
              'cmpny_typefilter':companytype,
              'cmpny_rolefilter':companyrole}
        return JsonResponse(data)
        return render (request,'pages/tables/basic-table.html', {"data1":multifilter_data,"datan":params,'companynamefilter':companyname,'cmpny_typefilter':companytype,'cmpny_rolefilter':companyrole})
    
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')

      
