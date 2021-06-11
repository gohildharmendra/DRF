#validation use only file name serializers.py

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


#Validator
#create first function
def start_with_d(value):
    if value[0].lower() !='d':
        raise serializers.ValidationError('Name should be start with d')

#impliment abou functions like
class StudentSerializer(serializers.Serializer):    
    name = serializers.CharField(max_length=100,validators=[start_with_d])


