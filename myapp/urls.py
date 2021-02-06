from django.contrib import admin
from django.urls import path,include
from myapp import views


urlpatterns = [
    path('', views.index,name="home"),
    path('login', views.loginfun,name="login"),
    path('formd', views.formfun,name="formfun")
    
    
   

]
