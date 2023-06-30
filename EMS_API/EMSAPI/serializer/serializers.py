from rest_framework import serializers
from EMSAPI.model.employeemodels import*
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from rest_framework.validators import UniqueValidator
class Employeedataserializer(serializers.ModelSerializer):
    role_name=serializers.ReadOnlyField(source='Role.Employee_role')
    class Meta:
        model = Employeedata
        fields= ('id','Name','DOB','Gender','Bloodgroup',
                 'Datejoininng','Email','Mobile','Address','Role','Salarytype','employee_type','Workinghour',
                 'Overtime','Casualleave','Basicsalary','HRA','MedicalAllowance','Coveneyance','General','Professionaltax',
                 'RD','PF','ESI','leave_count','present_count','on_leave','Netsalary','Checkin_status','Check_in',
                 'Check_out','WorkedHour','Date','role_name','created_by')
class attendanceserializer(serializers.ModelSerializer):
    role_name=serializers.ReadOnlyField(source='Role.Employee_role')
    class Meta:
        model = Employeedata
        fields= ('id','Name','DOB','Gender','Bloodgroup',
                 'Datejoininng','Email','Mobile','Address','Role','Salarytype','employee_type','Workinghour',
                 'Overtime','Casualleave','Basicsalary','HRA','MedicalAllowance','Coveneyance','General','Professionaltax',
                 'RD','PF','ESI','leave_count','present_count','on_leave','Netsalary','Checkin_status','Check_in',
                 'Check_out','WorkedHour','Date','role_name','created_by')

class Employee_role_serializer(serializers.ModelSerializer):
    class Meta:
        model=Employee_role
        fields='__all__'
class salary_type_serializer(serializers.ModelSerializer):

    class Meta:
        model = salary_type
        fields= '__all__' 
class employees_type_serializer(serializers.ModelSerializer):

    class Meta:
        model = employees_type
        fields= '__all__' 

class log_entrys_api_serializer(serializers.ModelSerializer):
    class Meta:
        model=log_entrys_api
        fields= '__all__' 
    
class type_of_company_serializer(serializers.ModelSerializer):
    class Meta:
        model=type_of_company
        fields= '__all__' 
class company_name_serializer(serializers.ModelSerializer):
    class Meta:
        model=company_name
        fields= '__all__' 
class skill_serializer(serializers.ModelSerializer):
    class Meta:
        model=skill
        fields= '__all__' 
class shipingtype_serializer(serializers.ModelSerializer):
    class Meta:
        model=ship_type
        fields= '__all__' 
class transporters_serializer(serializers.ModelSerializer):
    class Meta:
        model=transporters
        fields= '__all__' 
class customer_add_serializer(serializers.ModelSerializer):
    class Meta:
        model=customer_add
        fields= '__all__' 
class bills_serializer(serializers.ModelSerializer):
    customer_name=serializers.ReadOnlyField(source='customer.custome_name')
    trans_porter_name=serializers.ReadOnlyField(source='trans_porter.transporter')
    type_shiping_name=serializers.ReadOnlyField(source='type_shiping.shipping_type')
    
    class Meta:
        model=bills
        fields= ('id','customer','trans_porter','type_shiping','amount','total_amount','customer_name','trans_porter_name','type_shiping_name')
class final_bills_serializer(serializers.ModelSerializer):
    customer_name=serializers.ReadOnlyField(source='customer.custome_name')
    trans_porter_name=serializers.ReadOnlyField(source='trans_porter.transporter')
    type_shiping_name=serializers.ReadOnlyField(source='type_shiping.shipping_type')
    class Meta:
        model=final_bills
        fields= fields= ('id','customer','trans_porter','type_shiping','amount','total_amount','customer_name','trans_porter_name','type_shiping_name')

#----------PURCHASE_____________________
class purchase_serializer(serializers.ModelSerializer):
    supplier_name=serializers.ReadOnlyField(source="supplier.supplier_name")
    product_name=serializers.ReadOnlyField(source="product.product_name")
    product_price=serializers.ReadOnlyField(source="product.price")
    class Meta:
        model=purchase_order
        fields= fields= ('id','supplier','quantity','product','amount','remaining_qty','date','supplier_name','product_name','product_price')
class supplier_serializer(serializers.ModelSerializer):
    class Meta:
        model=supplier
        fields= '__all__' 
class product_serializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields= '__all__' 
class temprary_purchase_serializer(serializers.ModelSerializer):
    supplier_name=serializers.ReadOnlyField(source="supplier.supplier_name")
    product_name=serializers.ReadOnlyField(source="product.product_name")
    class Meta:
        model=temrary_purchase_order
        fields= fields= ('id','supplier','quantity','product','amount','date','supplier_name','product_name')
class temprary_GRN_serializer(serializers.ModelSerializer):
    supplier_name=serializers.ReadOnlyField(source="supplier.supplier_name")
    product_name=serializers.ReadOnlyField(source="product.product_name")
    product_price=serializers.ReadOnlyField(source="product.price")
    class Meta:
        model=tempraryGRN
        fields= fields= ('id','supplier','quantity','product','amount','date','supplier_name','product_name','product_price','purchaseid')
class final_GRN_serializer(serializers.ModelSerializer):
    supplier_name=serializers.ReadOnlyField(source="supplier.supplier_name")
    product_name=serializers.ReadOnlyField(source="product.product_name")
    product_price=serializers.ReadOnlyField(source="product.price")
    class Meta:
        model=finalGRN
        fields= fields= ('id','supplier','quantity','product','amount','date','supplier_name','product_name','product_price','purchaseid')