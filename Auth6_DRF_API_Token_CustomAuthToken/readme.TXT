#CustomeAuthToken generate

#settings.py file changes
INSTALLED_APPS = [
    .................
    'rest_framework',
    'rest_framework.authtoken',
    'api',
]

#Create one file auth.py
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token,created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id':user.pk,
            'email':user.email,
            'FirstName': user.first_name,
            'LastName': user.last_name
        })


#urls.py file add this code
from api.auth import CustomAuthToken
 path('gettoken/', CustomAuthToken.as_view()),

#submethod1
#Go to Thunder Client or Postman
POST
http://127.0.0.1:8000/gettoken/

Body > json
{
    "username":"admin",
    "password":"admin"
}
----
OR
#submethod2
#Add Package
>pip install httpie
#Run command
>http POST http://127.0.0.1:8000/gettoken/ username="admin" password="admin"
-----
__________________________________________________________________________
#output
{
    "FirstName": "Gohil",
    "LastName": "DB",
    "email": "gohildb.dev@gmail.com",
    "token": "32d7994d56d98bc752bad60297ef5d89cea0eb82",
    "user_id": 1
}





