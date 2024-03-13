import requests
import json
from urllib.parse import urlparse, parse_qs
from urllib.parse import quote
import datetime
import time

cookies = {
    'deviceId': '8CCA50B3670797C8',
    'sdkVersion': '4.2.17',
}

headers = {
    'Host': 'account.xiaomi.com',
    'Accept': '*/*',
    # 'Cookie': 'deviceId=8CCA50B3670797C8; sdkVersion=4.2.17',
    'User-Agent': 'APP/com.xiaomi.youpin APPV/5.21.0 iosPassportSDK/4.2.17 iPadOS/17.2',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
}

login_headers = {
    'Host': 'account.xiaomi.com',
    'Accept': '*/*',
    # 'Cookie': 'deviceId=8CCA50B3670797C8; sdkVersion=4.2.17',
    'User-Agent': 'APP/com.xiaomi.youpin APPV/5.21.0 iosPassportSDK/4.2.17 iPadOS/17.2',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded',
}

params = {
    'sid': 'miotstore',
    '_json': 'true',
}

session = requests.Session()


def fetch_params():
    # 获取参数
    response = session.get('https://account.xiaomi.com/pass/serviceLogin', params=params, cookies=cookies,
                           headers=headers)
    json_data = convert_json(response.text)
    sign_value = json_data.get('_sign')
    location_value = json_data.get('location')
    qs_value = query_url_params(location_value, 'qs')
    # 向 Session 对象的 cookies 中添加或更新 cookies
    session.cookies.update(cookies)
    return sign_value, qs_value


def login(sign_value, qs_value, username):
    login_data = ('_json=true&hash=BDD74FB37BCAEFCC1C27EA942E9BDEC3&sid=miotstore&callback=https%3A//shopapi.io.mi.com'
                  '/app/shop/auth&_sign=') + quote(
        sign_value) + '&qs=' + quote(qs_value) + '&user=' + username
    loging_rsp = session.post('https://account.xiaomi.com/pass/serviceLoginAuth2', headers=login_headers,
                              data=login_data)
    print("------登录报文")
    print(loging_rsp.text)
    print("------\n")
    t1_json = convert_json(loging_rsp.text)
    print("------刷新获得token请求报文1")
    print(t1_json)
    print("------\n")
    temp_location1 = t1_json.get('location')
    return temp_location1


def refresh_token(location):
    refresh_header = {
        'Host': 'shopapi.io.mi.com',
        'user-agent': 'APP/com.xiaomi.youpin APPV/5.21.0 iosPassportSDK/4.2.17 iPadOS/17.2',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh-Hans;q=0.9',
    }
    # 刷新cookie
    url = location + '&clientSign=%2BT%2Bo4GZP20SMciNM7reeP7w9wCQ%3D'
    session.get(url, headers=refresh_header)

    refresh_rsp = session.get('https://account.xiaomi.com/pass/serviceLogin', params={'sid': 'miotstore',
                                                                                      '_json': 'true'}, headers=headers)
    refresh_json = convert_json(refresh_rsp.text)
    print("------刷新获得token请求报文2")
    print(refresh_json)
    print("------\n")

    refresh_location = refresh_json.get('location')
    print(refresh_location)

    # 刷新token
    url = refresh_location + '&clientSign=%2BT%2Bo4GZP20SMciNM7reeP7w9wCQ%3D'
    print(url)
    session.get(url, headers=refresh_header)
    print("-------\n")
    print(session.cookies)
    print("-------\n")


def get_activity_id():
    activity_params = {
        'spmref': 'M_H5.7346.158793.1.20248391'
    }
    activity_cookies = {
        'youpin_sessionid': '18cf80cf772-03fe0fdace6b098-17c8',
        'youpindistinct_id': '18ce8146fce-0025113ace58358-17c8',
        'mjclient': 'PC',
    }
    activity_headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Referer': 'https://m.xiaomiyoupin.com/w/universal?_rt=weex&pageid=7346&sign=a407cb71c12b9973be2bcc72d8ce5cc4',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }
    activity_response = requests.get('https://m.xiaomiyoupin.com/mr/5fa529d1c9e77c000148d30f', params=activity_params,
                                     headers=activity_headers, cookies=activity_cookies, allow_redirects=False)
    activity_id = query_url_params(activity_response.headers["Location"], 'actId')
    return activity_id


