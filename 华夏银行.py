import requests
import time
import datetime

headers = {
    'Host': 'mrp.creditcard.hxb.com.cn',
    'Accept': 'application/json, text/plain, */*',
    'timestamp': '1710399252695',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Sec-Fetch-Mode': 'cors',
    'sessionId': '1d2157e0-eae2-410d-81f3-a45dc9997fed',
    'Origin': 'https://mrp.creditcard.hxb.com.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) MicroMessenger/6.8.0(0x16080000) MacWechat/3.7(0x13070011) Safari/605.1.15 NetType/WIFI',
    'Referer': 'https://mrp.creditcard.hxb.com.cn/eiPoint/index.html?responseCode=00&surname=%E7%86%8A%E6%AC%A3',
    'Sec-Fetch-Dest': 'empty',
    'sign': 'LLP5+eCXzy7rmxi+O8BKe/Dd21ViWWSlJ/7UItmHUYxCGTOy542A91i2o2fqomOHuiAdgbg6tTu3feNCVvYARXbHZNLuIPov7V2gtENZP62GFwVzBX+wg8XKqLAUm6mTdE9SWMwkyjZ8RCNaVa+GRwqriy9fMZbF3bba4fbcfxAoVbfLVnyExHXz2qMbd2XfvyMc0MQo53gnReAWrJ0MIK+KukoWWh2R+ThYR1TsHjDZNrroHvoBkH8q0vfCCDAw3rZojMj0jkPD7Cv7vXeTRcs2cqCBdRdW5zsyOANhqzQx4UJk6K8nPJhe0WZvyWg0twnf98aaKL3rGQNBN90Fdw==',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
    'cur_data': '{"prodCode":"SPSJ002263","issueNum":1}',
    'sessionId': '1d2157e0-eae2-410d-81f3-a45dc9997fed',
}

# 早上10点准点请求
def send_request():
    res = requests.post('https://mrp.creditcard.hxb.com.cn/online/3009', headers=headers, data=data)
    return res


target_time = datetime.datetime(2024, 3, 14, 15, 0, 0)
time_diff = (target_time - datetime.datetime.now()).total_seconds()
if time_diff > 0:
    time.sleep(time_diff)

result = True

while result:
    response = send_request()
    if response.status_code != 200:
        print('请求失败')
        time.sleep(0.2)
        continue
    json = response.json()
    rspCode = json['responseCode']
    msg = json['responseMsg']
    if "您来晚了" in msg:
        print("抱歉,券已经被抢光啦,请期待下一轮")
        result = False
    else:
        print(msg)
        if "成功" in msg:
            result = False
            print("领取成功")
        else:
            print('领取失败, 重新领取')
            time.sleep(0.4)

