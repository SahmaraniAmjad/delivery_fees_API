# we will send a request from this file

import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "cart/32", {"cart_value": 10, "delivery_distance": 121, "number_of_items": 2, "time": "2021-01-16T13:00:00Z"})
print(response.json())
input()

response = requests.get(BASE + "cart/32")
print(response.json())
