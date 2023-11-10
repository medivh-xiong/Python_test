import requests
import time
import datetime

headers = {
    'Host': 'mrp.creditcard.hxb.com.cn',
    'Accept': 'application/json, text/plain, */*',
    'timestamp': '1698213619557',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Sec-Fetch-Mode': 'cors',
    'sessionId': '36505c95-0c4a-4f2b-a199-f0c30c85c460',
    'Origin': 'https://mrp.creditcard.hxb.com.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) MicroMessenger/6.8.0(0x16080000) MacWechat/3.7(0x13070011) Safari/605.1.15 NetType/WIFI',
    'Referer': 'https://mrp.creditcard.hxb.com.cn/veryinterested/index.html?responseCode=00&isFirstLogin=0&surname=%E7%86%8A%E6%AC%A3',
    'Sec-Fetch-Dest': 'empty',
    'sign': 'O3gOCl71iNBdoQfY09o2ofB2hOWdrlI1oVWu9gvO+uQIGNQ4Acfnf+7yAbepv4fDhTNhlDlTEziw8C+OCjS9xIv5lCtFYQKrHMEpKFSi0dlS+JsvWJplB41eNjt52EAdCcmIsVO692RyFJuYiydf8qhasGLBVvoL4DQf1ga9FUEnmyB/myuO/tIuJhpgn8PP8QvWN/6ky+gwzA1Xb0RKm8U0iREBsJ1lYq8fKw/otsKoJfB93SpR0S4znqzO4zs6ThnvMfT0+K+PQgphAyZBRiFsuxSJv42ZyJBMY51uomnZP665Jly3psXgZQM5JNqvc20S2yx4oGg1iGEmCSCB1A==',
    'Content-Type': 'application/x-www-form-urlencoded',
}
data = {
    'cur_data': '{"prodCode":"SPSJ002012","issueNum":1}',
    'sessionId': '36505c95-0c4a-4f2b-a199-f0c30c85c460',
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

