import requests
import time
import datetime

cookies = {
    '2mfFfHc8uOmwP': '5RLvHbDFxuZWcqGitar_amaWu1IJU8i_1xnlY2sMtWeBeurMef2zlSHDssLjy3czsGDBoT2FyTByUTj4CtwMwmUrk0pjEERiOnrInDN9kyAMVFahxr2KCB0PRLFBUeoXIqacL3O1_YPAl7wi5twE8NkVe7ZUvywd_3wP.7h.FI3zKSTKSqTzNSEb0jjiJn8Z8R90Z33Fvqh.OR5Ef.Ac9_QRvBr5BH_RumCF_G31O87akJoACv4fkQZxzXVpxmZItosv5zpnGVU_d2.cBLe8LPB',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22188c21bc1811ef-0c18290424cd5c8-6a126d64-250125-188c21bc184141%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22mobileAppBank%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg4YzIxYmMxODExZWYtMGMxODI5MDQyNGNkNWM4LTZhMTI2ZDY0LTI1MDEyNS0xODhjMjFiYzE4NDE0MSIsImlkZW50aXR5X21hbGxfdG9rZW4iOiJ1K09iNG5JMC9OYVZ1NUs2ZUNadTVrb1MzcWhET0FwQmZmN05ZU2E5bnN0MU9WTGdKSVlGN3dQSkJJYlhrQTZEIiwiJGlkZW50aXR5X21wX3VuaW9uaWQiOiJvbGNmOHZzZnRobW5zc2cyUmx2NlJYcF9IcFRNIiwiaWRlbnRpdHlfdXNlcmlkIjoib0NSUU81Qk5DbnI5S00tVFhVSWNFcUt6UExZUSIsImlkX2NhcmRfbnVtYmVyIjoib0hpZG5JVFFRSFN2TW5zSkZjMkV4MEVyQzZqNmc4aG5JNHBJc1NKU2ZCOD0iLCIkaWRlbnRpdHlfbW9iaWxlIjoiaytHYlZqb1l3L3RHRTRLRWZqYWd6QT09In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22188c21bc1811ef-0c18290424cd5c8-6a126d64-250125-188c21bc184141%22%7D',
    '2mfFfHc8uOmwO': '5qThisHB7YEaDbqntJfd31Yh57o.oHENyXefAA4csdG0UUS5WHprtARfKAbVjzV7JvQXxsQGxayv_CUE65uR43A',
    'sajssdk_2015_cross_new_user': '1',
}

headers = {
    'Host': 'mall.creditcard.gzcb.com.cn',
    # 'Cookie': '2mfFfHc8uOmwP=5RLvHbDFxuZWcqGitar_amaWu1IJU8i_1xnlY2sMtWeBeurMef2zlSHDssLjy3czsGDBoT2FyTByUTj4CtwMwmUrk0pjEERiOnrInDN9kyAMVFahxr2KCB0PRLFBUeoXIqacL3O1_YPAl7wi5twE8NkVe7ZUvywd_3wP.7h.FI3zKSTKSqTzNSEb0jjiJn8Z8R90Z33Fvqh.OR5Ef.Ac9_QRvBr5BH_RumCF_G31O87akJoACv4fkQZxzXVpxmZItosv5zpnGVU_d2.cBLe8LPB; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22188c21bc1811ef-0c18290424cd5c8-6a126d64-250125-188c21bc184141%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22mobileAppBank%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg4YzIxYmMxODExZWYtMGMxODI5MDQyNGNkNWM4LTZhMTI2ZDY0LTI1MDEyNS0xODhjMjFiYzE4NDE0MSIsImlkZW50aXR5X21hbGxfdG9rZW4iOiJ1K09iNG5JMC9OYVZ1NUs2ZUNadTVrb1MzcWhET0FwQmZmN05ZU2E5bnN0MU9WTGdKSVlGN3dQSkJJYlhrQTZEIiwiJGlkZW50aXR5X21wX3VuaW9uaWQiOiJvbGNmOHZzZnRobW5zc2cyUmx2NlJYcF9IcFRNIiwiaWRlbnRpdHlfdXNlcmlkIjoib0NSUU81Qk5DbnI5S00tVFhVSWNFcUt6UExZUSIsImlkX2NhcmRfbnVtYmVyIjoib0hpZG5JVFFRSFN2TW5zSkZjMkV4MEVyQzZqNmc4aG5JNHBJc1NKU2ZCOD0iLCIkaWRlbnRpdHlfbW9iaWxlIjoiaytHYlZqb1l3L3RHRTRLRWZqYWd6QT09In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22188c21bc1811ef-0c18290424cd5c8-6a126d64-250125-188c21bc184141%22%7D; 2mfFfHc8uOmwO=5qThisHB7YEaDbqntJfd31Yh57o.oHENyXefAA4csdG0UUS5WHprtARfKAbVjzV7JvQXxsQGxayv_CUE65uR43A; sajssdk_2015_cross_new_user=1',
    'content-type': 'application/json;charset=utf-8',
    'accept': 'application/json, text/plain, */*',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'zh-CN,zh-Hans;q=0.9',
    'sec-fetch-mode': 'cors',
    'origin': 'https://mall.creditcard.gzcb.com.cn',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) gzbankapp',
    'referer': 'https://mall.creditcard.gzcb.com.cn/mall/?n=78812',
    'sec-fetch-dest': 'empty',
}

params = {
    'v9xtfhMd': '5niUtlU5NgSF7QRQ1e.EZNk.pC0OO_k.orNeAh94rp_vis2VfpZmZdL2xoFDJaY9AyYouAGp2gpvBQkT7uYoDzUaOYWBV0m4kFAGCS4UABEskldSGVqAJKPK54hdMA7FtenvLK3Aa4nS6QntYFigooGWhqLWi4Ca0Mp6Ou2IXuTETV3D0foehDPp2O_QMLCPMO.6B1.DYB4WQw_SSh0_FMcZ0hBsVzdUn1fqstfKBAeZYEURkJhSvyKIvY1r.zHC8Atvw7x6GXuiJ.kWo1dwFhJBt.g9.1O9znhmkPPtAtPrH9SwTCKrMMdaCpQb6FLXZ',
}

json_data = {
    'data': {
        'key': 'e8bc8eea9af7f79ef2f5118fd5ea213c',
        'userKey': '8b493edd1a9940b4ad1d73a56609a4ba641',
        'userToken': '070fa4f0cbfc470eb00f086c683042a8120',
        'voucherId': '3621',
    },
    'sign': 'c83b352454a62ffa25ac2eefc14d0649',
}

# 早上10点准点请求
def send_request():
    res = requests.post(
        'https://mall.creditcard.gzcb.com.cn/prettymall_api/auth/voucher/createVoucherEntity.do',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    return res




target_time = datetime.datetime(2023, 6, 16, 10, 52, 0)
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
    print(json)
    rspCode = json['RspCode']
    msg = json['msg']
    if "抢光" in msg:
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

