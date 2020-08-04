url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=d0d74b9a-f533-4313-8494-d13b7ca56fba"
import urllib
import urllib.request
import json
import datetime
from datetime import timedelta
import time
def sendRequest(msg):
    data ={ "msgtype": "markdown", "markdown":  {"content":msg}}
    data = json.dumps(data)
    print(data)
    req= urllib.request.Request(url,method='POST',data=bytes(data.encode("utf-8")))
    with urllib.request.urlopen(req) as resp:
        pass
        # response_data = json.loads(resp.read().decode("utf-8"))
        # print(response_data)
one = datetime.time(17,38,00)
tow = datetime.time(18,00,00)
three = datetime.time(19,00,00)
# tow = datetime.time(11,21,10)
print('start botdady')
# while True:
dt = datetime.datetime.now()
cur_d = dt.date()
cur_t=dt.time()
if cur_t < one:
    start_player=datetime.datetime.combine(cur_d,one)
elif cur_t < tow  and cur_t > one:
    start_player=datetime.datetime.combine(cur_d,tow)
elif cur_t <three  and cur_t > tow:
    start_player=datetime.datetime.combine(cur_d,three)
delta=start_player - dt
    # time.sleep(1*60*60)
if cur_t == one or cur_t == tow:
    with open('botdady.md','r',encoding='utf-8') as f:
        sendRequest("push pole social :"+str(delta)+"\n"+f.read())
