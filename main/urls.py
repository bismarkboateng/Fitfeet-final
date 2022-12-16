from django.urls import path 
from . import views 


urlpatterns = [
    path("", views.index, name="home"),
    path("products/<int:pk>/order/", views.SingleProduct, name="single"),
    path("accounts/login/", views.LoginView.as_view(), name="login"), 
    path("accounts/signup/", views.SignupView.as_view(), name="signup"),
    path("accounts/logout/", views.Logout, name="logout")
]