def join(activity_id):
    json_data = [
        {},
        {
            'actId': activity_id,
            'tel': '17895003078',
        },
    ]
    join_header = {
        'Host': 'm.xiaomiyoupin.com',
        'content-type': 'application/json',
        'yp-srt': '1704711637163',
        'yp-srs': '439418079',
        'yp-ss': 'EE7AABDDC10EAB4A9AE6755D599B16CE',
        'accept': 'application/json',
        'x-requested-with': 'XMLHttpRequest',
        'sec-fetch-site': 'same-origin',
        'accept-language': 'zh-CN,zh-Hans;q=0.9',
        'sec-fetch-mode': 'cors',
        'origin': 'https://m.xiaomiyoupin.com',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                      'like Gecko) Mobile/15E148 MIOTStore/20191212 (YouPin;5.21.0;('
                      'null);;I;00000000-0000-0000-0000-000000000000;;;727E65F9-49FC-5CE8-9378-3247C14A5624) '
                      'APP/com.xiaomi.youpin APPV/5.21.0 iosPassportSDK/4.2.17 '
                      'iPadOS/17.2/XiaoMi/MiuiBrowser/4.3/Shop/ios/iPad8,6/4.5.91',
        'referer': 'https://m.xiaomiyoupin.com/app/shop/ugg/subscribeBuy.html?actId=6593ec0fbe07770001a8c931&spmref'
                   '=YouPin_I.7346.158793.1.50203032',
        'sec-fetch-dest': 'empty',
    }
    session.cookies.update({'mjclient': 'YouPin'})
    join_cookies = {
        'mjclient': 'YouPin',
        'serviceToken': session.cookies['miotstore_serviceToken']
    }
    params3 = {
        '_': get_current_time()
    }
    response = session.post(
        'https://m.xiaomiyoupin.com/mtop/act/orderspike/order',
        params=params3,
        headers=join_header,
        cookies=join_cookies,
        json=json_data,
    )
    print(response.text)


def get_current_time():
    # 获取当前时间的毫秒表示
    current_time_milliseconds = int(datetime.datetime.timestamp(datetime.datetime.now()) * 1000)
    # 将毫秒表示转换为字符串
    return str(current_time_milliseconds)


def xiaomi_prepare():
    print("第一步，先获得请求参数")
    request_param = fetch_params()
    sign_value = request_param[0]
    qs_value = request_param[1]
    # 登录
    print("第二步，登录, 拿到url")
    temp_location1 = login(sign_value, qs_value, '15951003078')
    # 刷新ck
    refresh_token(temp_location1)
    # 获取活动ID
    activity_id = get_activity_id()
    return activity_id


def xiaomi_schedule():
    # 报名
    join(xiaomi_prepare())
    # xiaomi_buy()

def xiaomi_request(activity_id):
    buy_headers = {
        'Host': 'm.xiaomiyoupin.com',
        'referer': 'https://m.xiaomiyoupin.com/app/shop/ugg/subscribeBuy.html?actId=%s&spmref'
                   '=YouPin_I.7346.158793.1.2361007' % activity_id,
        'c': '6',
        'x-requested-with': 'XMLHttpRequest',
        'd': '55',
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                      'Mobile/15E148 MIOTStore/20191212 ('
                      'YouPin;5.21.0;8CCA50B3670797C8;;I;00000000-0000-0000-0000-000000000000;;8CCA50B3670797C8'
                      ';9856B8A2-D037-59B9-B6C6-54F126814DE0) APP/com.xiaomi.youpin APPV/5.21.0 iosPassportSDK/4.2.17 '
                      'iPadOS/17.2/XiaoMi/MiuiBrowser/4.3/Shop/ios/iPad8,6/4.5.91',
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
    buy_params = {
        '_': get_current_time(),
    }
    buy_json = [
        {},
        {
            'actId': activity_id,
            'token': activity_id,
        },
    ]
    response = session.post(
        'https://m.xiaomiyoupin.com/mtop/act/orderspike/ekips00',
        params=buy_params,
        cookies=cookies,
        headers=buy_headers,
        json=buy_json,
    )
    return response


def convert_json(text):
    print("解析json，内容为是" + text + "\n")
    # 移除 '&&&START&&&'
    data_without_start = text.replace('&&&START&&&', '')
    # 解析 JSON 数据
    json_data = json.loads(data_without_start)
    return json_data


def query_url_params(url, param):
    # 使用 urllib.parse 中的 urlparse 和 parse_qs 函数来解析 URL 中的查询参数
    parsed_url = urlparse(url)
    parsed_params = parse_qs(parsed_url.query)
    qs_value = parsed_params.get(param)[0]
    return qs_value


def xiaomi_buy():
    target_time = datetime.datetime(2024, 2, 27, 10, 0, 0)
    activity_id = xiaomi_prepare()
    time_diff = (target_time - datetime.datetime.now()).total_seconds()
    if time_diff > 0:
        time.sleep(time_diff)
    count = 2

    while count >= 0:
        response = xiaomi_request(activity_id)
        print(response.text)
        count -= 1
        if response.status_code != 200:
            print('请求失败')
            time.sleep(0.2)
            continue
        resp_json = response.json()
        data = resp_json['data']['success']
        print(data)
        if data:
            print("领取成功")
            exit()
        elif not data:
            print("本场已抢光，下场再来吧")
            time.sleep(0.4)
        else:
            print('领取失败, 重新领取')
            time.sleep(0.4)

xiaomi_schedule()