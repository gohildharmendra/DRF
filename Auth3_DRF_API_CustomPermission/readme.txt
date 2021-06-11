#Session Authentication using Custom Permission

#Create File custompermissions.py
from rest_framework.permissions import BasePermission
class MyPermission(BasePermission):
    def has_permission(self,request,view):
        if request.method == 'GET':
            return True
        return False


#views.py file code
from .custompermissions import MyPermission

permission_classes = [MyPermission]


