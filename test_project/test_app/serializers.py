from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *


class user_reg_serilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class Book_serilizer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = ['id','Book_name','Student','teachers']

class Student_serilizer(serializers.ModelSerializer):
    book = Book_serilizer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = ['id','Name','College_name','Year','book']

class teachers_serilizer(serializers.ModelSerializer):
    book = Book_serilizer(many=True, read_only=True)
    class Meta:
        model = Teachers
        fields = ['id','Name','Deparment','Year','book']
