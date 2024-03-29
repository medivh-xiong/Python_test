import requests
import time
import datetime



cookies = {
    'MSESSIONID': '1d3d9de7-be16-40f7-a583-e65c6c373531',
    'smidV2': '20240320085556b70849b456d37af7c2d6bc2b23ff7cc500138c004e120ba10',
    'UqZBpD3n3iTJDwxS': 'v1OqB+g8ScR84',
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
    # 'Cookie': 'MSESSIONID=1d3d9de7-be16-40f7-a583-e65c6c373531; smidV2=20240320085556b70849b456d37af7c2d6bc2b23ff7cc500138c004e120ba10; UqZBpD3n3iTJDwxS=v1OqB+g8ScR84',
}

json_data = {
    'mobileNo': '15951003078',
    'productId': 103137,
    'promotionId': 19846,
    'accountNo': '',
    'sign': 'IkYiMDJuOAiK9B+dRmamlUcKTYhSvMPjjVvXjpzhuM0=',
    'cardInfo': {
        'cardNoAlis': '**********8131',
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


target_time = datetime.datetime(2024, 3, 20, 9, 0, 0)
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
    elif response.text.find('领取次数超过商品限制兑换次数') != -1:
        print('领取成功')
        exit()
    elif response.text.find('"success":true') != -1:
        print('领取成功')
        exit()
    else:
        print('领取失败, 重新领取')
