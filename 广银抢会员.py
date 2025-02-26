import requests

cookies = {
    '2mfFfHc8uOmwP': '5RdDNJDISjVVcqGiWHwQzgax71g872JkCJub1Q3HFICa5ZIQvPtf9ks4wpJvLNPAmS6q_aIxT5GARRY1wdZU4Ni1_LityYV3cPY002rf.6FQ0G2Ejuj4HuczpdxXUu10iWslUb_PP0wCMhuErdA1xiP9ZVqFUCXhs7m7ZrKMP84YJa5MIxy5APb35n6IMAJIkYjnKsRAeLe3QQPv_XZZjb0HXWKX4FCxerWkynhCQRqneFfjQJNbtGb2GU7ZNupn7p9wc1xXF3kIQjv4a5tSagno.wfPnjBbueL9hsQ_XNy7kuo1.Ap3L1AAVWIH7a7nrE',
    '2mfFfHc8uOmwO': '54jADg4nwHSnVVHb4TnYHJSfTng_tCAlzhF9HflpTKAAf73lSsff7XEQ91RnsP0HP.3NJisMib963sr9NbmX8g3hHv.KMPz0NohOJqwdyvjjVPolXfMYoj8ZEOJo.4Rpd',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218e3d9fc5f5634-00c39975a3fe9868-61685a24-250125-18e3d9fc5f7a36%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22mobileAppBank%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThlM2Q5ZmM1ZjU2MzQtMDBjMzk5NzVhM2ZlOTg2OC02MTY4NWEyNC0yNTAxMjUtMThlM2Q5ZmM1ZjdhMzYiLCJpZGVudGl0eV9tYWxsX3Rva2VuIjoidStPYjRuSTAvTmFWdTVLNmVDWnU1a29TM3FoRE9BcEJmZjdOWVNhOW5zdDFPVkxnSklZRjd3UEpCSWJYa0E2RCIsIiRpZGVudGl0eV9tcF91bmlvbmlkIjoib2xjZjh2c2Z0aG1uc3NnMlJsdjZSWHBfSHBUTSIsImlkZW50aXR5X3VzZXJpZCI6Im9DUlFPNUJOQ25yOUtNLVRYVUljRXFLelBMWVEiLCJpZF9jYXJkX251bWJlciI6Im9IaWRuSVRRUUhTdk1uc0pGYzJFeDBFckM2ajZnOGhuSTRwSXNTSlNmQjg9IiwiJGlkZW50aXR5X21vYmlsZSI6ImsrR2JWam9Zdy90R0U0S0VmamFnekE9PSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218e3d9fc5f5634-00c39975a3fe9868-61685a24-250125-18e3d9fc5f7a36%22%7D',
    '1735D64331DF397E': 'akxD2dLqGAE5T7tiNkfimQyBtH0rcpSDxsU9Dlxgu7RHrLMOE37OQAK1h989%2BM74n9WlmEZ6PAUjqLBn8iy3eA%3D%3D',
    '_xid': 'YkhkMIQ7I5j%2F0JZ3pBExAc2iiEuzmw2S3VZ%2BDMvrZPw%3D',
}

