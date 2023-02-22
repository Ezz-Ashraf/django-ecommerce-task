# django-ecommerce-task

Task for e-commerce using django Rest Framework

# Steps to run the Project
## 1) using Django commands
### prerequistes as mentioned in requirements.txt:
### Django
### (psycopg2-binary for linux) or (psycopg2 for windows)
### djangorestframework
### The steps:
### 1- Navigate to ecommerce folder
### 2-type in terminal or cmd the following command: 
### python manage.py runserver
### 3-The Project will be available on port 8000 



## 2- using docker image:
### The steps:
### 1- Navigate to ecommerce folder
### 2-type command ( docker build -t django_img .) to build image
### 3-type command ( docker run -p 8000:8000 django_img )To run the container
### 4-The Project will be available on port 8000 

## 2- using docker-compose:
### The steps:
### 1- Navigate to repositry folder
### 2-type command (docker-compose up) to run the container directly
### 3- if there is any issue in permissions for docker(Most probably on Linux) type the following commands in order:
### sudo groupadd docker
### sudo usermod -aG docker $USER
### newgrp docker
### 4- to stop the container type (docker-compose down --rmi all  -v ) /rmi => remove images made by the composer , -v => remove volumes made by the compose

# Available endpoints in the project

## 1) "/sign-up" , post request required for creating a new user
### Takes 4 arguments (username, email, password1, password2)
### It's preferred that username starts with Capital Letter , email can be @test.com  , password contains special character

## 2) "/products-ordered" get request to show Prducts (Ordered By Price) which are added from the admin panel only

## 3) "/products" , get request to show Prducts (Ordered By Creation date) which are added from the admin panel only

## 4) "/get-product/?q=ca" , get request with query parameter q to search for product name ordered by Price for example b gets Mobile and Book Non-case Sensitive and position of letters don't matter

## 5) "/add-to-cart" , post request takes two fields(product,quantity) which is product id(PK) and quantity wanted

## 6) "/get-cart" , get request to show the user's cart

## 7) "/create-order" , post request to create order with no wanted fields

## 8) "/get-orders" , get request to get orders with name of Products and the date 

## 9) "/get-orders-details" , get request to get orders items with the quantity and their total price


## 10) "/logout" Post request with no fields

## 11) "/login", post request with username and password field


## To add Product create a superuser and go to /admin and login with user created and add Product with name and Price
# Unit testing:
## using django unittest.TestCase in main/tests.py
## to run navigate to ecommerce and type python(python3 for linux) manage.py test

# Database used is postgresql