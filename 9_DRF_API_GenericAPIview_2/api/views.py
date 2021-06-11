# GenericAPIView and Model Mixin
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from  rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

#Not required pk Create and list
class student_APIList_create(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
   
#Required pk Update, Retive, Delete API Data
class student_update_delete_retive(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request, *args, **kwargs):

        return self.retrieve(request, *args, **kwargs)
    def post(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    


    
