from django.db import models

# Create your models here.
class type_of_company(models.Model):
    company_type=models.CharField(max_length=40,blank=True, null=True)
    
class company_name(models.Model):
    company_name=models.CharField(max_length=40,blank=True, null=True)
    company_type=models.ForeignKey(type_of_company,on_delete=models.CASCADE,null=True,related_name="cmpmytyp")

class Employee_role(models.Model):
    Employee_role=models.CharField(max_length=40,blank=True, null=True)
    company_name=models.ForeignKey(company_name,on_delete=models.CASCADE,null=True)

class salary_type(models.Model):
    salary_type=models.CharField(max_length=40,blank=True, null=True)

class employees_type(models.Model):
    employees_type=models.CharField(max_length=40,blank=True, null=True)

class skill(models.Model):
    Skill=models.CharField(max_length=100)
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
    
    Checkin_status= models.BooleanField(blank=True, null=True)
    Check_in = models.DateTimeField( help_text="Time in", null=True, blank=True)

    Check_out = models.DateTimeField(blank=True, help_text="Time out", null=True)
    WorkedHour = models.IntegerField(default=0)

    Date=models.CharField(max_length=50,blank=True, null=True)
       
    def __str__(self):
        return self.Name
    
class Employee_skill(models.Model):
    employeeId =models.ForeignKey(Employeedata,on_delete=models.CASCADE,null=True,related_name="empskemplo")
    skill=models.ForeignKey(skill,on_delete=models.CASCADE,null=True,related_name="empskslikk")

class log_entrys_api(models.Model):
    time_entry = models.DateTimeField(auto_now_add=True)
    message = models.CharField()
    trace_back=models.CharField(null=True,blank=True)
    IP_address=models.CharField(blank=True,null=True)
    path=models.CharField(blank=True,null=True)
