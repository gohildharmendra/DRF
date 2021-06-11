from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):    
   # name = serializers.CharField(read_only=True) #read_only single field
    class Meta:
        model = Student
        fields = ['id','url','name','roll','city']
        # read_only_fields = ['name','roll'] # Multiple read_only Method 1        
        # Multiple read_only Method 2
        # extra_kwargs = {'name':{'read_only':True},'roll':{'read_only':True}}

   