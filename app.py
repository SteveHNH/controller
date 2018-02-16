import requests
import json
import os

from time import sleep


URL = os.environ.get('URL')

requests.post(URL, json=json.dumps('{"test": "value"}'))
