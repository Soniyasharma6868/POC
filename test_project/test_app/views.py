
import datetime
from datetime import date, timedelta
from django.db.models import Max
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import JsonResponse
from test_app.models import *
# Create your views here.
# from e_jewelry_admin_website.models import *
from django.http import HttpResponseRedirect

from django.contrib import messages
# from e_jewelry_admin_website.serializers import *
from django.core import serializers
from .forms import SignUp
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
#from rest_framework_simplejwt.authentication import JWTAuthentication



class user_reg_view(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = user_reg_serilizer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]



# Create your views here.
def user_registration(request):
    if request.method=="POST":
        fm =SignUp(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=SignUp()
    return render(request, 'login/registration.html', {'form':fm})

def user_Dashboard(request):
    # name=request.session['name']='akshay'
    return render(request,'base/base.html')



class Student_View(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Student_serilizer
#    authentication_classes=[JWTAuthentication]
   # permission_classes=[IsAuthenticated]


class Book_View(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = Book_serilizer

class Teacher(ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = teachers_serilizer


