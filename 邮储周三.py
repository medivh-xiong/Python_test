import requests
import time
import datetime


cookies = {
    'MSESSIONID': 'd16ffed8-beeb-4e9b-9d15-639c55fef6f6',
    'smidV2': '20240221085727b46b5c497d5afd3d8dbb0bb5c4f272a600e8af342771d94e0',
    'UqZBpD3n3iTJDwxS': 'v1PKB+g8Sc+75',
}

headers = {
    'Host': 'psbc.huajifen.com',
    'branchCode': '000000',
    'Accept': 'application/json, text/plain, */*',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Sec-Fetch-Mode': 'cors',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://psbc.huajifen.com',
    'bankCode': '6100',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 /sa-sdk-ios/sensors-verify/ibfp.psbc.com?credit  CreditCardAppNew',
    'Referer': 'https://psbc.huajifen.com/impFront/voucherOrder?productId=103137&promotionId=19846&campId=10131&groupIndex=0&groupId=27885&configDiscribe=%E5%A5%96%E5%8A%B1%E7%82%B9',
    'Sec-Fetch-Dest': 'empty',
    # 'Cookie': 'MSESSIONID=41893c30-b100-4798-ab09-e8b249f0f722; smidV2=202402200941193bd9d44246a222b4b26eebe0cbbcc76a00409f66c46296840; UqZBpD3n3iTJDwxS=v1PKB+g8Sc+75',
}


json_data = {
    'mobileNo': '15951003078',
    'productId': 103137,
    'promotionId': 19846,
    'accountNo': '',
    'sign': 'lD5lVRaWnTwu5GW8pfK+Db7ASvbHOfiiaClzHyVb7co=',
    'cardInfo': {
        'cardNoAlis': '6259******8131',
        'id': 2189046,
    },
    'promProdInfo': {
        'productNo': '294975',
        'purseId': 'S00000001700520231222',
        'fullCredits': 0,
        'partCredits': 0,
        'partPrice': 0,
        'bankCodes': '6100',
        'productId': 103137,
        'promotionId': 19846,
        'rightPrice': 1,
    },
    'rewardName': '奖励点',
    'productBreed': 'E',
    'productType': '1',
    'campId': '10131',
    'orderNumber': '',
    'orderChannel': 'MobileApp',
    'smsCode': '',
}

def send_request():
    res = requests.post('https://psbc.huajifen.com/impMobile/order/initImpOrder', headers=headers, cookies=cookies, json=json_data)
    print(res.text)
    return res


target_time = datetime.datetime(2024, 2, 21, 9, 0, 0)
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
    if response.text.find('抢兑时间') != -1:
        print('还未开始')
        time.sleep(10)
        continue
    elif response.text.find('很抱歉,您目前尚未具备资格'):
        print('领取成功')
        exit()
    else:
        print('领取失败, 重新领取')
