from django.contrib import admin
from django.urls import path
from task import views 
from views import *

urlpatterns = [  
  path("",views.test,name="task"),
  path("excel/",[views.Task_dataTOexcel,views.user_dataTOexcel])
]
  