import requests
import time
import datetime


headers = {
    'Host': 'mrp.creditcard.hxb.com.cn',
    'Accept': 'application/json, text/plain, */*',
    'timestamp': '1706594448020',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Sec-Fetch-Mode': 'cors',
    'sessionId': '06bccc73-56b3-482e-8ca9-6b7adac6121a',
    'Origin': 'https://mrp.creditcard.hxb.com.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) MicroMessenger/6.8.0(0x16080000) MacWechat/3.7(0x13070011) Safari/605.1.15 NetType/WIFI',
    'Referer': 'https://mrp.creditcard.hxb.com.cn/veryinterested/index.html?responseCode=00&isFirstLogin=0&pageSwitch=null&surname=%E7%86%8A%E6%AC%A3',
    'Sec-Fetch-Dest': 'empty',
    'sign': 'VoizD82UWlPnwVIjbEBF+/bwesT0W+0n+5KtdvfeEA7INofn/cIhrQPmwHZ9xhDLv68E/78o/2XOb8K3GJDrtSdsG6YNuGaxmSuhICTK9TBmZmr3Pwfn0FFUNeuQbSBabzlxI9OUdyRDJ+Y5oAwrlraONW/tir2KvSvi9fSF+qTTe4FTKf4Kfb6uILfT717XNTOPD9ToEco3HNeXDYm+jEZ6t5qpO8HJ4zCYBNityohdXovK43qqmgjas3c3BkcVCKCrrxS0yj8j2/RE1RBjngYMivMTlaQF8kZ0BENEPe6MyRXuki/HW+3lw25rHauviXkUgUIcZlWNtNHvfD8K6A=='
}

data = {
    'cur_data': '{"issueNum":1,"prodCode":"SPSJ002119"}',
    'sessionId': '06bccc73-56b3-482e-8ca9-6b7adac6121a'
}

def send_request():
    res = requests.post('https://mrp.creditcard.hxb.com.cn/online/3009', headers=headers, data=data)
    print(res.text)
    return res


target_time = datetime.datetime(2024, 2, 2, 14, 0, 0)
time_diff = (target_time - datetime.datetime.now()).total_seconds()
if time_diff > 0:
    time.sleep(time_diff)

result = True

while result:
    response = send_request()
    if response.status_code != 200:
        print('请求失败')
        time.sleep(0.1)
        continue
    if response.text.find('兑换未开始'):
        print('还未开始')
        time.sleep(0.1)
        continue
    elif response.text.find('很抱歉,您目前尚未具备资格'):
        print('领取成功')
        exit()
    else:
        print('领取失败, 重新领取')
        time.sleep(0.1)
