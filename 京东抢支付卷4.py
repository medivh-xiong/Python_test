import requests
import time
import datetime





cookies = {
    'wxa_level': '1',
    'retina': '1',
    'cid': '9',
    'wqmnx1': 'MDEyNjM2MnRjLmN1c2NseUhmbm9JVUFZRVdOMF85bCZqMTU3OHo1YXN0YyA7MkcyMGUyMllhLTQxUlMjISk%3D',
    'jxsid': '17085815048459199023',
    'appCode': 'ms0ca95114',
    'webp': '1',
    '__jda': '122270672.17085815051151983555208.1708581505.1708581505.1708581505.1',
    '__jdb': '122270672.4.17085815051151983555208|1.1708581505',
    '__jdv': '122270672%7Cdirect%7C-%7Cnone%7C-%7C1708581505115',
    '__jdc': '122270672',
    'mba_muid': '17085815051151983555208',
    'mba_sid': '17085815051195355840043875384.4',
    'visitkey': '7745328847350038908',
    '__wga': '1708581554378.1708581505980.1708581505980.1708581505980.3.1',
    'PPRD_P': 'UUID.17085815051151983555208',
    '3AB9D23F7A4B3CSS': 'jdd035NVHGAFE7P6UELD7LOWB3ERFPQOIYJYZXBLIX3QJU7G3Y6M3NE5BMM63LDMU5ST5C4HXFQTZK5HHE5WZSIRGPW6PJIAAAAMNZ5SMZ4IAAAAACPT4Y7MIQM65ZAX',
    '3AB9D23F7A4B3C9B': '5NVHGAFE7P6UELD7LOWB3ERFPQOIYJYZXBLIX3QJU7G3Y6M3NE5BMM63LDMU5ST5C4HXFQTZK5HHE5WZSIRGPW6PJI',
    '_gia_d': '1',
    'shshshfpa': 'cd618118-2bda-81d6-7be0-942f9bbcd9eb-1708581524',
    'shshshfpx': 'cd618118-2bda-81d6-7be0-942f9bbcd9eb-1708581524',
    'shshshfpb': 'BApXeYYBtzOhAly8I2Z1vYskp_VggemgxBkoZEgto9xJ1MinZy4O2',
    'jcap_dvzw_fp': 'S66JuqVW4kotWdEz3nkH7QAFJYSYTnD4KIhCggJDPxzheRv6K3HWPJXzNLrbq4Ft2dZBUyZHmsbhDCoTODlW1w==',
    'TrackerID': 'ydKG2rZNfmU_zJLBJNwln1vvVkzs4wSYAbqRY7Z6kzhALnHqbBQC_w3D-7-Y61dCwqN86z_NY23Wi8FFi0yJXlQdXl6cYfqvfPLPQ3XGSJoaz4nd2-X4dhvR4uKstC_8VAiaqZZFP8LZI62KNlw2Ww',
    'pt_key': 'AAJl1uKxADA5KU4-wn9dTUzN5oj0RV0XPt3P1hrXRI1cmpfTjGynLpthIAjTbK98xp3V-_Ckkzc',
    'pt_pin': 'jd_GemiSgxMUvhg',
    'pt_token': 'qmt9bnsl',
    'pwdt_id': 'jd_GemiSgxMUvhg',
    'sfstoken': 'tk01me32e1d59a8sM3gzKzJ4Mngxrm+A1/ubp4ydbWkcxKHrZwkaHzz3qboGr7+mp5qgJ7AWVkRydJNq7oXPNW9NvUAo',
    'whwswswws': '',
    '__jd_ref_cls': 'MProductCoupon_WaitGetCoupon',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:122.0) Gecko/20100101 Firefox/122.0',
    'Accept': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'x-referer-page': 'https://coupon.m.jd.com/coupons/show.action',
    'x-rp-client': 'h5_1.0.0',
    'Origin': 'https://coupon.m.jd.com',
    'Connection': 'keep-alive',
    'Referer': 'https://coupon.m.jd.com/',
    # 'Cookie': '__jda=181111935.1668069089029464342293.1668069089.1708570714.1708580176.238; b_dw=1905; b_dh=942; b_dpr=2; b_webp=1; b_avif=1; shshshfpb=BApXev7ODzehA5kVcheQqbPiQ8NWkO6NcBypHl75X9xJ1MhsrroO2; shshshfp=b6ec8c37a67e0e37fd7f25ffacb1dc2b; shshshfpa=3910eb4c-77a3-c4d8-4a59-99a21ffd1286-1668069091; jcap_dvzw_fp=MStjxvc74o8PNBQNWwvkqMy4UUC2oFU3mziJBO7xwNEc-qWJfCkVnJtoSp00zaKo8Gu2BA==; __jdu=1668069089029464342293; shshshfpx=3910eb4c-77a3-c4d8-4a59-99a21ffd1286-1668069091; 3AB9D23F7A4B3CSS=jdd037XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4AAAAMNZ5IIJQYAAAAACQSE75TBE53IRYX; unpl=JF8EAKhnNSttWR5SAxICExZDSFxWW1hYS0QAO2YNXVpcS1UFG1VJFBd7XlVdWBRKFB9sZBRUXFNKVQ4eAisSEHtdVV9dD0MTA2hkNWRdWUpUBBwLGBsSe15Ublw4SxAEZmYCXFxRQ1UGEwccFxJOXldWXzhKJwNnYDVkbVl7VAQbAxMiEktcVV9YDk8TC18sa1UQWExTDBoFExMZQ1xXVlgPThUGbGQNVm1Ze1c; pinId=9zvM1MUZPR30TcKyARJfCQ; whwswswws=; TrackID=1qzgjq5pK4vuM12LfiEvxuS_7rEXiKO8eEeUfPmOPfhtO5lzVWG5e1RIiHFY0R7TA0sKxHcxnn4Fv96zSoaINJgG85dIoc9m5Pdl18ZJkE6Aa8buB0GsYoqlTkCTj-Wbj; ipLoc-djd=12-904-907-50559; pin=15951003078_p; unick=%E5%86%A5%E7%8E%8B%E4%B9%8B%E6%AD%8C; _tp=ak3bQDgGku8%2BskP5GCRaiw%3D%3D; _pst=15951003078_p; warehistory="10085827003737,100064695864,100064695864,10081479480401,10081479480401,100066206148,10086397575079,10091517815466,100068431529,100058134266,100035340746,"; mba_muid=1668069089029464342293; joyya=1708567241.1708567242.61.0m7w6p6; retina=1; cid=9; webp=1; visitkey=737803510179678; equipmentId=7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4; fingerprint=808f4ae16c15d708044b42078e6b45d9; deviceVersion=122.0; deviceOS=; deviceOSVersion=; deviceName=Firefox; __wga=1708580176345.1708580176345.1708570714961.1706755024545.1.4; sc_width=1920; __jdv=181111935%7Ckong%7Ct_1001695162_%7Cjingfen%7C0d778195b20344a1b2e098651011fc76%7C1708567241426; areaId=12; wxa_level=1; jxsid=17085054438780613147; PPRD_P=EA.17053.1.1-UUID.1668069089029464342293; thor=BF80140138890A11F2001240DE13FB3F3C61C0880504BFA8A1E9BDE57F39C654446FCF0B0368B1B87ECB49154D3FA9771981E851793FBC2F1BC369F2284164BDCF5F6F604977DC2AFC32B2AF7BEA92CAC927790641C26AE2D827E958FCDE3A69CAA21D9483485E5BC1B26112362198F0D30BEC08B16BFC3408AA913CB86F8D9968A0F50371768AD1D15A7626F6F588BC; flash=2_Y-yYDSx4OkxRGgtBchJT9K6hmP8Xl6qQACgpqh9P2dOSZ0dLY1gL9etUsnPSm2S9irep3t6nTE2UlDPWZnS5_F6PFEoDxrt0B4NfQhN0CPN*; TARGET_UNIT=bjcenter; ceshi3.com=201; __jdc=181111935; wlfstk_smdl=e8i1new46uubar3ioih4ul9532oibmup; appCode=ms0ca95114; qid_uid=65b042c2-e30b-4c1b-a6df-9243cc568239; qid_fs=1708564603236; qid_ls=1708564603236; qid_ts=1708564603239; qid_vis=1; 3AB9D23F7A4B3C9B=7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4; mba_sid=17085801288097830269465466998.1; wqmnx1=MDEyNjM1M3BjbmQvb2hjP0tBeGZuRnFLaHBZeUJqMWZfQWxBb2QxNzE2ei8objtlY1gxdi5lMjFpeC4zWWRmNDNWUkRGSCZS; __jdb=181111935.1.1668069089029464342293|238.1708580176; __jd_ref_cls=MProductCoupon_WaitGetCoupon; _gia_d=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}


