import traceback
from EMSAPI.model.employeemodels import*
def function_api_log(request,messages,e):
    traceback_info = traceback.extract_tb(e.__traceback__)
    client_ip = request.META['REMOTE_ADDR']
    pathh = request.path
    log_data=log_entrys_api.objects.create(message=messages,trace_back=traceback_info,IP_address=client_ip,path=pathh)

