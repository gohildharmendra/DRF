# GenericAPIView and Model Mixin
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from  rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


class student_list(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        
class student_create(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class student_retive(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class student_update(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def post(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class student_delete(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
