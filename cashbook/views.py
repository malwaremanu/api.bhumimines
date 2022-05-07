from django.http import JsonResponse
from django.shortcuts import redirect, render
import os, datetime

def check_login(request):
    if not request.session:
        return redirect('accounts_login')

def index(request):        
    check_login(request)
    context = {
        'msg' : 'success', 
        'page' : 'main page.', 
    }    
    return render(request, 'cashbook/base.html', context)
