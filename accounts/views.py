from django.http import JsonResponse
import os, datetime, json
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import user

def index(request):    
    context = {
        'msg' : 'accounts index', 
    }    
    return JsonResponse(context)

def login(request):    
    if request.method != 'POST':
        return render(request, 'accounts/login.html')
    data = dict(request.POST)    
    all_users = [x.up() for x in user.objects.all()]
    if (data.get('username')[0] +"####"+ data.get('password')[0]) in all_users:
        print('login successfull')


        for x in user.objects.all():
            x = x.userpass()
            if (data.get('username')[0] == x['username']) and data.get('password')[0] == x['password']:
                request.session['username'] = x['username']
                request.session['password'] = x['password']
                request.session['data'] = x
                return redirect('cashbook_index')
    else:
        print('login failed', data)
        return render(request, 'accounts/login.html',{
            'msg' : 'Either username or password is incorrect.'
        })

def logout(request):    
    del request.session['username'] 
    del request.session['password'] 
    return render(request, 'accounts/login.html',{
            'msg' : 'You have successfully logged out.'
        })

@csrf_exempt
def api_login(request): 
    data = json.loads(request.body.decode('utf-8'))
    all_users = [x.up() for x in user.objects.all()]

    if (data.get('username') +"####"+ data.get('password')) in all_users:
        msg = 'success'
    else:
        msg = 'error'

    context = {
        'msg' : msg,
        "data" : data
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