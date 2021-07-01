import requests
import json
import time

webhook_url ='http://127.0.0.1:5000/webhook'

data = { 'name': 'Eric',
         'favorite show': 'Code Geass' }

time .sleep(5)

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})