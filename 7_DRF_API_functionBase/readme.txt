if you run apiData.py file
than
views.py file some change
id = request.data.get('id') #uncomment
# id = pk #comment this line


if you run Direct Browser
than
#id = request.data.get('id') #comment this line
id = pk #remove_comment this line

#use this files
model.py
admin.py
serializers.py
views.py
urls.py

#other file[outside project]
apiData.py