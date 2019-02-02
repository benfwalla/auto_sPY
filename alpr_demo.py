#!/usr/bin/python
import requests
import base64
import json

# Insert a path to an image here (ex: 'images/car2.jpg')
IMAGE_PATH = 'IMAGE PATH HERE'

# The secret key for our OpenALPR account.
# Look in our Slack channel to find this key
SECRET_KEY = 'SECRET KEY HERE'

with open(IMAGE_PATH, 'rb') as image_file:
    img_base64 = base64.b64encode(image_file.read())

url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' % (SECRET_KEY)
r = requests.post(url, data = img_base64)

print(json.dumps(r.json(), indent=2))