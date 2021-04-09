import requests
import json
def getdata():
    
    url = 'http://ipinfo.io/json'
    response = requests.request("GET",url)
    data = json.loads(response.text)
    dic={}
    dic['ip']=data['ip']
    dic['org']=data['org']
    dic['city'] = data['city']
    dic['country'] = data['country']
    dic['region'] = data['region']
    loc = list(float(x) for x in data['loc'].split(','))
    dic['lat'] = loc[0]
    dic['lon'] = loc[1]

    return dic
    
    

