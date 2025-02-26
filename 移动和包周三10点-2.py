import requests
import time
import datetime

cookies = {
    'sid': 'MCALOGIN-a0785f28-b173-47c9-a75d-183e2ec5b64a',
    'act_sid': 'act-780a0240-ebc3-43f9-b27a-3c92956d4c93',
}


headers = {
    'Host': 'ump.cmpay.com',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    # 'Cookie': 'sid=MCALOGIN-1d9acfe3-1a9d-4481-9e52-dceabcdc652e; act_sid=act-19532b02-cae4-481c-9c7a-7227ead23f03',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Html5Plus/1.0 (Immersed/20) uni-app',
    'X-Requested-With': 'XMLHttpRequest',
}

json_data = {
    'prizeNo': 'JFMS20234006',
}

def send_request():
    res = requests.post('https://ump.cmpay.com/activities/v1/members/integralTicketReceive', headers=headers, cookies=cookies, json=json_data, timeout=2)
    print(res.text)
    return res


target_time = datetime.datetime(2024, 3, 27, 10, 0, 0)
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

