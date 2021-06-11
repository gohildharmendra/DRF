Filename: settings.py
INSTALLED_APPS = [
    ................ 
    'rest_framework',
    'api',
]

Filename: apiData.py
URL = "http://127.0.0.1:8000/studentapi/" #for Function base view
URL = "http://127.0.0.1:8000/student_api/" #For Classbase view


Filename: urls.py
path('studentapi/', views.student_api),#For Function base view
path('student_api/', views.StudentAPI.as_view()),#ForClass base view


Filename: views.py
#FunctionBase Code start here
@csrf_exempt
def student_api(request):
................
#FunctionBase Code End

# ClassBase view code Start here
@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
.......................
# ClassBase view code End

Filename: models.py
from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=200)

Filename: admin.py
from .models import Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id', 'name','roll','city']


Filename: serializer.py
from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.Serializer):    
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=200)

    def create(self,validated_data):
        return Student.objects.create(**validated_data)  

    def update(self,instance,validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance







