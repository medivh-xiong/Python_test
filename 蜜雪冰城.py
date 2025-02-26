import requests
import time
import datetime
from requests.exceptions import Timeout

headers = {
    'Host': 'mxsa.mxbc.net',
    'Accept': 'application/json, text/plain, */*',
    'Sec-Fetch-Site': 'same-site',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Sec-Fetch-Mode': 'cors',
    'Content-Type': 'application/json;charset=utf-8',
    'Origin': 'https://mxsa-h5.mxbc.net',
    'Access-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ3eG1pbmlfMTgxODQ4MjQxNTEwMzMwNzc3OCIsImlhdCI6MTcyMjM5NDk2OH0.JeQRbTY2wxjQxBAKKyPu8R2UlTEQFlQ5yj8PpjcxRnpo3Qts7lM_BqzkimQhVR-t1Sf6g34-nmkxvVKCirhorA',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.50(0x18003234) NetType/WIFI Language/zh_CN miniProgram/wx7696c66d2245d107',
    'Referer': 'https://mxsa-h5.mxbc.net/',
    'Sec-Fetch-Dest': 'empty',
}

params = {
    'type__1286': 'Cq0xc7iQDQ0QuD0y3IKDOUD8Fy5Y5Dk/AbeD',
}

# 获取当前时间的秒级时间戳
seconds = time.time()

# 将秒级时间戳转换为毫秒级时间戳
milliseconds = int(seconds * 1000)

json_data = {
    'marketingId': '1816854086004391938',
    'round': '12:00',
    'secretword': '茉莉奶绿销量突破1000万杯',
    'sign': 'db7fed7c1a363f4da91de31f7d3522a5',
    's': 2,
    'stamp': milliseconds,
}

print(json_data)

def send_request():
    try:
        res = requests.post('https://mxsa.mxbc.net/api/v1/h5/marketing/secretword/confirm',
                            params=params,
                            headers=headers,
                            json=json_data,
                            timeout=2)
        print(res.text)
        return res
    except Timeout:
        print("请求超时，但程序没有崩溃！")

target_time = datetime.datetime(2024, 7, 15, 9, 30, 0)
time_diff = (target_time - datetime.datetime.now()).total_seconds()
if time_diff > 0:
    time.sleep(time_diff)

result = True

while result:
    response = send_request()
    print(response.text)
    if response.status_code != 200:
        print('请求失败')
        time.sleep(1)
        continue
    if response.text.find('本周名额已抢光') != -1:
        print('已经抢完')
        exit()
    if response.text.find('W1190950079482429441') != -1:
        print("抢购成功")
        exit()
    elif response.text.find('您存在待支付订单') != -1:
        print("抢购成功")
        exit()
    else:
        print('领取失败, 重新领取')
        time.sleep(1)
