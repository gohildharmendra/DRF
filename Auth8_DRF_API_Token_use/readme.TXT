#

#settings.py file changes
INSTALLED_APPS = [
    .................
    'rest_framework',
    'rest_framework.authtoken',
    'api',
]

#Add Package
>pip install httpie

#views.py file
#import
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

#code
 authentication_classes = [TokenAuthentication]  
 permission_classes = [IsAuthenticatedOrReadOnly]
 #Run Command
 http http://127.0.0.1:8000/student_api/
 ........................................
 authentication_classes = [TokenAuthentication]    
 permission_classes = [IsAuthenticated]
 #Run Command
 http http://127.0.0.1:8000/student_api/ "Authorization:Token e5f1680c6aa7c724320dfa98b1a4bb3612871cf7"


