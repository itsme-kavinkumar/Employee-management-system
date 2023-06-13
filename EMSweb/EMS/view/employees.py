from telnetlib import LOGOUT
from django.shortcuts import render,redirect
from django.utils import timezone
from datetime import datetime as dt
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout
import requests
from weblogs import*

url='http://127.0.0.1:8000/'
def homepage (request):
    try: 
        lists=requests.get("{url}/employees/".format(url=url)).json()
        total_employees=len(lists)
        onleave_list=requests.get("{url}/onleave_list/".format(url=url)).json()
        onleave_lists=len(onleave_list)
        
        return render(request,"index.html",{'total_employees':total_employees,'onleave_list':onleave_lists})
    except Exception as e:
        function_log(request,str(e),e)
        return redirect('error_page')

# Create your views here.
def newemployee (request):
    try:
        emp_role=requests.get("{url}/Employee_role/".format(url=url)).json()
        emp_salarytype=requests.get("{url}/salary_type/".format(url=url)).json()
        emp_type=requests.get("{url}/employees_type/".format(url=url)).json()
        skill_type=requests.get("{url}/Employeeskill/".format(url=url)).json()
      
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
            
            data={'Name':empname,'DOB':dob,'Gender':genderr,'Bloodgroup':bloodgroup,
                'Datejoininng':datejoin,'Email':email,'Mobile':mobile,
                'Address':address,'Role':role,'employee_type':employee_type,'Salarytype':salarytype,
                'Workinghour':workinghour,'Overtime':overtime,'Casualleave':cassualleave,'Basicsalary':basicsalary,
                'HRA':hra,'MedicalAllowance':medicalallowance,'Coveneyance':conveyanceallowance,
                'General':generalallowance,'Professionaltax':professionaltax,'RD':rd,'PF':pf,'ESI':esi,'skills':skill}
            postdata = requests.post("{url}/employees/".format(url=url), json=data)
            print('----------',data)
            print('---------',postdata.status_code)
            if postdata.status_code==201:
                return redirect('newemployee')
            elif postdata.status_code==400:
                emp_role=requests.get("{url}/Employee_role/".format(url=url)).json()
                emp_salarytype=requests.get("{url}/salary_type/".format(url=url)).json()
                emp_type=requests.get("{url}/employees_type/".format(url=url)).json()
                skill_type=requests.get("{url}/Employeeskill/".format(url=url)).json()
                return render (request,"pages/forms/basic_elements.html",{'Emp_data':data,'emp_role':emp_role,'emp_salarytype':emp_salarytype,'emp_type':emp_type,'skill_type':skill_type})
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')


def employeelist (request):
    try:
        companytype=requests.get("{url}/type_of_company/".format(url=url)).json()
        lists=requests.get("{url}/employees/".format(url=url)).json()
        companyname=requests.get("{url}/company_name/".format(url=url)).json()   
        companyrole=requests.get("{url}/Employee_role/".format(url=url)).json()                                    
        empdata1 = lists
        print('-----------------',empdata1)
        return render(request,'pages/tables/basic-table.html',{"data1":empdata1,'cmpny_typefilter':companytype,'companynamefilter':companyname,'cmpny_rolefilter':companyrole})
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
def Deletedata(request,pk):
    try:
        params={"id":pk}
        delete_data= requests.delete("{url}/employees/".format(url=url),params=params)
        if delete_data.status_code==200:
            return redirect ('showpage')
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
def Editpage(request,pk):
    try:
        params={'id':pk}
        edit_data= requests.get("{url}/employees/".format(url=url),params=params).json()
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
            edit=requests.put("{url}/employees/".format(url=url),params=params,json=data)
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
        current_date = timezone.now().date()
        now=dt.now()
        Time = now.strftime("%I:%M %p")
        empdata2 =requests.get("{url}/employees/".format(url=url)).json()               
        return render(request,'Attendance.html',{'date':current_date,'Adata':empdata2,'time':Time})
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
def leave_status(request, pk):
    try:
        params={'id':pk}
        empdata1 =requests.get("{url}/attendance_status_data/".format(url=url),params=params)          
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
            data = requests.put("{url}/employees/".format(url=url),params=params,json=data)
        else:
            alterdata=empdata.get('on_leave')
            leave_count=empdata.get('leave_count')
            leave_countt = leave_count + 1
            print('+++++++++++++++++++++',leave_count)
            alterdata = True
            data={'on_leave':alterdata,'leave_count':leave_countt}
            data = requests.put("{url}/employees/".format(url=url),params=params,json=data)
    
        return redirect('empattandance2')
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
   
