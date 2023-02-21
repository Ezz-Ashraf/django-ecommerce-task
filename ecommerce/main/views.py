from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Product , Cart , Order , OrderItem
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
import json
from django.db.models import Q

@login_required(login_url="/admin/")
def home(request):  
    return JsonResponse({
    "message": "index endpoint"
    })


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
    
def get_products_ordered(request):
    if request.method == "GET":
        products = Product.objects.all().order_by('price')
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
    
@login_required(login_url="/")
@csrf_exempt
def add_to_cart(request):
    if request.method == "POST":
        productId = request.POST['product']
        quantity = request.POST['quantity']
        product = Product.objects.get(pk=productId)
        if (product):
            #serializedProduct = serializers.serialize('json', product)
            #jsonProduct = json.loads(serializedProduct)
            #productPrice = jsonProduct[0].get("fields").get("price")
            #productName = jsonProduct[0].get("fields").get("name")
            #productCreatedAt = jsonProduct[0].get("fields").get("created_at")
            #productUpdatedAt = jsonProduct[0].get("fields").get("updated_at")
            #productPK = jsonProduct[0].get("fields").get("pk")
            #productInstance = Product(pk=productPK, name=productName, price=productPrice, 
            #                          created_at=productCreatedAt,
            #                          updated_at=productUpdatedAt)
            Cart.objects.create(customer=request.user, product=product, quantity = int(quantity) ,price = int(quantity) * product.price)
            return JsonResponse({
        "message": "Added to cart successfully"
        })

        else:
            return JsonResponse({
        "message": "No Such a product exists"
        })
        
    else:
        return JsonResponse({
        "message": "Request must be Post"
        })
    
@login_required(login_url="/")
@csrf_exempt
def get_cart(request):
    if request.method == "GET":
        cart = Cart.objects.filter(customer=request.user.id)
        data = serializers.serialize('json', cart)
        return JsonResponse({
            "products":json.loads(data)
        })
        
    else:
        return JsonResponse({
        "message": "Request must be gET"
        })

@login_required(login_url="/")
@csrf_exempt
def get_orders(request):
    if request.method == "GET":
        orders = Order.objects.filter(customer=request.user.id)
        data = serializers.serialize('json', orders)
        return JsonResponse({
            "products":json.loads(data)
        })
    else:
        return JsonResponse({
        "message": "Request must be Post"
        })

@login_required(login_url="/")
@csrf_exempt
def get_product_by_name(request):
    if request.method == "GET":
        productName = request.GET.get('q','')
        #orders = Product.objects.filter(name__contains=productName)
        orders = Product.objects.filter(Q(name__contains=productName.lower()) | Q(name__contains=productName.upper()))
        data = serializers.serialize('json', orders)
        return JsonResponse({
            "products":json.loads(data)
        })
    else:
        return JsonResponse({
        "message": "Request must be Post"
        })

@login_required(login_url="/")
@csrf_exempt
def get_orders_details(request):
    if request.method == "GET":
        orders = OrderItem.objects.filter(customer=request.user.id)
        data = serializers.serialize('json', orders)
        return JsonResponse({
            "orders":json.loads(data)
        })
    else:
        return JsonResponse({
        "message": "Request must be Post"
        })

@login_required(login_url="/")
@csrf_exempt
def create_order(request):
    if request.method == "POST":
        cartItems = Cart.objects.filter(customer=request.user.id)
        cartItemsSerialized = serializers.serialize('json', cartItems)
        cartItemsJson = json.loads(cartItemsSerialized)
        itemsSet = set()
        totalPrice = 0
        for item in cartItemsJson:
            product = Product.objects.get(pk=int(item.get("fields").get("product")))
            itemsSet.add(product.name)
            totalPrice += item.get("fields").get("price")
        order = Order(customer=request.user, products=list(itemsSet) , totalPrice=totalPrice)
        order.save()
        for item in cartItemsJson:
            product = Product.objects.get(pk=item.get("fields").get("product"))
            order_item = OrderItem(customer=request.user, product=product, order=order,
                                   quantity=item.get("fields").get("quantity"),price=item.get("fields").get("price") )
            order_item.save()
        Cart.objects.filter(customer=request.user.id).delete()
        return JsonResponse({
            "message": "Order Saved ,Cart is empty now"
        })
    else:
        return JsonResponse({
        "message": "Request must be Post"
        })