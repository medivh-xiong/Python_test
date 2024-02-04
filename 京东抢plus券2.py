import requests
import time
import datetime

cookies = {
    '__jda': '122270672.1706062432561453409376.1706062432.1706062432.1706062432.1',
    '__jdb': '122270672.3.1706062432561453409376|1.1706062432',
    '__jdv': '122270672%7Cdirect%7C-%7Cnone%7C-%7C1706062432561',
    '__jdc': '122270672',
    'mba_muid': '1706062432561453409376',
    'shshshfpa': '2a6cc904-3119-3bf9-5fab-9f4b9bc1a345-1706062432',
    'shshshfpx': '2a6cc904-3119-3bf9-5fab-9f4b9bc1a345-1706062432',
    'mba_sid': '17060624327198755600049488490.3',
    'shshshfpb': 'BApXe-Fw2OuhAmmcUw17VTe1i9jwgBxKfBkRHIx1o9xJ1MtxJrYO2',
    'jcap_dvzw_fp': 'rW5EtQI21nb1yJ4hPffbftzVnplvSeycT0_xwB4ewVoPdqJWjz9Wquw_C4Vh5XuNYKTjKlI1X-IDaQeOR1FAuw==',
    'TrackerID': 'zJWHwQDpoiDOOsDNkZeJNR0yBxbaD7fyp2YODbE80nG_BueVLhKR7Q4hbF8NdvXQTHdjpYBvB1Zhf73NliySCFrQvPJwAuWX8zz8zzlyrr8JHa8ge-7n3_HEYDgDB9Jgm2akeK7yNgFW35K8nu61hQ',
    'pt_key': 'AAJlsHK3ADByG_17HzOjS_xDHQfxpGV5TzpxwTzhx6AiGZV0auCsEpjbjnBGmxNre93PF8ydTJA',
    'pt_pin': '15951003078_p',
    'pt_token': 'wp4ic022',
    'pwdt_id': '15951003078_p',
    'sfstoken': 'tk01mee5d1deda8sMngxTk9TM3BUHffxWnOomIaKnMFaowJcJcPxdmmsV/w2mAsVZnj01xtcReXUUoPn9EIpIrfRmhgW',
    'whwswswws': '',
    'p-request-id': '15951003078_p2024012410E2iMytZz6L',
    'wxa_level': '1',
    '3AB9D23F7A4B3CSS': 'jdd037XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4AAAAMNHFACB7QAAAAADE3KZRJH7HGKSMX',
    '3AB9D23F7A4B3C9B': '7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4',
    '__jd_ref_cls': 'MPlusCoupon_Confirm',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://plus.m.jd.com/coupon/index',
    'content-type': 'application/x-www-form-urlencoded',
    'x-referer-page': 'https://plus.m.jd.com/coupon/index',
    'x-rp-client': 'h5_1.0.0',
    # 'Content-Length': '0',
    'Origin': 'https://plus.m.jd.com',
    'DNT': '1',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    # 'Cookie': '__jda=122270672.1706062432561453409376.1706062432.1706062432.1706062432.1; __jdb=122270672.3.1706062432561453409376|1.1706062432; __jdv=122270672%7Cdirect%7C-%7Cnone%7C-%7C1706062432561; __jdc=122270672; mba_muid=1706062432561453409376; shshshfpa=2a6cc904-3119-3bf9-5fab-9f4b9bc1a345-1706062432; shshshfpx=2a6cc904-3119-3bf9-5fab-9f4b9bc1a345-1706062432; mba_sid=17060624327198755600049488490.3; shshshfpb=BApXe-Fw2OuhAmmcUw17VTe1i9jwgBxKfBkRHIx1o9xJ1MtxJrYO2; jcap_dvzw_fp=rW5EtQI21nb1yJ4hPffbftzVnplvSeycT0_xwB4ewVoPdqJWjz9Wquw_C4Vh5XuNYKTjKlI1X-IDaQeOR1FAuw==; TrackerID=zJWHwQDpoiDOOsDNkZeJNR0yBxbaD7fyp2YODbE80nG_BueVLhKR7Q4hbF8NdvXQTHdjpYBvB1Zhf73NliySCFrQvPJwAuWX8zz8zzlyrr8JHa8ge-7n3_HEYDgDB9Jgm2akeK7yNgFW35K8nu61hQ; pt_key=AAJlsHK3ADByG_17HzOjS_xDHQfxpGV5TzpxwTzhx6AiGZV0auCsEpjbjnBGmxNre93PF8ydTJA; pt_pin=15951003078_p; pt_token=wp4ic022; pwdt_id=15951003078_p; sfstoken=tk01mee5d1deda8sMngxTk9TM3BUHffxWnOomIaKnMFaowJcJcPxdmmsV/w2mAsVZnj01xtcReXUUoPn9EIpIrfRmhgW; whwswswws=; p-request-id=15951003078_p2024012410E2iMytZz6L; wxa_level=1; 3AB9D23F7A4B3CSS=jdd037XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4AAAAMNHFACB7QAAAAADE3KZRJH7HGKSMX; 3AB9D23F7A4B3C9B=7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4; __jd_ref_cls=MPlusCoupon_Confirm',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'functionId': 'coupon_receiveDayCoupon_v2',
    'loginType': '2',
    'loginWQBiz': '',
    'appid': 'plus_business',
    'body': '{"platform":3,"eventId":"MPlusCoupon_Get","eid":"7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4","fp":"1b71d176f07e708abbd5814e5fccf15a","activityId":"qyb_1052"}',
    'scval': '',
    '_': '1685522971069',
}

# 早上10点准点请求
def send_request():
    res = requests.get('https://api.m.jd.com/api', params=params, cookies=cookies, headers=headers)
    print(res.text)
    return res

target_time = datetime.datetime(2023, 11, 10, 16, 0, 0)
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
    rspCode = json['code']
    if rspCode == "1760001":
        print("领取成功")
        count = -1
        result = False
    elif rspCode == "1760010":
        print("本场已抢光，下场再来吧")
        exit()
    else:
        print('领取失败, 重新领取')
        time.sleep(0.4)
