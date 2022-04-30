from django.http import JsonResponse
import os, datetime

def index(request):
    
    context = {
        'msg' : 'accounts index', 
    }    
    return JsonResponse(context)