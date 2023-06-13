from django.urls import path
from EMS.view.employees import*
from EMS.view.signuplogin import*

urlpatterns = [
    path('',signup,name="signup"),
    path("login_user/",login_user, name="login_user"),
    path("logout_use/r",logout_user, name="logout_user"),
    path('employee_page/', homepage,name="employee-page"),
    path('newemployee.html/',newemployee,name="newemployee"),
    path('emp-list/',emplist,name="emplist"),
    path('employeelist.html/',employeelist,name="employee"),
    path('employeenew/',insertemployee,name="employeenew"),
    path('showpage/', employeelist, name='showpage'),
    path('edit/<int:pk>',Editpage, name='edit'),
    path('update/<int:pk>', UpdateData, name='update'),
    path('delete/<int:pk>',Deletedata, name='delete'),  
    path('attandance.html',attandance,name="empattandance2"),
    path('leave-status/<int:pk>',leave_status, name="leave_status"),
    path('salary.html/',empsalary, name='salary'),
    path('checkin-checkout/<int:pk>/',checkin_checkout,name="checkin_checkout"),
    path('errorpage/',error_page,name="error_page"),
    path('companytype_filter/',company_type_filter,name="companytype_filter"),
    path('company_name_filter/',company_name_filter,name="company_name_filter"),
    path('company_role_filter/',company_role_filter,name="company_role_filter"),
    path('multi_filter/',multi_filter,name="multi_filter")    
]