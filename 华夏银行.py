import requests
import time
import datetime

headers = {
    'Host': 'mrp.creditcard.hxb.com.cn',
    'Accept': 'application/json, text/plain, */*',
    'timestamp': '1706079636451',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Sec-Fetch-Mode': 'cors',
    'sessionId': '01c9b964-631e-46e1-baa3-5ec128dc418e',
    'Origin': 'https://mrp.creditcard.hxb.com.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) MicroMessenger/6.8.0(0x16080000) MacWechat/3.7(0x13070011) Safari/605.1.15 NetType/WIFI',
    'Referer': 'https://mrp.creditcard.hxb.com.cn/veryinterested/index.html?responseCode=00&isFirstLogin=0&isNewTenMind=null&surname=%E7%86%8A%E6%AC%A3',
    'Sec-Fetch-Dest': 'empty',
    'sign': 'qTVjQqQysDyMAEIrOlKeg/YDR4GTNpvPFKvBYsiaIK/UzYlQnoJ5/UR4xOQIq1wpxn3folbtkk5POs89g63bn2ziXYOj9NK3oVBbwMqMM4/ypfeOljiZyvCsgQNho83Yw8j9wKTXMwDUE9afpmLMFUKeFprDpMAP+mucGQ2mQGPttUYGERcPVNwe3+STUCYm/pmg25PgtKYHEEZ3z+EXVrGAMWB/YEVbG0U6CUU7mGmKuhBPKY1Jk+i1n0JOWi3Je//ISPtHMi0wckg8itAkFtYnucUwvvA5GafuRIuxg6M+yU+WtkDqIAuxkmKuS8GQ4AKY1nfyjTL0qK3DBa+wrA==',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
    'cur_data': '{"prodCode":"SPSJ002119","issueNum":1}',
    'sessionId': '01c9b964-631e-46e1-baa3-5ec128dc418e',
}

# 早上10点准点请求
def send_request():
    res = requests.post('https://mrp.creditcard.hxb.com.cn/online/3009', headers=headers, data=data)
    return res


target_time = datetime.datetime(2023, 10, 26, 14, 0, 0)
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

