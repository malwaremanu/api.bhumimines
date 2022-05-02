from django.http import JsonResponse
import os, datetime

def index(request):    
    context = {
        'msg' : 'success', 
        'page' : 'main page.', 
    }    
    return JsonResponse(context)

def rs(request):
    os.system('pip install -r req.txt')
    os.system("echo '' > tmp/restart.txt")
    context = {
        'msg' : 'success', 
        'git' : 'updated', 
        'time' : str(datetime.datetime.now())
    }    
    return JsonResponse(context)
