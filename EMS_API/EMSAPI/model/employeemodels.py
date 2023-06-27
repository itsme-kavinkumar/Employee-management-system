from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from datetime import datetime as dt
# Create your models here.
class type_of_company(models.Model):
    company_type=models.CharField(max_length=40,blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,) 
 
        
class company_name(models.Model):
    company_name=models.CharField(max_length=40,blank=True, null=True)
    company_type=models.ForeignKey(type_of_company,on_delete=models.CASCADE,null=True,related_name="cmpmytyp")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
class Employee_role(models.Model):
    Employee_role=models.CharField(max_length=40,blank=True, null=True)
    company_name=models.ForeignKey(company_name,on_delete=models.CASCADE,null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
class salary_type(models.Model):
    salary_type=models.CharField(max_length=40,blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
class employees_type(models.Model):
    employees_type=models.CharField(max_length=40,blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
class skill(models.Model):
    Skill=models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
class Employeedata(models.Model):
    #employee details
    Name=models.CharField(max_length=50,blank=True, null=True)
    DOB=models.CharField(max_length=50,blank=True, null=True)
    Gender=models.CharField(max_length=50,blank=True, null=True)
    Bloodgroup=models.CharField(max_length=50,blank=True, null=True)
    Datejoininng=models.CharField(max_length=50,blank=True, null=True)
    Email=models.EmailField(max_length=50,blank=True, null=True)
    Mobile=models.CharField(max_length=50,blank=True, null=True)
    Address=models.CharField(max_length=50,blank=True,null=True)
    Role=models.ForeignKey(Employee_role,on_delete=models.CASCADE,related_name='emplemplrl',blank=True, null=True)
    #salary deatails
    Salarytype=models.ForeignKey(salary_type,on_delete=models.CASCADE,related_name='emplempltyp',blank=True, null=True)
    employee_type=models.ForeignKey(employees_type,on_delete=models.CASCADE,related_name='emplemplemptp',blank=True, null=True)
    Workinghour=models.IntegerField(default=0)
    Overtime=models.IntegerField(default=0)
    Casualleave=models.IntegerField(default=0) 
    Basicsalary=models.IntegerField(default=0)
    HRA=models.IntegerField(default=0)
    MedicalAllowance=models.IntegerField(default=0)
    Coveneyance=models.IntegerField(default=0)
    General=models.IntegerField(default=0)
    Professionaltax=models.IntegerField(default=0)
    RD=models.IntegerField(default=0)
    PF=models.IntegerField(default=0)
    ESI=models.IntegerField(default=0)
    #attendance data
    leave_count = models.IntegerField(default=0)
    present_count = models.IntegerField(default=0)
    on_leave = models.BooleanField(blank=True, null=True)
    Netsalary=models.IntegerField(default=0)
    
    Checkin_status= models.BooleanField(default=True)
    Check_in = models.DateTimeField( help_text="Time in", null=True, blank=True)

    Check_out = models.DateTimeField(blank=True, help_text="Time out", null=True)
    WorkedHour = models.IntegerField(default=0)

    Date=models.CharField(max_length=50,blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.Name
    # def save(self, *args, **kwargs):
    #     # now = dt.now()
    #     # #now=now.strftime('%Y-%m-%d %I:%M %p') 
    #     if self.Checkin_status:
    #         self.Check_out = timezone.localtime()
    #     else:
    #         self.Check_in=timezone.localtime()
        super().save(*args, **kwargs)
class Employee_skill(models.Model):
    employeeId =models.ForeignKey(Employeedata,on_delete=models.CASCADE,null=True,related_name="empskemplo")
    skill=models.ForeignKey(skill,on_delete=models.CASCADE,null=True,related_name="empskslikk")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
class log_entrys_api(models.Model):
    time_entry = models.DateTimeField(auto_now_add=True)
    message = models.CharField()
    trace_back=models.CharField(null=True,blank=True)
    IP_address=models.CharField(blank=True,null=True)
    path=models.CharField(blank=True,null=True)
class ship_type(models.Model):
    shipping_type= models.CharField(max_length=100,blank=True,null=True)
    #transporter--------
class transporters(models.Model):
    transporter= models.CharField(max_length=100,blank=True,null=True)
    mobile=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True,null=True)
    address=models.CharField(blank=True,null=True)
    charges=models.IntegerField(blank=True,null=True)
    

class customer_add(models.Model):
    custome_name= models.CharField(max_length=100,blank=True,null=True)
    mobile= models.CharField(max_length=100,blank=True,null=True)
class bills(models.Model):
    customer=models.ForeignKey(customer_add,on_delete=models.CASCADE,null=True)   
    trans_porter=models.ForeignKey(transporters,on_delete=models.CASCADE,null=True)
    type_shiping=models.ForeignKey(ship_type,on_delete=models.CASCADE,null=True)
    amount=models.IntegerField(blank=True,null=True)
    total_amount=models.CharField(max_length=50,blank=True,null=True)
class final_bills(models.Model):
    customer=models.ForeignKey(customer_add,on_delete=models.CASCADE,null=True)   
    trans_porter=models.ForeignKey(transporters,on_delete=models.CASCADE,null=True)
    type_shiping=models.ForeignKey(ship_type,on_delete=models.CASCADE,null=True)
    amount=models.IntegerField(blank=True,null=True)
    total_amount=models.CharField(max_length=50,blank=True,null=True)


