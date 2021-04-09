from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . import api

def index(request):
    return render(request,'api_qr.html')

def response(request):
    if(request.method == 'POST'):
        resp = api.getdata()
        resp['name']=request.POST['name']
        return render(request,'api_resp.html',resp)
    else:
        return HttpResponse("<h1>This is a bad way to access page. go through <a href='127.0.0.1:8080/api_ip'>/api_ip</a></h1>")