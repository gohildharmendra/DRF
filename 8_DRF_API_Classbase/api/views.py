from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView


class api_data(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stud = Student.objects.get(id=id)
            serializer = StudentSerializer(stud)
            return Response(serializer.data)
        stud = Student.objects.all()
        serializer = StudentSerializer(stud, many=True)
        return Response(serializer.data)

    def post(self, request,format=None, pk=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()    
            return Response({'msg':'Record inserted successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None, pk=None):
        id = pk    
        stud = Student.objects.get(pk=id)
        serializer = StudentSerializer(stud, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Record Updated successfully'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, format=None, pk=None):
        id = pk    
        stud = Student.objects.get(pk=id)
        serializer = StudentSerializer(stud, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Record Updated successfully'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
         
    def delete(self, request, format=None, pk=None):
        id = pk    
        stud = Student.objects.get(pk=id)
        stud.delete()
        return Response({'msg':'Record Deleted successfully'})       
  

   
