from django.http import JsonResponse
from django.shortcuts import redirect, render
import os, datetime

def index(request):  
    print(request.session.get('username'))  
    print(request.session.get('username'))  
    context = {
        'msg' : 'success', 
        'page' : 'main page.', 
    }    
    return render(request, 'project/base.html', context)

def rs(request):
    os.system('pip install -r requirements.txt')
    os.system("echo '' > tmp/restart.txt")
    context = {
        'msg' : 'success', 
        'git' : 'updated', 
        'time' : str(datetime.datetime.now())
    }    
    return JsonResponse(context)