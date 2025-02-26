import requests

import json

# 定义URL

url = "https://mp.trendingstar.tech/fun-member/api/mall/createOrder"

# 定义请求头部

headers = {

    "Host": "mp.trendingstar.tech",

    "userId": "581270be836c72904f7c028059abcaaa",

    "uid": "3258577",

    "Content-Type": "application/json",

    "X-AUTH-TOKEN": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1bmlvbklkIjoib2xvTzU2Y0N3QUNOcUF2UjEyeHFIOFRTOEdOSSIsIm5iZiI6MTcyNDkyNTUzMiwiYXBwVHlwZSI6ImZ1bi13ZWNoYXQtbXAiLCJvcGVuSWQiOiJvTFkwaDVWQWlROHBrOWFiTU9jRnlmVjluZWJRIiwidXNlclV1SWQiOiI1ODEyNzBiZTgzNmM3MjkwNGY3YzAyODA1OWFiY2FhYSIsImV4cCI6MTcyNzUxNzUzMiwidXNlcklkIjozMjU4NTc3LCJpYXQiOjE3MjQ5MjU1MzJ9.ydDkTSR_qo0ssSZFf7_pKibvJg9SYO78HTzMsNRxqoA",

    "timeStamp": "1724926158037",

    "appId": "wxd30c7522dd4574b8683e7fdc75d17a",

    "sign": "19979e901d30fe9b2ca2090fa6b65466",

    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.50(0x1800323a) NetType/WIFI Language/zh_CN",

    "Referer": "https://servicewechat.com/wx6051d144a2afef7e/520/page-frame.html"

}

# 定义请求正文

data = {

    "fromType": 1,

    "useDeliveryCard": 0,

    "couponRecordId": "",

    "useRedPacket": 1,

    "prizeList": "[]",

    "goodsList": "[{\"purchaseInfoId\": 1445, \"activityId\": 1322, \"purchaseNums\": 1, \"goodsType\": 1}]",
    # 注意修正了转义字符

    "shareUserId": "",

    "distributor": "",

    "appId": "wxd30c7522dd4574b8683e7fdc75d17a",

    "addressId": 322050,

    "useRedPacketF": 0

}

# 发送POST请求

response = requests.post(url, headers=headers, json=data)

# 打印响应状态码和响应文本

print(response.status_code)

print(response.text)