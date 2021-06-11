Basic Authentication

List of permission class:
-AllowAny
-IsAuthenticated
-IsAdminUser
-IsAuthenticatedOrReadOnly
-DjangoModelPermissions
-DjangoModelPermissionsOrAnonReadOnly
-DjangoObjectPermissions

#rest_framework Authentication and perssions code here (setttings.py file(globally use))
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSIS':['rest_framework.authentication.BasicAuthentication'],    
    'DEFAULT_PERMISSION_CLASSIS':['rest_framework.permissions.IsAuthenticated']
}

#use class Base
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
class StudentModalViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    
    authentication_classes = [BasicAuthentication]    
    permission_classes = [IsAuthenticated]


#AllowAny globally override code here 
class StudentModalViewSet1(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer  
    #globally override code here  
    authentication_classes = [BasicAuthentication]    
    permission_classes = [AllowAny]

#Only Staff member use this API
class StudentModalViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    
    authentication_classes = [BasicAuthentication]    
    permission_classes = [IsAdminUser]