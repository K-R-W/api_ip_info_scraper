import requests
import json
def getdata():
    
    url = 'http://ipwhois.app/json/106.195.5.27'
    response = requests.request("GET",url)
    data = json.loads(response.text)
    dic={}
    dic['ip']=data['ip']
    dic['org']=data['org']
    dic['city'] = data['city']
    dic['country'] = data['country']
    dic['region'] = data['region']
    dic['lat'] = data['latitude']
    dic['lon'] = data['longitude']

    return dic
    
    

