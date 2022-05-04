from django.http import JsonResponse
from django.shortcuts import redirect, render
import os, datetime

def index(request):    
    context = {
        'msg' : 'success', 
        'page' : 'main page.', 
    }    
    return render(request, 'cashbook/base.html', context)