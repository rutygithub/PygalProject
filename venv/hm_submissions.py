import requests

from operator import itemgetter

url = 'https://www.sina.com.cn/'
r = requests.get(url)
print("Status code:", r.status_code)