#!/usr/bin/python

import requests
import base64
import json

# Sample image file is available at http://plates.openalpr.com/ea7the.jpg
IMAGE_PATH = 'car2.jpg'
SECRET_KEY = 'sk_0825613da3ca63a72b628884'

with open(IMAGE_PATH, 'rb') as image_file:
    img_base64 = base64.b64encode(image_file.read())

url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' % (SECRET_KEY)
r = requests.post(url, data = img_base64)

print(json.dumps(r.json(), indent=2))