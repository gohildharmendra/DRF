from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def api_data(request, pk=None):
    if request.method == 'GET':
        # id = request.data.get('id')
        id = pk
        if id is not None:
            stud = Student.objects.get(id=id)
            serializer = StudentSerializer(stud)
            return Response(serializer.data)
        stud = Student.objects.all()
        serializer = StudentSerializer(stud, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()    
            return Response({'msg':'Record inserted successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT': #All Field Update
        # id = request.data.get('id')       
        id = pk    
        stud = Student.objects.get(pk=id)
        serializer = StudentSerializer(stud, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Record Updated successfully'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':#Partial field update
        # id = request.data.get('id')       
        id = pk    
        stud = Student.objects.get(pk=id)
        serializer = StudentSerializer(stud, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Record Updated successfully'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
         
    if request.method == 'DELETE':
        # id = request.data.get('id')   
        id = pk    
        stud = Student.objects.get(pk=id)
        stud.delete()
        return Response({'msg':'Record Deleted successfully'})
   
