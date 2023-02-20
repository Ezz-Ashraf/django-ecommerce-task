from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product  # , OrderItem , Order ,Cart


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["price", "name"]

# class OrderItemForm(forms.ModelForm):
#    class Meta:
#        model = OrderItem
#        fields = ["price", "name"]

# class OrderForm(forms.ModelForm):
#    class Meta:
#        model = Order
#        fields = ["price", "name"]

# class CartForm(forms.ModelForm):
#    class Meta:
#        model = Cart
#        fields = ["customer", "product","quantity","price"]
