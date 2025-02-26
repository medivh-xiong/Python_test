import requests

headers = {
    'Host': 'gou.jieyou.pro',
    'content-type': 'application/json',
    'accept': 'application/json, text/plain, */*',
    'app-id': 'QhdZpITxqBy2tlKsvDqRHUT282QpRDEntgxonyqX3IQguoroAtAfBv0mH4JySbv7',
    'client-type': 'H5',
    'tenant-id': '98',
    'sec-fetch-site': 'same-site',
    'accept-language': 'zh-CN,zh-Hans;q=0.9',
    'sec-fetch-mode': 'cors',
    'charset': 'utf-8',
    'origin': 'https://mini.jieyou.pro',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 /sa-sdk-ios/sensors-verify/analytics.95516.com?production   (com.unionpay.chsp) (cordova 4.5.4) (updebug 0) (version 1005) (UnionPay/1.0 CloudPay) (clientVersion 305) (language zh_CN) (upApplet single) (walletMode 00) ',
    'referer': 'https://mini.jieyou.pro/',
    'sec-fetch-dest': 'empty',
    'third-session': 'wx:1673691262230130690:efd75ed4-fa8b-4b2b-abad-5dfb7f0d18c7',
}

json_data = {
    'phoneNumber': '17512573084',
    'spuId': '1531925834425085953',
}





response = requests.post('https://gou.jieyou.pro/mallapi/onedollarinterest/obtainCoupon', headers=headers, json=json_data)
