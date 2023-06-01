
import requests

url = 'http://127.0.0.1:5000/api'
# input_time1=1519842782
# input_time2=1520952783

params = {'input_time1':1519842782,'input_time2':1520952783}
r = requests.get(url,data=params)

print(r.text)