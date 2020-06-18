from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import requests
from subprocess import run,PIPE
# Create your views here.

def index(request):
    return render(request,'index.html') 

def external(request):
    ip = request.POST.get('param')
    print(ip)
    ch = request.POST.get('param')

    out = run([sys.executable,"//Users//964167//Documents//Splunk//Sri/scaner.py",ip,ch],shell=False,stdout=PIPE)
    print(out)
    return render(request,'index.html')
