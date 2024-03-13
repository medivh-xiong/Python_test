import requests

cookies = {
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218d5d3cc7a224d-04ba1e33452e00c-61685a24-250125-18d5d3cc7a4554%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22mobileAppBank%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThkNWQzY2M3YTIyNGQtMDRiYTFlMzM0NTJlMDBjLTYxNjg1YTI0LTI1MDEyNS0xOGQ1ZDNjYzdhNDU1NCIsImlkZW50aXR5X21hbGxfdG9rZW4iOiIwNzBmYTRmMGNiZmM0NzBlYjAwZjA4NmM2ODMwNDJhODEyMCIsIiRpZGVudGl0eV9tcF91bmlvbmlkIjoib2xjZjh2c2Z0aG1uc3NnMlJsdjZSWHBfSHBUTSIsImlkZW50aXR5X3VzZXJpZCI6Im9DUlFPNUJOQ25yOUtNLVRYVUljRXFLelBMWVEiLCJpZF9jYXJkX251bWJlciI6Im9IaWRuSVRRUUhTdk1uc0pGYzJFeDBFckM2ajZnOGhuSTRwSXNTSlNmQjg9IiwiJGlkZW50aXR5X21vYmlsZSI6ImsrR2JWam9Zdy90R0U0S0VmamFnekE9PSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218d5d3cc7a224d-04ba1e33452e00c-61685a24-250125-18d5d3cc7a4554%22%7D',
    '2mfFfHc8uOmwO': '596W5J6QsTqFXu9H.b_I1icXcMZCtpxU8hdBXxydXj1xKtgfBKO5i.YzO9Lc5UsUTAqb6qFFIiUObQTOV0.I.dCEqNneriRikZuBZkbvX86Pd8rRVaIKKXFqJYysRaVqr',
    '2mfFfHc8uOmwP': '5ReeoBKIIpeacqGiH_2N0kAR5Vl0QdU9hHGDW28wfCJbbbgMRbdh0ifFVuFekLFiVAfp6_PQDR1sXuOWuKIB.33HuKC6HJfPD2UQyYwxG14xV9BRDbtgVMQIhQIgw9OltQ3hyY.lIf6lzRubVWr0iuT2HNXb5KjCoGtIJKXIkuS_7GVzG277SJttgkU2m8VrMAk2NOXr1uG9JJWHkxFLMjP.E4TCCdbIeBprqROwN82iQzTcLpVVSEx1QL6uwNv44G',
}

headers = {
    'Host': 'mall.creditcard.gzcb.com.cn',
    'content-type': 'application/json',
    'accept': 'application/json, text/plain, */*',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'zh-CN,zh-Hans;q=0.9',
    'sec-fetch-mode': 'cors',
    'origin': 'https://mall.creditcard.gzcb.com.cn',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148/sa-sdk-ios/gzbankapp',
    'referer': 'https://mall.creditcard.gzcb.com.cn/mall-h5/?n=160103',
    'sec-fetch-dest': 'empty',
}

params = {
    'v9xtfhMd': '56e4X4XvwOdoZYLm_31jagslPqzgNPD855fmQH6BVIM7S4xmdVz4DjLs3s7hGF3iysNMA49UmIP4Ge4ziVU_2JRtyWN.C2ebegZjCiCE9kruX7bQMTZs_Nw934S3I4ZptLxGEM7nrTZQyKcukeGusqdNP5DlB_FCz1Jh8lqzF6pECSOJFefG6TePav76xYbNCu.1rjRDJ0P6U9M1f0OiIv8BZkesphhPqfaKgqVmgU0C4m9G2lFnNibFTHiBGLsfSFkE_3Ibuqdf6GQFNNcMgCcTdPzOG2Ex7.64W.hpMVpl',
}

json_data = {
    'data': {
        'key': '7a0538cd9102d35e9462f4e519416ade',
        'orderChannel': '1',
        'orderPayType': '1',
        'orderProductNum': '1',
        'rechargeType': '1',
        'rechargeValue': '296853461',
        'rightProductId': '10547',
        'userKey': 'e3bc54224b9547e6842e38b3774a8633796',
        'userToken': '070fa4f0cbfc470eb00f086c683042a8120',
        'versionItemCode': 'IosPay',
    },
    'sign': '62aa97a411b473a2f33ea51f8a7d56d6',
}

response = requests.post(
    'https://mall.creditcard.gzcb.com.cn/prettymall_api/auth/order/get/createGetRightOrder.do',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)
print(response.text)

