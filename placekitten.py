import shutil

import requests

url = 'http://placekitten.com/g/200/300'
response = requests.get(url, stream=True)
with open('img.png', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response