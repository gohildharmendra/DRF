from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .serializers import StudentSerializer
from .models import Student


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        stud = Student.objects.all()
        serializer = StudentSerializer(stud, many=True)
        return Response(serializer.data)
        

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stud = Student.objects.get(id=id)
            serializer = StudentSerializer(stud)
            return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()    
            return Response({'msg':'Record inserted successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        id = pk    
        stud = Student.objects.get(pk=id)
        serializer = StudentSerializer(stud, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Record Updated successfully'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request,pk):
        id = pk    
        stud = Student.objects.get(pk=id)
        serializer = StudentSerializer(stud, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Record Updated successfully'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
         
    def destroy(self, request, pk):
        id = pk    
        stud = Student.objects.get(pk=id)
        stud.delete()
        return Response({'msg':'Record Deleted successfully'})       
  

   
