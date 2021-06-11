Session Authentication

List of permission class:
-AllowAny
-IsAuthenticated
-IsAdminUser
-IsAuthenticatedOrReadOnly
-DjangoModelPermissions
-DjangoModelPermissionsOrAnonReadOnly
-DjangoObjectPermissions

#urls.py file add this code
path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))


#rest_framework Authentication and perssions code here (setttings.py file(globally use))
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSIS':['rest_framework.authentication.SessionAuthentication'],    
    'DEFAULT_PERMISSION_CLASSIS':['rest_framework.permissions.IsAuthenticated']
}

#use class Base
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
class StudentModalViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    
    authentication_classes = [SessionAuthentication]    
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser]


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