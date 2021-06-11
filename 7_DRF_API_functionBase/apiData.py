import requests
import json


URL = "http://127.0.0.1:8000/studentapi/" #For Functionbase

def get_data(id = None):
    data = {}
    if id != None:
        data = {'id':id}    
    json_data = json.dumps(data)
    headers = {'Content-Type':'application/json'}
    r = requests.get(url = URL, headers=headers, data=json_data)
    data = r.json()
    print(data)
        
get_data()
get_data(2)

def add_data():
    data = {
        'name':'Rakesh',
        'roll':105,
        'city':'Una'
    }
    headers = {'Content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url = URL,headers=headers, data=json_data)
    data = r.json()
    print(data)
# add_data()

def update_data():
    data = {
        'id':8,
        'name':'Ranjitsinh',
        'roll':106,
        'city':'motha',        
    }
    headers = {'Content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url = URL, headers=headers, data=json_data)
    data = r.json()
    print(data)
# update_data()

def delete_data():
    data = { 'id':9 }
    json_data = json.dumps(data)
    headers = {'Content-Type':'application/json'}
    r = requests.delete(url = URL, headers=headers, data=json_data)
    data = r.json()
    print(data)
# delete_data()


