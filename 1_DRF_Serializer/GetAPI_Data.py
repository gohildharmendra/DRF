import requests
#Set the URL
URL = "http://127.0.0.1:8000/stuinfo/1"
# get API data
getdata = requests.get(url = URL)
#Convert to Json
data = getdata.json()
#print the data
print(data)

