import json
from datetime import datetime
import urllib3
import groupmebotsecrets #has all the secrets




def lambda_handler(event, context):
    http = urllib3.PoolManager()
    
    # TODO implement
    content = json.loads(event['body'])
    print(content)
    try:
        imgUrl = content['attachments'][0]['url']
        print(imgUrl)
    except:
        imgUrl = ""
    
    ts  = content['created_at'] - 21600
    time = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print(time)
    data = {}
    #data["content"] = str(content['name']).split(" ")[0] +": " + str(time)
    data["username"] = "The GroupMe Chat"
    data["embeds"] = []
    embed = {}
    embed["description"] = content['text']
    embed["title"] = str(content['name']).split(" ")[0] +": " + str(time)
    embed["image"] = {"url": imgUrl}
    embed["color"] = 0X32B1F1
    data["embeds"].append(embed)
    response = http.request('POST', url, body=json.dumps(data), headers = {'Content-Type': 'application/json'},retries = False)
    #result = requests.post(url, json=data, headers={"Content-Type": "application/json"})




    
