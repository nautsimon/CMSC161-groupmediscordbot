import json
from datetime import datetime
import urllib3
import groupmebotsecrets




def lambda_handler(event, context):
    http = urllib3.PoolManager()
    content = json.loads(event['body'])
    ts  = content['created_at'] - 21600
    time = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print(time)
    data = {}
    data["username"] = "GROUPME BOT"
    data["embeds"] = []
    embed = {}
    embed["description"] = content['text']
    embed["title"] = str(content['name']).split(" ")[0] +": " + str(time)
    embed["color"] = 0X32B1F1
    data["embeds"].append(embed)
    response = http.request('POST', groupmebotsecrets.url, body=json.dumps(data), headers = {'Content-Type': 'application/json'},retries = False)




    