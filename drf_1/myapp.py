import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def post_data():
    data = {
    'name' : 'ayushi',
    'roll': 110,
    'city': 'indore'
    }
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(data)
# post_data()

def update_data():
    data = {
    'id' : 3,
    'name': 'Vishakha',
    'roll': 103,
    'city': 'jaipur'
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)

update_data()



def post_data():
    data = {
        'name' : 'shivani',
        'roll': 103,
        'city': 'indore'
    }

    json_data = json.dumps(data)
    r= requests.post(url = URL, data = json_data)
    data = r.json()
    # print(data)


def get_data(id = None):
    data = {}
    if id is not None :
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(data)
# get_data(4)


def delete_data(id = None):
    data = {'id':4}
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)
# delete_data()

