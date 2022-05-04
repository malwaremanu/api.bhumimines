from django.http import JsonResponse
import os, datetime, json
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

def index(request):    
    context = {
        'msg' : 'accounts index', 
    }    
    return JsonResponse(context)

def login(request):    
    return render(request, 'accounts/login.html')

@csrf_exempt
def api_login(request): 
    data = json.loads(request.body.decode('utf-8'))
    if data.get('username') == 'admin' and data.get('password') == 'pass':
        msg = 'success'
    else:
        msg = 'error'
    
    context = {
        'msg' : msg
    }    
    return JsonResponse(context)


@csrf_exempt
def api_reset(request): 
    data = json.loads(request.body.decode('utf-8'))
    context = {
        'msg' : 'password reset successfull', 		
        'data' : json.loads(request.body.decode('utf-8'))
    }    
    return JsonResponse(context)