import requests
import json

URL = "http://127.0.0.1:8000/"

data = {
    'name':'Gyan Panda',
    'roll':102,
    'city':'Surat'
}
json_data = json.dumps(data) #Convert to Complex data into json data
r = requests.post(url=URL, data=json_data) #send request to another url to createing data
extract_data = r.json() #Accept the responce messages after creating data
print(extract_data)