def empsalary(request):
    try:
        Sdata =requests.get("{url}/employees/".format(url=url)).json()
        
        for salary_data in Sdata:
            days = 26
            Addamount =  salary_data.get('HRA') + salary_data.get('MedicalAllowance') +salary_data.get('Coveneyance') + salary_data.get('General')
            lessamount = (salary_data.get('Professionaltax') + salary_data.get('RD') + salary_data.get('PF') + salary_data.get('ESI'))
            daysalary = int(salary_data.get('Basicsalary')) / days
            leavesalary = daysalary * (salary_data.get('leave_count') - salary_data.get('Casualleave'))
        # netsalary =  (salary_data.get('Basicsalary') + Addamount ) -(lessamount + leavesalary)
            Netsalary = (salary_data.get('Basicsalary') + Addamount ) -(lessamount + leavesalary)
            print('----------',Netsalary)
            net_salary=  requests.put("{url}/employees/".format(url=url),json={'Netsalary':int(Netsalary)}).json()
            Salarydata =requests.get("{url}/employees/".format(url=url)).json()

        
        return render(request,'pages/salary.html',{'data':Salarydata})
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
#checkin  checkout===================================================

def checkin_checkout(request, pk):
    try:
        params={'id':pk}
        now = dt.now()
        data = requests.get("{url}/employees/".format(url=url),params=params).json()
        checkin_checkout_data=data[0]
        if checkin_checkout_data.get('Checkin_status'):
            checkin=checkin_checkout_data.get('Checkin_status')
            checkin =False 
            update_data={'Checkin_status':checkin,'check_in':str(now)}
            update=requests.put("{url}/employees/".format(url=url),params=params,json=update_data)  
            return redirect('empattandance2')       
        else: 
            checkin=checkin_checkout_data.get('Checkin_status')  
            checkout = True
            update_data={'Checkin_status':checkin,'check_out':str(now)}
            update=requests.put("{url}/employees/".format(url=url),params=params,json=update_data).json()
            return redirect('empattandance2')
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
def company_type_filter(request):
    try:
        if request.method == "POST":
            cmptype_id= request.POST.get("cmptype_id")
            params={'id':int(cmptype_id)}
            typ_id=int(cmptype_id)
            
            companyname=requests.get("{url}/company_name/".format(url=url)).json()
            data = requests.get("{url}/companytype_filterapi/".format(url=url),params=params).json()
            companytype=requests.get("{url}/type_of_company/".format(url=url)).json()
            companyrole=requests.get("{url}/Employee_role/".format(url=url)).json()
        return render (request,'pages/tables/basic-table.html', {"data1":data,'data':params,'cmpny_typefilter':companytype,'companynamefilter':companyname,'cmpny_rolefilter':companyrole})
        
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
def company_name_filter(request):
    try:
        if request.method == "POST":
            cmpname_id= request.POST.get("cmpname_id")
            params={'id':int(cmpname_id)}
            print('------------',cmpname_id)
            data = requests.get("{url}/companyname_filter/".format(url=url),params=params).json()
            companyname=requests.get("{url}/company_name/".format(url=url)).json()
            companytype=requests.get("{url}/type_of_company/".format(url=url)).json()
            companyrole=requests.get("{url}/Employee_role/".format(url=url)).json()
        return render (request,'pages/tables/basic-table.html', {"data1":data,"datan":params,'companynamefilter':companyname,'cmpny_rolefilter':companyrole,'cmpny_typefilter':companytype})
       
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
def company_role_filter(request):
    try:
        if request.method == "POST":
            cmprole_id= request.POST.get("cmprole_id")
            params={'id':int(cmprole_id)}
            
            data = requests.get("{url}/companyname_filter/".format(url=url),params=params).json()
            companyname=requests.get("{url}/company_name/".format(url=url)).json()
            companytype=requests.get("{url}/type_of_company/".format(url=url)).json()
            companyrole=requests.get("{url}/Employee_role/".format(url=url)).json()
        return render (request,'pages/tables/basic-table.html', {"data1":data,"datar":params,'companynamefilter':companyname,'cmpny_typefilter':companytype,'cmpny_rolefilter':companyrole})
       
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')
def multi_filter(request):
    try:
        if request.method == "POST":
            cmprole_id= request.POST.get("cmprole_id")
            cmpname_id= request.POST.get("cmpname_id")
            cmptype_id= request.POST.get("cmptype_id")
            params={'id':cmprole_id}
            post_id={'id':cmptype_id,'idn':cmpname_id,'idr':cmprole_id}
            print('------------',post_id)
            data = requests.get("{url}/companyname_filter/".format(url=url),params=params).json()
            companyname=requests.get("{url}/company_name/".format(url=url)).json()
            companytype=requests.get("{url}/type_of_company/".format(url=url)).json()
            companyrole=requests.get("{url}/multi_filter/".format(url=url)).json()
            #ff
            companyrole=requests.get("{url}/Employee_role/".format(url=url),params=post_id).json()
        return render (request,'pages/tables/basic-table.html', {"data1":data,'companynamefilter':companyname,'cmpny_typefilter':companytype,'cmpny_rolefilter':companyrole})
       
    except Exception as e:
        function_log(request,str(e),e)
        print('////////',e)
        return redirect('error_page')

      
