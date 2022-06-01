import requests
import json

URL = "http://localhost:8000/add"

data = {
    'item_name':"test",
    'cataegory':"testcat",
    'price':50
}

jsondata = json.dumps(data)
r = requests.post(url=URL,data=jsondata)
data = r.json()
print(data)