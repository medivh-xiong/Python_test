import requests
import time
import datetime

cookies = {
    'sid': 'MCALOGIN-9869cf50-cf12-42cd-8f41-78f8614799b6',
    'act_sid': 'act-d0f3d8d4-eff6-4b3f-a8c0-1f509bddf7f1',
}

headers = {
    'Host': 'ump.cmpay.com',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    # 'Cookie': 'sid=MCALOGIN-9869cf50-cf12-42cd-8f41-78f8614799b6; act_sid=act-d0f3d8d4-eff6-4b3f-a8c0-1f509bddf7f1',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Html5Plus/1.0 (Immersed/20) uni-app',
    'X-Requested-With': 'XMLHttpRequest',
}

json_data = {
    'prizeNo': 'JFMS20238004',
    'sign': 'A',
}

def send_request():
    res = requests.post('https://ump.cmpay.com/activities/v1/members/integralTicketReceive', headers=headers, cookies=cookies, json=json_data, timeout=2)
    print(res.text)
    return res


target_time = datetime.datetime(2024, 8, 28, 15, 0, 0)
time_diff = (target_time - datetime.datetime.now()).total_seconds()
if time_diff > 0:
    time.sleep(time_diff)

result = True

while result:
    response = send_request()
    if response.status_code != 200:
        print('请求失败')
        time.sleep(0.3)
        continue
    # if response.text.find('抢兑时间') != -1:
    #     print('还未开始')
    #     time.sleep(10)
    #     continue
    # elif response.text.find('领取次数超过商品限制兑换次数') != -1:
    #     print('领取成功')
    #     exit()
    else:
        print('领取失败, 重新领取')
        time.sleep(0.3)

