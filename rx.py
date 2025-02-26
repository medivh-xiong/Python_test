import requests

cookies = {
    'uid': 'd2c53ab8-73d1-4ec4-bb6b-4302185eef161731294759583',
}

headers = {
    'Host': 'capi.lkcoffee.com',
    # 'Cookie': 'uid=d2c53ab8-73d1-4ec4-bb6b-4302185eef161731294759583',
    'x-lk-akv': 'lk-wxmp-v5.1.72',
    'x-lk-sid': '601989',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/6.8.0(0x16080000) NetType/WIFI MiniProgramEnv/Mac MacWechat/WMPF MacWechat/3.8.7(0x13080712) XWEB/1191',
    'x-lk-csid': 'bfec78d3-0694-a1c9-856b-60376a854655',
    'content-type': 'application/x-www-form-urlencoded',
    'xweb_xhr': '1',
    'x-lk-mid': '263905160',
    'accept': '*/*',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://servicewechat.com/wx21c7506e98a2fe75/719/page-frame.html',
    'accept-language': 'zh-CN,zh;q=0.9',
}

data = {
    'cid': '230101',
    'q': 'HYeJKekUfZVYNXdcfbzcloWZB0coxwg1O_j2w7eZxw0wprvrIlyJUJrya8PpWlm_tFCHE3RrPXqpRGrZIPPSGpMacfwjDqvwK56nqKsFjKEZL4xBghR_o8fYZNzOB4dWxjgUXhb5t3JDiwT05xC5828H4N7E1ACN95MKPoUpxs8=',
    'dk': '1',
    'sign': '144239735066825660014588477052021135108',
}

response = requests.post(
    'https://capi.lkcoffee.com/resource/core/v2/virtual/product/limited',
    cookies=cookies,
    headers=headers,
    data=data,
)

print(response.text)