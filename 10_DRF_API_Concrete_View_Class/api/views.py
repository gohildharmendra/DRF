from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

#Disaply all list single class
class student_list(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# insert data single class
class student_create(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Update data single class
class student_update(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#delete data single class
class student_delete(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


#All list and insert data works this class[both work]
class student_listCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer  

#Retrive Update and Delete work this class
class student_retrive_update_delete(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer   

