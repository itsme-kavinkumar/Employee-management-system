from django.urls import path
from EMSAPI.view.registerlogin import*
from EMSAPI.view.employeesviews import*
from EMSAPI.view.logweb import*

urlpatterns = [
    path('employees/',EmployeedataView.as_view()),
    path('employees/<int:pk>/',EmployeedataView.as_view()),
    path('employees/<int:pk>/',EmployeedataView.as_view()),
    path('register/',register_view.as_view()),
    path('login/',login_view.as_view()),
    path('attendance_status_data/',attendance_view.as_view()),
    path('web_log_view/',web_log_view.as_view()),
    path('Employee_role/',Employee_role_view.as_view()),
    path('salary_type/',salary_type_view.as_view()),
    path('employees_type/',employees_type_view.as_view()),
    path('type_of_company/',type_of_company_view.as_view()),
    path('company_name/',company_name_view.as_view()),
    path('companytype_filterapi/',companytype_filter_viewapi.as_view()),
    path('companyname_filter/',companyname_filter_view.as_view()),
    path('companyrole_filter/',companyrole_filter_view.as_view()),
    path('multi_filter/',multifilter_view.as_view()),
    path('Employeeskill/',Employee_skill_view.as_view()),
    path('onleave_list/',onleave_list_view.as_view()),
    path('net_salary/',netsalary_view.as_view())
 
  
]