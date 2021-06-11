from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissions

class StudentModalViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    
    # authentication_classes = [SessionAuthentication]    
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [DjangoModelPermissions]


# #AllowAny globally override code here 
# class StudentModalViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer  
#     #globally override code here  
#     authentication_classes = [BasicAuthentication]    
#     permission_classes = [AllowAny]

# #Only Staff member use this API
# class StudentModalViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer    
#     authentication_classes = [BasicAuthentication]    
#     permission_classes = [IsAdminUser]


# ReadOnly API
class StudentReadonlyModalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