headers = {
    'Host': 'mall.creditcard.gzcb.com.cn',
    # 'Cookie': '2mfFfHc8uOmwP=5RdDNJDISjVVcqGiWHwQzgax71g872JkCJub1Q3HFICa5ZIQvPtf9ks4wpJvLNPAmS6q_aIxT5GARRY1wdZU4Ni1_LityYV3cPY002rf.6FQ0G2Ejuj4HuczpdxXUu10iWslUb_PP0wCMhuErdA1xiP9ZVqFUCXhs7m7ZrKMP84YJa5MIxy5APb35n6IMAJIkYjnKsRAeLe3QQPv_XZZjb0HXWKX4FCxerWkynhCQRqneFfjQJNbtGb2GU7ZNupn7p9wc1xXF3kIQjv4a5tSagno.wfPnjBbueL9hsQ_XNy7kuo1.Ap3L1AAVWIH7a7nrE; 2mfFfHc8uOmwO=54jADg4nwHSnVVHb4TnYHJSfTng_tCAlzhF9HflpTKAAf73lSsff7XEQ91RnsP0HP.3NJisMib963sr9NbmX8g3hHv.KMPz0NohOJqwdyvjjVPolXfMYoj8ZEOJo.4Rpd; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218e3d9fc5f5634-00c39975a3fe9868-61685a24-250125-18e3d9fc5f7a36%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22mobileAppBank%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThlM2Q5ZmM1ZjU2MzQtMDBjMzk5NzVhM2ZlOTg2OC02MTY4NWEyNC0yNTAxMjUtMThlM2Q5ZmM1ZjdhMzYiLCJpZGVudGl0eV9tYWxsX3Rva2VuIjoidStPYjRuSTAvTmFWdTVLNmVDWnU1a29TM3FoRE9BcEJmZjdOWVNhOW5zdDFPVkxnSklZRjd3UEpCSWJYa0E2RCIsIiRpZGVudGl0eV9tcF91bmlvbmlkIjoib2xjZjh2c2Z0aG1uc3NnMlJsdjZSWHBfSHBUTSIsImlkZW50aXR5X3VzZXJpZCI6Im9DUlFPNUJOQ25yOUtNLVRYVUljRXFLelBMWVEiLCJpZF9jYXJkX251bWJlciI6Im9IaWRuSVRRUUhTdk1uc0pGYzJFeDBFckM2ajZnOGhuSTRwSXNTSlNmQjg9IiwiJGlkZW50aXR5X21vYmlsZSI6ImsrR2JWam9Zdy90R0U0S0VmamFnekE9PSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218e3d9fc5f5634-00c39975a3fe9868-61685a24-250125-18e3d9fc5f7a36%22%7D; 1735D64331DF397E=akxD2dLqGAE5T7tiNkfimQyBtH0rcpSDxsU9Dlxgu7RHrLMOE37OQAK1h989%2BM74n9WlmEZ6PAUjqLBn8iy3eA%3D%3D; _xid=YkhkMIQ7I5j%2F0JZ3pBExAc2iiEuzmw2S3VZ%2BDMvrZPw%3D',
    'content-type': 'application/json',
    'accept': 'application/json, text/plain, */*',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'zh-CN,zh-Hans;q=0.9',
    'sec-fetch-mode': 'cors',
    'origin': 'https://mall.creditcard.gzcb.com.cn',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148/sa-sdk-ios/gzbankapp',
    'referer': 'https://mall.creditcard.gzcb.com.cn/mall-h5/?n=281564',
    'sec-fetch-dest': 'empty',
}

params = {
    'v9xtfhMd': '5wwDL9iQvmITU74v9QjbIjsB4mfwLmtpf50t8LDJcX04S2wy0yVWTkzofdKkDJlHkwvArU7AqxChj03BMKSDsLj4Ub.iQdvQ4xIpCQCanIfK_X2gmlkGPqUR9_AUvOQalG6TGHkYBaCQndOIm.8Hcrlopn7NKYa46ycfxo83xryqnpRt0ml67EQENNe0x294ZwKrC_trrN8nm5tqexQ03vV4kAlJlBN1C1z.ynr9hbNcxpeIrebZbodlnVBDFyJFkALNpU7L0EqojD_z1sWjON.u4lSJF0jVGOZ8xnrGNV697ko94tsyxPnPbbmvCBlnCQRFTOkX7Lu3QzjOc8wGkxApxnKtW.HOH6tr8BF2Kmc7',
}

json_data = {
    'data': {
        'key': 'ba1678e09fca625333047ad4c11c7dcc',
        'orderChannel': '1',
        'orderPayType': '1',
        'orderProductNum': '1',
        'rechargeType': '1',
        'rechargeValue': '296853461',
        'rightProductId': '10553',
        'userKey': 'f5d30abf8580471e9fdfaf18ad91323b834',
        'userToken': '070fa4f0cbfc470eb00f086c683042a8120',
        'versionItemCode': 'IosPay',
    },
    'sign': 'e0cb3a75ee514f453f3648393f012d57',
}

response = requests.post(
    'https://mall.creditcard.gzcb.com.cn/prettymall_api/auth/order/get/createGetRightOrder.do',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)
print(response.text)

