from django.shortcuts import render, redirect
from .forms import RegisterForm, ProductForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from .models import Product
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse
from django.core import serializers
import json
# import json

@login_required(login_url="/admin/")
def home(request):  
    # posts = Post.objects.all()
    return JsonResponse({
    "message": "index endpoint"
    })


@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        #mydata = json.loads(request.body)
        #print(mydata.get('username'))
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({
           "status": True
            })
        else:
            return JsonResponse({
           "status": False
            })
    else:
        return JsonResponse({
        "status": True
        })

@csrf_exempt
def get_username(request):
    if request.method == 'GET':
        print(request.user)
        return JsonResponse({
           "USERNAME logged-in": request.user.id
            })
    else:
        return JsonResponse({
        "status": True
        })
@login_required(login_url="/admin/")
@csrf_exempt
def get_products(request):
    if request.method == "GET":
        products = Product.objects.all()
        data = serializers.serialize('json', products)
        return JsonResponse({
            "products":json.loads(data)
        })
    else:
        return JsonResponse({
        "message": "Request Must be get"
        })
    
@csrf_exempt
def log_out(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({
        "message": "User logged Out Succesfully"
        })
    else:
        return JsonResponse({
        "message": "Request Must be post"
        })
    
@csrf_exempt
def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return JsonResponse({
        "message": "User logged in Succesfully"
        })
        else:
         return JsonResponse({
        "message": "Error occured"
        })
    else:
        return JsonResponse({
        "message": "Request must be Post"
        })