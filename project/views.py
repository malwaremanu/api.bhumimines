from django.http import JsonResponse
import os, datetime

def index(request):
    context = {
        'msg' : 'success', 
        'pages' : 'first page'
    }    
    return JsonResponse(context)