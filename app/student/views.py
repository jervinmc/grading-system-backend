from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Student
from .serializers import StudentSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import GetUserSerializer
import pusher
from decouple import config
class StudentView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Student.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=StudentSerializer
    
    def list(self,request):
        item = Student.objects.filter(kinder_level = request.GET['kinder_level'])
        item = StudentSerializer(item,many=True)
        return Response(data=item.data)


