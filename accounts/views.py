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
    if request.method != 'POST':
        return render(request, 'accounts/login.html')
    data = dict(request.POST)
    print(data)
    if data['username'][0] == 'asd@asd.com' and data['password'][0] == 'password':
        print('login successfull')
        request.session['username'] = data['username'][0]
        request.session['password'] = data['password'][0]        
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