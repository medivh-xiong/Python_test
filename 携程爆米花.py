import requests
import time
import datetime

cookies = {
    'GUID': '09031067219085125642',
    '_abtest_userid': '2de85528-3112-43af-9d51-35ba9654eac4',
    'nfes_isSupportWebP': '1',
    '_bfaStatusPVSend': '1',
    '_RSG': 'L.q1b7h0wn3q0X2IQghGIB',
    '_RDG': '28533ab76411c225b024ec4e118bedde13',
    '_RGUID': '3c7a02b1-e507-4f95-b490-aea6920a1034',
    '_bfs': '1.2',
    '_bfi': 'p1%3D153002%26p2%3D10650083748%26v1%3D2%26v2%3D1',
    'cticket': '5B61B782C3256A0F1B00BAD7554E11C8809A79358F23A3B66E00E55FB121282E',
    'login_type': '0',
    'login_uid': 'E13C9EF3D20DE1EC784E314A1F8A979B',
    'DUID': 'u=463AE8FDC2C03386E055B75613598E45&v=0',
    'IsNonUser': 'F',
    'AHeadUserInfo': 'VipGrade=30&VipGradeName=%D7%EA%CA%AF%B9%F3%B1%F6&UserName=%D0%DC%D0%C0&NoReadMessageCount=1',
    'UUID': '26FE780F474A40C19EA61A9211936BF2',
    '_bfaStatus': 'send',
    'Union': 'OUID=&AllianceID=66672&SID=1693366&SourceID=&AppID=&OpenID=&exmktID=&createtime=1683512259&Expires'
             '=1684117058639',
    'MKT_Pagesource': 'H5',
    '_RF1': '117.89.208.4',
    '_pd': '%7B%22_o%22%3A2%2C%22s%22%3A106%2C%22_s%22%3A0%7D',
    'MKT_code': 'PUSHCODE=dbiconfl&createtime=1683512992',
    'MKT_OrderClick': 'ASID=&AID=&CSID=&OUID=&CT=1683512992118&CURL=https%3A%2F%2Fm.ctrip.com%2Fwebapp'
                      '%2Fvipwelfareapp%2Fhome%3Fpopup%3Dclose%26pushcode%3Ddbiconfl%26ishidenavbar%3Dyes'
                      '%26from_native_page%3D1%26s_guid%3D6fbc8ce3-a8fe-43a8-97f1-eead2cd83764%26id%3D1&VAL={'
                      '"h5_vid":"1683512239593.2hcvyj"}',
    '_bfa': '1.1683512239593.2hcvyj.1.1683512239593.1683512992180.1.10.10650057398',
    '_ubtstatus': '%7B%22vid%22%3A%221683512239593.2hcvyj%22%2C%22sid%22%3A1%2C%22pvid%22%3A10%2C%22pid%22'
                  '%3A10650057398%7D',
}

headers = {
    'Host': 'm.ctrip.com',
    # 'Cookie': 'GUID=09031067219085125642; _abtest_userid=2de85528-3112-43af-9d51-35ba9654eac4;
    # nfes_isSupportWebP=1; _bfaStatusPVSend=1; _RSG=L.q1b7h0wn3q0X2IQghGIB; _RDG=28533ab76411c225b024ec4e118bedde13;
    # _RGUID=3c7a02b1-e507-4f95-b490-aea6920a1034; _bfs=1.2; _bfi=p1%3D153002%26p2%3D10650083748%26v1%3D2%26v2%3D1;
    # cticket=5B61B782C3256A0F1B00BAD7554E11C8809A79358F23A3B66E00E55FB121282E; login_type=0;
    # login_uid=E13C9EF3D20DE1EC784E314A1F8A979B; DUID=u=463AE8FDC2C03386E055B75613598E45&v=0; IsNonUser=F;
    # AHeadUserInfo=VipGrade=30&VipGradeName=%D7%EA%CA%AF%B9%F3%B1%F6&UserName=%D0%DC%D0%C0&NoReadMessageCount=1;
    # UUID=26FE780F474A40C19EA61A9211936BF2; _bfaStatus=send;
    # Union=OUID=&AllianceID=66672&SID=1693366&SourceID=&AppID=&OpenID=&exmktID=&createtime=1683512259&Expires
    # =1684117058639; MKT_Pagesource=H5; _RF1=117.89.208.4; _pd=%7B%22_o%22%3A2%2C%22s%22%3A106%2C%22_s%22%3A0%7D;
    # MKT_code=PUSHCODE=dbiconfl&createtime=1683512992;
    # MKT_OrderClick=ASID=&AID=&CSID=&OUID=&CT=1683512992118&CURL=https%3A%2F%2Fm.ctrip.com%2Fwebapp%2Fvipwelfareapp
    # %2Fhome%3Fpopup%3Dclose%26pushcode%3Ddbiconfl%26ishidenavbar%3Dyes%26from_native_page%3D1%26s_guid%3D6fbc8ce3
    # -a8fe-43a8-97f1-eead2cd83764%26id%3D1&VAL={"h5_vid":"1683512239593.2hcvyj"};
    # _bfa=1.1683512239593.2hcvyj.1.1683512239593.1683512992180.1.10.10650057398;
    # _ubtstatus=%7B%22vid%22%3A%221683512239593.2hcvyj%22%2C%22sid%22%3A1%2C%22pvid%22%3A10%2C%22pid%22
    # %3A10650057398%7D',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'cookieorigin': 'https://m.ctrip.com',
    'content-type': 'application/json',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
    'accept': '*/*',
    'origin': 'https://m.ctrip.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://m.ctrip.com/webapp/vipwelfareapp/home?popup=close&pushcode=dbiconfl&ishidenavbar=yes'
               '&from_native_page=1&s_guid=6fbc8ce3-a8fe-43a8-97f1-eead2cd83764&id=1',
    'accept-language': 'zh-CN,zh;q=0.9',
}

params = {
    '_fxpcqlniredt': '09031067219085125642',
    'x-traceID': '09031067219085125642-1683513068091-5870817',
}

json_data = {
    'platform': 'h5',
    'contentType': 'json',
    'RightsInterestID': 2313,
    'rightsInterestCode': 'yPmW',
    'MobileType': '',
    'Position': {
        'cityID': 0,
        'cityName': '',
    },
    'head': {
        'cid': '09031067219085125642',
        'ctok': '',
        'cver': '1.0',
        'lang': '01',
        'sid': '8888',
        'syscode': '09',
        'auth': '',
        'xsid': '',
        'extension': [],
    },
}

# 早上10点准点请求
def send_request():
    res = requests.post(
        'https://m.ctrip.com/restapi/soa2/15311/json/grantRightsInterestV2',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    return res


target_time = datetime.datetime(2023, 5, 9, 10, 0, 0)
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
    dic = json['resultInformation']
    if dic['resultCode'] == 0:
        print("领取成功")
        result = False
    elif dic['resultMessage'] == '很抱歉，您已经领过了，无法重复领取':
        print('已经领过了')
        result = False
    else:
        print('领取失败, 重新领取')
        time.sleep(0.5)
