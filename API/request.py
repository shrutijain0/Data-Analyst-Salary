# -*- coding: utf-8 -*-

import requests 
from data_in import data_input

URL = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {"input": data_input}

r = requests.get(URL,headers=headers, json=data) 

r.json()


