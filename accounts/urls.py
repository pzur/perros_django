from django.urls import path
from . import views 


urlpatterns = [

    path('register/', views.registerPage, name= "register"),
    path('login/', views.loginPage, name = "login"),

    path('', views.home, name= "home"),
    path('product/', views.product, name= "product"),
    path('customer/', views.customer),
]