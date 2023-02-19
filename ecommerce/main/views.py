from django.shortcuts import render, redirect
from .forms import RegisterForm, ProductForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def home(request):  
    # posts = Post.objects.all()
    return "hello user"

@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
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

