from django.http import JsonResponse
import os, datetime

def index(request):
    
    os.system("echo '' > tmp/restart.txt")
    
    context = {
        'msg' : 'success', 
        'time' : str(datetime.datetime.now())
    }    
    return JsonResponse(context)