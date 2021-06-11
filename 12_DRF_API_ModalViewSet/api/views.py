from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student


class StudentModalViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
        
# ReadOnly API
class StudentReadonlyModalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
