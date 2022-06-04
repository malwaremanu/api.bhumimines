from django.http import JsonResponse
from django.shortcuts import redirect, render
import os, datetime

from project.login import check_login

def index(request):        
    check_login(request)
    context = {
        'msg' : 'success', 
        'page' : 'main page.', 
    }    
    return render(request, 'cashbook/base.html', context)

def add(request):        
    check_login(request)
    context = {
        'msg' : 'success', 
        'page' : 'main page.', 
    }    
    return render(request, 'cashbook/add.html', context)
