#Functionbase Authentication

#add code views.py files
#namespace import
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

#Add Authentication decorators
@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def api_data(request, pk=None):
    if request.method == 'GET':
    ...............................
    ..............
    ......
    ...
    ..
    .

