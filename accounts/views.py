from django.http import JsonResponse
import os, datetime
from django.views.decorators.csrf import csrf_exempt

def index(request):    
    context = {
        'msg' : 'accounts index', 
    }    
    return JsonResponse(context)

@csrf_exempt
def login(request):    
    context = {
        'username' : 'admin', 
		'password' : 'pass', 		
    }    
    return JsonResponse(context)