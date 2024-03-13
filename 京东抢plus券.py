import requests
import time
import datetime


cookies = {
    '__jda': '165946495.1709528223499522069957.1709528223.1709528223.1709530418.2',
    '__jdv': '122270672%7Cdirect%7C-%7Cnone%7C-%7C1709528223499',
    '__jdc': '165946495',
    'shshshfpa': '65101128-16de-7757-61d7-8534154b6058-1709528223',
    'shshshfpx': '65101128-16de-7757-61d7-8534154b6058-1709528223',
    'shshshfpb': 'BApXeYIn8BOtA5r845JmZ49Me7EOujdGCBksThQxu9xJ1Mhxv-IO2',
    'jcap_dvzw_fp': 'M--Mo_PjodLAbOPMrnpd24dezMIJIQR9a5CLoVDv5KSS6YyvaCVwK8mvwk9KmHfr1F49zFUSzxm3R3FMNyxFQw==',
    '__jdu': '1709528223499522069957',
    'areaId': '12',
    'ipLoc-djd': '12-904-0-0',
    '3AB9D23F7A4B3CSS': 'jdd03VRGLVSOMLDWYIYHL3V4E6VLEXRIFFMXRAKX22222NKJUBYPAVWCQ2OGP4UL27VAWIC2AIALCW3ERZRCYZECHIZ6KLEAAAAMOA72Q5BYAAAAADS6IJ2EIJ3EOM4X',
    'PCSYCityID': 'CN_320000_320100_0',
    'TrackID': '1RnJz_oOWUPGTJ0j3rjsiGxHtb24NTcdwPtMZI3eMEp6b8sMzryNrk7sPo_7L4hywgvZujnDXg1HQZ_zTVghBnEslT6dq58yi7OqTKFyldEUCWFP8MS-aYBmMgXkYfycwI6jGwEHfAJakEqws3xJiFw',
    'thor': 'D722FD6AA8EAAECCEF3E684776707C7DA9C3E38875EE02D75B38EDEF70EDEAF627AB4B53A9AC431F3BABE54427A0FAFFA036DAEA18D40FBA4E517132F88F0201D8FADC1B70F6B9A11BB0822FC52BAC107F16B4F63C5E13CF5B612839950239BFB58FC35BC00526E6036300530EB68D30DAECEC8687DD83A2BC9E531C539D5ED2EB356ACB2B9EB91F1EEFC2BB9618BF413663A30411E575EF635135319FB02454',
    'flash': '2_N3xjiYHt7lc1SutwXC7DaZM8xFeyPxfwm3JH62QjfN4Qw8gTKaX7lV6FYhTT8add3BSvwNDBamB0iiJJJkH1YOjTNNNdZHHuE-AGDPkkWQe*',
    'pinId': '7JO5GEhhODJIi3Oh5-DqmLV9-x-f3wj7',
    'pin': 'jd_7aa9586c0aeb5',
    'unick': 'jd_153660rjcv',
    'ceshi3.com': '201',
    '_tp': '3a8Tp8VzkImjyB1fRKmuRNnf9LknLkQv74x4meNdnNs%3D',
    '_pst': 'jd_7aa9586c0aeb5',
    'mba_muid': '1709528223499522069957',
    '3AB9D23F7A4B3C9B': 'VRGLVSOMLDWYIYHL3V4E6VLEXRIFFMXRAKX22222NKJUBYPAVWCQ2OGP4UL27VAWIC2AIALCW3ERZRCYZECHIZ6KLE',
    'whwswswws': '',
    '__jdb': '165946495.5.1709528223499522069957|2.1709530418',
    'mba_sid': '17095304231851497313749431005.4',
    'TrackerID': 'sTzl3YSTnrB_u2hgmaGc87QvU5dazOIlDKfGgOjBnwIYp0JOzmQhj1_nOWeDIFMSFrO1be6qIMi1T3gTY_OVtwYzCno143ydk5b4VbeHVSFb-LpaB7a8rJ_FtLHvno2ynH0DPyw9bubcg2woCyvOvQ',
    'pt_key': 'AAJl5V1gADAgabqPEpDJQBFrru2vZOBSGn11uTY7wrycZSqiX53lm-smphz5TVk9vP5rcFB7F08',
    'pt_pin': 'jd_7aa9586c0aeb5',
    'pt_token': '3ojbc3av',
    'pwdt_id': 'jd_7aa9586c0aeb5',
    'sfstoken': 'tk01mb53e1c58a8sMSsyeDNIYzM4o5MTE1bqyilkHKT310W9VCNBxpzWFLFOg7meSWQflgWAmWllxoCoTZeJ4w0fN/5b',
    'wxa_level': '1',
    'retina': '1',
    'cid': '9',
    'wqmnx1': 'MDEyNjM5MXRqNzM5NW50UzswMkYycmE0MU8jKQ%3D%3D',
    'jxsid': '17095304669439908303',
    'appCode': 'ms0ca95114',
    'webp': '1',
    'visitkey': '7589086153636930459',
    'p-request-id': 'jd_7aa9586c0aeb52024030413a6Kv9NOI1D',
    '__jd_ref_cls': 'MPlusCoupon_BackTopExpo',
    '_gia_d': '1',
}


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Referer': 'https://plus.m.jd.com/coupon/index',
    'x-referer-page': 'https://plus.m.jd.com/coupon/index',
    'x-rp-client': 'h5_1.0.0',
    'Origin': 'https://plus.m.jd.com',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
}

params = {
    'functionId': 'coupon_receiveDayCoupon_v2',
    'loginType': '2',
    'loginWQBiz': '',
    'appid': 'plus_business',
    'body': '{"batchId":1107257417,"platform":3,"eventId":"MPlusCoupon_Get",'
            '"eid":"VRGLVSOMLDWYIYHL3V4E6VLEXRIFFMXRAKX22222NKJUBYPAVWCQ2OGP4UL27VAWIC2AIALCW3ERZRCYZECHIZ6KLE",'
            '"fp":"65352cb85a1e41bf5ca71d676e54b623","activityId":"qyb_1061"}',
    'scval': '',
    '_': '1709481608436',
}

# 早上10点准点请求
def send_request():
    res = requests.get('https://api.m.jd.com/api', params=params, cookies=cookies, headers=headers)
    print(res.text)
    return res



target_time = datetime.datetime(2024, 3, 4, 16, 0, 0)
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
    rspCode = json['code']
    if rspCode == "1760001":
        print("领取成功")
        result = False
    elif rspCode == "1760010":
        print("本场已抢光，下场再来吧")
        exit()
    else:
        print('领取失败, 重新领取')
        time.sleep(0.4)
