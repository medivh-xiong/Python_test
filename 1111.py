import requests

cookies = {
    'MSESSIONID': 'ae18e312-c918-4209-b4c8-0841922251d2',
    'smidV2': '202403270851073053610cd54c77eca5549f5581f280d500aedc02ac2dc10c0',
    'UqZBpD3n3iTJDwxS': 'v1P6B+g8Scttw',
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
    # 'Cookie': 'MSESSIONID=ae18e312-c918-4209-b4c8-0841922251d2; smidV2=202403270851073053610cd54c77eca5549f5581f280d500aedc02ac2dc10c0; UqZBpD3n3iTJDwxS=v1P6B+g8Scttw',
}

json_data = {
    'mobileNo': '15951003078',
    'productId': 103137,
    'promotionId': 19846,
    'accountNo': '',
    'sign': 'IkYiMDJuOAiK9B+dRmamlWAiOGZ79tPsZTzEoVn5lOE=',
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

response = requests.post(
    'https://psbc.huajifen.com/impMobile/order/initImpOrder',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
print(response.text)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"mobileNo":"15951003078","productId":103137,"promotionId":19846,"accountNo":"","sign":"IkYiMDJuOAiK9B+dRmamlWAiOGZ79tPsZTzEoVn5lOE=","cardInfo":{"cardNoAlis":"**********8131","id":2189046},"promProdInfo":{"productNo":"294975","purseId":"S00000001700520231222","fullCredits":0,"partCredits":0,"partPrice":0,"bankCodes":"6100","productId":103137,"promotionId":19846,"rightPrice":1},"rewardName":"奖励点","productBreed":"E","productType":"1","campId":"10131","orderNumber":"","orderChannel":"MobileApp","smsCode":""}'.encode()
#response = requests.post('https://psbc.huajifen.com/impMobile/order/initImpOrder', cookies=cookies, headers=headers, data=data)