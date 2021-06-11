from rest_framework import serializers
from .models import Student




class StudentSerializer(serializers.ModelSerializer):
    
   # name = serializers.CharField(read_only=True) #read_only single field
    class Meta:
        model = Student
        fields = ['name','roll','city']
        # read_only_fields = ['name','roll'] # Multiple read_only Method 1        
        # Multiple read_only Method 2
        # extra_kwargs = {'name':{'read_only':True},'roll':{'read_only':True}}

    #1)Function base validation
    #Validator Function enter name start with first letter d
    def start_with_d(value):
        if value[0].lower() !='d':
            raise serializers.ValidationError('Name should be start with d')
    name = serializers.CharField(validators=[start_with_d])
    
    #2)field level Validation code here
    def validate_roll(self,value):
        if value >=300:
            raise serializers.ValidationError('Seat Full')
        return value

    #3)Oject level Validation code here
    def validate(self,data):
        name = data.get('name')
        city = data.get('city')
        if name.lower() =='db' and city.lower() != 'una':
            raise serializers.ValidationError({city:'City must be Una'}) 
        return data

    

