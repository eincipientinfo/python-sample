from django.contrib import admin  
from django.urls import path  
from myapp import views

app_name = 'myapp'
  
#Use as a url 

urlpatterns =[  
    path('hello/', views.hello),
    path('index/', views.index),
    path('form1/', views.form1),
    path('ssession',views.setsession),  
    path('gsession',views.getsession),
    path('scookie',views.setcookie),  
    path('gcookie',views.getcookie),
]  