params = {
    'appid': 'h5_awake_wxapp',
    'functionId': 'mcoupon_getcoupon',
    'client': 'wh5',
    't': '1708580187047',
    'body': '{"key":"","roleId":"","linkKey":"AAROH_xIpeffAs_-naABEFoeoCqcIYiKXTUWhpdGApbv7QYn43CyEn77B7WJ_jt8Nc1u4Z0fg0fu_EpnxA91v5lBlknAmw","to":"m.jd.com","venderid":""}',
    '_stk': 'appid,body,client,functionId,t',
    '_ste': '1',
    'h5st': '20240222133627064;t6tmn6hq5nt6klk1;27abe;tk03w79a11b3b18nC1PD2Spds4VT2AQPfIl0_b-YnTmaqyo6Re_UHB4F18-VTmjDN9w0nnXmxVbJRz0fVX-EzYV0G8tR;59fdcbf659f3a63aed2476e9c731aa47c3646d80944f4e7899b3c6040dd31684;4.3;1708580187064;6ab648016f4b18e308deb8189a91955075b82204fe1f5a3e2d017a46737552fa1b5c10b259f21644f0374719ac308aa52382eda65bf97eed4658bbf35cb73194e19a4f8b4d55160ac0292cca6b1e2c90786e5ae2735f7074f9041cf85cf9d97442532c9bde5164bfdd65db72fbe3e5f9641d227b565967aa7d6911c55f0fc7697069bf8f27ded9c09f61ca35b08f1bd819d55ee0a3c7b7886ae91b2676c2c02c25ab4eb79e136265876271fd09dac099c97c524f0286745227fb031a6cc14aca47026b0bcb7003422f4bef7509b97cae75bf41d13a0784e5711a790e766bca62bd5231f353fe7b84db4d1f8d3b9e79645940104f971822397f4380a4b0d6486f302a5ab283a1a6ea77ba81f27e81cff3e633d7192bed706cbcee7b855a91f231628ddd85bdd9caba1a1a75149e1e8988f3fbbf02a4a73690bef26ac80a605d98',
    'x-api-eid-token': 'jdd037XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4AAAAMNZ5IIJQYAAAAACQSE75TBE53IRYX',
    '_': '1708580187066',
    'sceneval': '2',
    'g_login_type': '1',
    'appCode': 'ms0ca95114',
    'g_ty': 'ajax',
}

def send_request():
    res = requests.get('https://api.m.jd.com/client.action', params=params, cookies=cookies, headers=headers)
    print(res.text)
    return res

target_time = datetime.datetime(2024, 2, 22, 14, 0, 0,  0)
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
    if response.text.find('本时段优惠券已抢完') != -1:
        print("本场已抢光，下场再来吧")
        exit()
    elif response.text.find('您已经参加过此活动') != -1:
        print("结束")
        exit()
    else:
        print('领取失败, 重新领取')
        time.sleep(0.3)
