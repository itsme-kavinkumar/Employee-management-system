import traceback
import requests
url='http://127.0.0.1:8000/'
def function_log(request,messages,e):
    traceback_info = traceback.extract_tb(e.__traceback__)
    client_ip = request.META['REMOTE_ADDR']
    pathh = request.path
    data={'message':messages,'trace_back':traceback_info,'IP_address':client_ip,'path':pathh}
    postdata = requests.post("{url}/web_log_view/".format(url=url), json=data)
    print('--------8888----------',postdata.status_code)
    #log_data=log_entrys_api.objects.create('message'=messages,'trace_back'=traceback_info,'IP_address'=client_ip,path=pathh)

