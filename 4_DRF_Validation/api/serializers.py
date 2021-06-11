from rest_framework import serializers
from .models import Student

#Validator
def start_with_d(value):
    if value[0].lower() !='d':
        raise serializers.ValidationError('Name should be start with d')

class StudentSerializer(serializers.Serializer):    
    name = serializers.CharField(max_length=100,validators=[start_with_d])
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

    #field level Validation code here
    def validate_roll(self,value):
        if value >=300:
            raise serializers.ValidationError('Seat Full')
        return value

    #Oject level Validation code here
    def validate(self,data):
        name = data.get('name')
        city = data.get('city')
        if name.lower() =='db' and city.lower() != 'una':
            raise serializers.ValidationError({city:'City must be Una'})
        return data



