from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth
from django.contrib.auth.models import User 
from django.contrib import messages
from .models import Product

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def Logout(reqeust):
    auth.logout(reqeust)
    return redirect('home')






def SingleProduct(request, pk):
    single_product = Product.objects.get(id=pk)

    ctx = {
        'product': single_product
    }

    return render(request, 'product.html', ctx)





class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/login.html')


    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")


        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, "Login Success!")
            return redirect("home")
            
        else:
            messages.info(request, "Invalid Credentials!")
            return redirect("login")


class SignupView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/signup.html')


    def post(self, request, *args, **kwargs):
        firstname = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        Confirm_password = request.POST.get('confirm_password')

        if password == Confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken !')
                return redirect('signup')

            else:
                user = User.objects.create_user(username=username, first_name=firstname, email=email, password=password)
                user.save()
                messages.info(request, "Account created successfully!")
                return redirect('login')

        else:
            messages.info(request, 'Passwords Don"t Match!')
            return redirect('signup')

        