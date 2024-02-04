import requests
import time
import datetime

cookies = {
    'JSESSIONID': 'CBEE72A4BE5129BCFA188D64518EBC26',
    'acsweb_session_sticky': '989d4d22605204f09840d33fd8582876',
    'zx_acsweb_sessionid': '2cf192c49feb7a13a7b493b1705bc896',
    '__VCAP_ID__': 'cc1be550-d208-4a4e-49ae-68ac',
    'kzx_acsweb_session_sticky': 'fbd936937261e49cb09df331db20f766',
    'mapp_session_sticky': '568d4663ad0374a6bcc8210e53e4d432',
}

headers = {
    'Host': 'creditcardapp.bankcomm.com',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'cors',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://creditcardapp.bankcomm.com',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148com.bankcomm.maidanba.V2;mapp_saoma;isApplePayUsable;paypinflag;newVCard;digitalcert;WKWebView;UnionPay/1.0 BoComMDB;buildVersion239;mdbTitleBar;',
    'Referer': 'https://creditcardapp.bankcomm.com/acsweb/actDetail/progressForActive?payMrchntNo=301001900001642&callbackurl=acsweb/actDetail/progressForActive&actId=20230920210549&regist=false&mgmType=null&mgmId=null&org.apache.catalina.filters.CSRF_NONCE=60D2DB2E047A2C29A1A9BE8F409BC5BC',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    # 'Cookie': 'JSESSIONID=429763C753FE032A974584D9863E06CA; __VCAP_ID__=a9291282-33b2-44ae-7508-ef18; acsweb_session_sticky=697f57782cdd6dae1d190f7e75eab694; kzx_acsweb_session_sticky=dd9ad5edc445ecd16b3e78a7d1d64c7b; zx_acsweb_sessionid=bf4ee0488e49c78bc5155714a66cdf10; mapp_session_sticky=297d4ee824e4f7b51053d29192674f99',
}

data = {
    'taskId': '20230921104158',
    'actId': '20230920210549',
    'awardId': '20230921102046',
    'prizeId': '20230920212021',
    'orderNo': '',
    'token': '414F4CE527D373802E18A9CF167364A1',
}

# 早上10点准点请求
def send_request():
    res =requests.post('https://creditcardapp.bankcomm.com/acsweb/actDetail/award', cookies=cookies, headers=headers, data=data)

    print(res.text)
    return res


target_time = datetime.datetime(2024, 1, 10, 10, 0, 0)
time_diff = (target_time - datetime.datetime.now()).total_seconds()
if time_diff > 0:
    time.sleep(time_diff)

count = 10

while count >= 0:
    response = send_request()
    count -= 1
    if response.status_code != 200:
        print('请求失败')
        time.sleep(0.2)
        continue
    json = response.json()
    rspCode = json['returnCode']
    if '成功' in response.text:
        print("领取成功")
        result = False
    elif rspCode == "AY1019":
        print('抱歉，活动尚未开始。')
        exit()
    else:
        print('领取失败, 重新领取')
        time.sleep(0.4)
