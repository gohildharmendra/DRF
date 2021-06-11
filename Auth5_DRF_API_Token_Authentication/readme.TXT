#Token Authentication

#settings.py file changes
INSTALLED_APPS = [
    .................
    'rest_framework',
    'rest_framework.authtoken',
    'api',
]

#Token generate method
....................................................................
#Method1
Go to Admin panel and generate Token
....................................................................

--------------------------------------------------------------------
#Method2
[using Commandline(exist user)]
>python manage.py drf_create_token user1
--------------------------------------------------------------------
____________________________________________________________________
#Method3
#urls.py file add this code
from rest_framework.authtoken.views import obtain_auth_token
path('gettoken/', obtain_auth_token),

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






