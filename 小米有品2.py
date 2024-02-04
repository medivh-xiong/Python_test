import requests

cookies = {
    'mjclient': 'YouPin',
    'serviceToken': 'RuuQxXPwsbVNbPbWmocykRTvKlpdLN5ElN8n4jIsCvsnXrRHynPsU3zYjJw77MHkm8loLIhwDeiyOVhurEoJ4Cj9enzkDxia2BT30nt9Wzq1MbI64Mc89twMsmL0+5kzcS7YbYbAqgJ3zblwAmlKKQ==',
    'youpin_sessionid': '18cebf294e5-0778eaab9fb4e68-6160',
    'youpindistinct_id': '18ce80f8cb4-034050449ce92a8-6031',
}

headers = {
    'Host': 'm.xiaomiyoupin.com',
    # 'Cookie': 'mjclient=YouPin; serviceToken=RuuQxXPwsbVNbPbWmocykRTvKlpdLN5ElN8n4jIsCvsnXrRHynPsU3zYjJw77MHkm8loLIhwDeiyOVhurEoJ4Cj9enzkDxia2BT30nt9Wzq1MbI64Mc89twMsmL0+5kzcS7YbYbAqgJ3zblwAmlKKQ==; youpin_sessionid=18cebf294e5-0778eaab9fb4e68-6160; youpindistinct_id=18ce80f8cb4-034050449ce92a8-6031',
    'referer': 'https://m.xiaomiyoupin.com/app/shop/ugg/subscribeBuy.html?actId=6593ec0fbe07770001a8c931&spmref=YouPin_I.7346.158793.1.2361007',
    'c': '6',
    'x-requested-with': 'XMLHttpRequest',
    'd': '55',
    'user-agent': 'Mozilla/5.0 (iPad; CPU OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MIOTStore/20191212 (YouPin;5.21.0;8CCA50B3670797C8;;I;00000000-0000-0000-0000-000000000000;;8CCA50B3670797C8;9856B8A2-D037-59B9-B6C6-54F126814DE0) APP/com.xiaomi.youpin APPV/5.21.0 iosPassportSDK/4.2.17 iPadOS/17.2/XiaoMi/MiuiBrowser/4.3/Shop/ios/iPad8,6/4.5.91',
    'yp-srt': '1704765601343',
    'origin': 'https://m.xiaomiyoupin.com',
    'sec-fetch-dest': 'empty',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'zh-CN,zh-Hans;q=0.9',
    'yp-srs': '414288593',
    'yp-ss': '6EFBAD70974846807C0A9E8FDD0B963C',
    'accept': 'application/json',
    'content-type': 'application/json',
    'sec-fetch-mode': 'cors',
}

params = {
    '_': '1704765602258',
}

json_data = [
    {},
    {
        'actId': '6593ec0fbe07770001a8c931',
        'token': '6593ec0fbe07770001a8c931',
    },
]

response = requests.post(
    'https://m.xiaomiyoupin.com/mtop/act/orderspike/ekips00',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '[{},{"actId":"6593ec0fbe07770001a8c931","token":"6593ec0fbe07770001a8c931"}]'
#response = requests.post(
#    'https://m.xiaomiyoupin.com/mtop/act/orderspike/ekips00',
#    params=params,
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)