from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

def  student_details(request,pk):
    stu = Student.objects.get(id=pk)   
    serializer = StudentSerializer(stu)  
    # return JsonResponse(serializer.data)
    json_data =JSONRenderer().render(serializer.data)    
    return HttpResponse(json_data, content_type='application/json')

#All Student Data Display code Query Set
def  student_list(request):
    stu = Student.objects.all()   
    serializer = StudentSerializer(stu,many=True)  
    # return JsonResponse(serializer.data,safe=False)
    json_data =JSONRenderer().render(serializer.data)    
    return HttpResponse(json_data, content_type='application/json')

