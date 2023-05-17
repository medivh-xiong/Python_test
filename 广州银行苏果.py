import requests
import time
import datetime

cookies = {
    'JSESSIONID': 'B6185AF65A214A0DC86508072C823D20',
    'JSESSIONID': 'B6185AF65A214A0DC86508072C823D20',
    'UqZBpD3n3iPIDwJU': 'v1GaF+g8ScoDV',
    'Yr1B4j3mrFm8eHQ09Fnp7ifI': 'v1JaN+g8ScaRY',
}

headers = {
    'Host': 'trip.creditcard.gzcb.com.cn',
    'Content-Type': 'application/json;charset=utf-8',
    'Origin': 'https://trip.creditcard.gzcb.com.cn',
    # 'Cookie': 'JSESSIONID=B6185AF65A214A0DC86508072C823D20; JSESSIONID=B6185AF65A214A0DC86508072C823D20; UqZBpD3n3iPIDwJU=v1GaF+g8ScoDV; Yr1B4j3mrFm8eHQ09Fnp7ifI=v1JaN+g8ScaRY',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) gzbankapp',
    'Referer': 'https://trip.creditcard.gzcb.com.cn/CMBANK/6413/version4.0/index.html',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
}

params = {
    'method': 'saveRushApply',
}

json_data = {
    'bankCode': '6413',
    'rushId': 113770,
    'articleId': '104464',
    'rushName': '2023年5月苏果超市满50返25',
    'cardNo': '6228757770874707',
    'areaName': '南京',
    'serialNo': '15731681784585423',
    'discountDesc': '您可享受报名日起当月内逢周五指定苏果超市门店刷满50元一次性返还25元优惠，每月限1次，消费后次日起的5个工作日内入账。',
}

# 早上10点准点请求
def send_request():
    res = requests.post(
        'https://trip.creditcard.gzcb.com.cn/CMBANK/srv/rushPlaceTrans.do',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    return res




target_time = datetime.datetime(2023, 5, 12, 11, 0, 0)
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
    rspCode = json['RspCode']
    if rspCode == "000":
        print("领取成功")
        result = False
    else:
        print('领取失败, 重新领取')
        time.sleep(0.4)
