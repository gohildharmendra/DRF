import requests
import json

URL = "http://127.0.0.1:8000/student_api/" #For Classbase view

def get_data(id = None):
    data = {}
    if id != None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data=json_data)
    data = r.json()
    print(data)
        
get_data()
get_data(2)

def add_data():
    data = {
        'name':'db',
        'roll':105,
        'city':'una'
    }
    json_data = json.dumps(data)
    r = requests.post(url = URL, data=json_data)
    data = r.json()
    print(data)
add_data()

def update_data():
    data = {
        'id':1,
        'name':'Ramesh',
        'roll':303,        
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL, data=json_data)
    data = r.json()
    print(data)
# update_data()

def delete_data():
    data = { 'id':5 }
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data=json_data)
    data = r.json()
    print(data)
# delete_data()


