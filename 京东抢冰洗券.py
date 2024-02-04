import requests
import time
import datetime


cookies = {
    '__jda': '122270672.1668069089029464342293.1668069089.1701680522.1701828983.187',
    'b_dw': '1902',
    'b_dh': '942',
    'b_dpr': '2',
    'b_webp': '1',
    'b_avif': '1',
    'shshshfpb': 'AAlax9jyMEhDrTHejxNhKWZmiH_0ShhZoBpCRfwAAAA0xNTk1MTAwMzA3OF9w',
    'shshshfp': 'b6ec8c37a67e0e37fd7f25ffacb1dc2b',
    'shshshfpa': '3910eb4c-77a3-c4d8-4a59-99a21ffd1286-1668069091',
    'jcap_dvzw_fp': 'MStjxvc74o8PNBQNWwvkqMy4UUC2oFU3mziJBO7xwNEc-qWJfCkVnJtoSp00zaKo8Gu2BA==',
    '__jdu': '1668069089029464342293',
    'shshshfpx': '3910eb4c-77a3-c4d8-4a59-99a21ffd1286-1668069091',
    '3AB9D23F7A4B3CSS': 'jdd037XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4AAAAMMHT23RWYAAAAADBPNG5HE5EVPNAX',
    'unpl': 'JF8EAMJnNSttD05cVR4HHEYYGwoDW1sLQ0dXPWBSU1lZHlEBHVccEEV7XlVdXxRLFB9uYhRUW1NKVw4aAisSEXtdVV9cCUIfCmdlNVRZXyVVaxsLHnx-G11TWQlbHEcFZjdXAQlQS2Q1GAIrEyBLWlNXXA9DFgpnZgZcWF9OVgAYARMQIEptVFZZOEsWAmZgBVRZW0NdAhgGKyIUTV5SWlwJShQzblcEZBY2ShkFHAUSExdDXF1WXAtDEgRqZQBXXlBJZAQrAQ',
    'pinId': '9zvM1MUZPR30TcKyARJfCQ',
    'whwswswws': '',
    'TrackID': '15Zlchf3ZmGOuIZzlTBLnnQThOSADPxmY6TkfYPXEbT_-ZR9x30nZHC12LotQn75HLLj7JXzzAGqjwrfO_DnX3gOyVu2e3EQvkMiPuvAKuAwXcMvwKq3dD_Oq8_xzIWeW',
    'qid_uid': '92095ee1-5b27-46be-8b6a-1bc810458c13',
    'qid_fs': '1686190520449',
    'qid_ls': '1686190520450',
    'qid_ts': '1699607456636',
    'qid_vis': '2',
    'mba_muid': '1668069089029464342293',
    'joyya': '1699610422.1699610422.72.0gi2j80i6',
    'visitkey': '737803510179678',
    'TrackerID': 'c9-FFuYaVRkgDliG8zgV4dFq7plaedViMFU8NL1KNYgIwCW2tcOgTyFD9Na-j5wcGOY8WAEVRXjEnG6ypT6ZApEyltwAni-g1Gm7w-ANJ6Qs0uzicdRBd2rt34Kb0dkOErtzr3IdH4UTP5pZSDpq-A',
    'cid': '9',
    'retina': '1',
    'webp': '1',
    '__wga': '1701829849046.1701828996065.1701067667008.1690941155328.4.18',
    '__jdv': '122270672|www.linkstars.com|t_1000089893_156_0_184__a166ebfa78acde91|tuiguang|f49a446e9aff4729aec6f650d457d63d|1701680526613',
    'ipLoc-djd': '12-904-907-50559',
    'pin': '15951003078_p',
    'unick': '%E5%86%A5%E7%8E%8B%E4%B9%8B%E6%AD%8C',
    '_tp': 'ak3bQDgGku8%2BskP5GCRaiw%3D%3D',
    '_pst': '15951003078_p',
    'warehistory': '"10091517815466,100068431529,100058134266,100035340746,"',
    'equipmentId': '7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4',
    'fingerprint': 'fa88edb26806f6bacfa75d54b30b53f8',
    'deviceVersion': '120.0',
    'deviceOS': '',
    'deviceOSVersion': '',
    'deviceName': 'Firefox',
    'sc_width': '1920',
    'areaId': '12',
    '3AB9D23F7A4B3C9B': '7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4',
    'thor': 'BF80140138890A11F2001240DE13FB3F3C61C0880504BFA8A1E9BDE57F39C6545B0BF4C6C21D32156BC98C736F4464D10776E3795FBB91D349D4ACFE0711B5C6DAE2FF594B86E1166072FC25012ECF15459145CE6D5D66BAA8A5D22DA31A07D8B3C8B4A673A3E7233FA11CF90F01F647C6A7D80CF3BDA2960FD141BB435664F3759D36BA7992D641C944D48FFA05E0FE',
    'flash': '2_OWTzgfZjyYwLuvimc-Iw6rIgZe4EB-b2nqZHyMkY0Pa56coRy4alnA08lSl-hnHNltVzekspyioCb72B5cboQGWmtlhkPnGNnPK31c6gE6s*',
    'TARGET_UNIT': 'bjcenter',
    'cn': '5',
    'ceshi3.com': '201',
    'wlfstk_smdl': 'nrmxjlejnqd9ou6q2y4ubb7nbpvyutzh',
    'p-request-id': '15951003078_p2023111016bfdq5Tez4v',
    'share_cpin': '',
    'share_open_id': '',
    'share_gpin': '',
    'shareChannel': '',
    'source_module': '',
    'erp': '',
    'appCode': 'ms0ca95114',
    'plusCustomBuryPointToken': '1698131788185_4020',
    '__jdc': '122270672',
    '__jdb': '122270672.8.1668069089029464342293|187.1701828983',
    'mba_sid': '17018289839268268800914776656.8',
    'wxa_level': '1',
    'wqmnx1': 'MDEyNjM3NHNwZG9zdHlkNDgxcjE1LiYzNTF1MDJtODE3MW81YzsgIDUyZTFGLzRZZi00WUQjKEg%3D',
    'jxsid': '17018289959745092554',
    'PPRD_P': 'UUID.1668069089029464342293',
    'jxsid_s_t': '1701829849061',
    'jxsid_s_u': 'https%3A//coupon.m.jd.com/coupons/show.action',
    '_gia_d': '1',
    'pt_key': 'AAJlb9zXADA9AbRpjfqBvdqwt8D8xljlEfaEjmdDETiec3NsBU6EOJf4V3w8_BQjVg0kq_R4y1I',
    'pt_pin': '15951003078_p',
    'pt_token': '7xmyw9hl',
    'pwdt_id': '15951003078_p',
    'sfstoken': 'tk01maa671c2da8sMngyKzErM09kaCKF+FQGpKu9JFn+bjD5lqTcXxXpMhmEd9s8Wa3Bz2/R5rQBv2OjGoiOJvRDevcT',
    '__jd_ref_cls': 'MProductCoupon_WaitGetCoupon',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Accept': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'x-referer-page': 'https://coupon.m.jd.com/coupons/show.action',
    'x-rp-client': 'h5_1.0.0',
    'Origin': 'https://coupon.m.jd.com',
    'Connection': 'keep-alive',
    'Referer': 'https://coupon.m.jd.com/',
    # 'Cookie': '__jda=122270672.1668069089029464342293.1668069089.1701680522.1701828983.187; b_dw=1902; b_dh=942; b_dpr=2; b_webp=1; b_avif=1; shshshfpb=AAlax9jyMEhDrTHejxNhKWZmiH_0ShhZoBpCRfwAAAA0xNTk1MTAwMzA3OF9w; shshshfp=b6ec8c37a67e0e37fd7f25ffacb1dc2b; shshshfpa=3910eb4c-77a3-c4d8-4a59-99a21ffd1286-1668069091; jcap_dvzw_fp=MStjxvc74o8PNBQNWwvkqMy4UUC2oFU3mziJBO7xwNEc-qWJfCkVnJtoSp00zaKo8Gu2BA==; __jdu=1668069089029464342293; shshshfpx=3910eb4c-77a3-c4d8-4a59-99a21ffd1286-1668069091; 3AB9D23F7A4B3CSS=jdd037XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4AAAAMMHT23RWYAAAAADBPNG5HE5EVPNAX; unpl=JF8EAMJnNSttD05cVR4HHEYYGwoDW1sLQ0dXPWBSU1lZHlEBHVccEEV7XlVdXxRLFB9uYhRUW1NKVw4aAisSEXtdVV9cCUIfCmdlNVRZXyVVaxsLHnx-G11TWQlbHEcFZjdXAQlQS2Q1GAIrEyBLWlNXXA9DFgpnZgZcWF9OVgAYARMQIEptVFZZOEsWAmZgBVRZW0NdAhgGKyIUTV5SWlwJShQzblcEZBY2ShkFHAUSExdDXF1WXAtDEgRqZQBXXlBJZAQrAQ; pinId=9zvM1MUZPR30TcKyARJfCQ; whwswswws=; TrackID=15Zlchf3ZmGOuIZzlTBLnnQThOSADPxmY6TkfYPXEbT_-ZR9x30nZHC12LotQn75HLLj7JXzzAGqjwrfO_DnX3gOyVu2e3EQvkMiPuvAKuAwXcMvwKq3dD_Oq8_xzIWeW; qid_uid=92095ee1-5b27-46be-8b6a-1bc810458c13; qid_fs=1686190520449; qid_ls=1686190520450; qid_ts=1699607456636; qid_vis=2; mba_muid=1668069089029464342293; joyya=1699610422.1699610422.72.0gi2j80i6; visitkey=737803510179678; TrackerID=c9-FFuYaVRkgDliG8zgV4dFq7plaedViMFU8NL1KNYgIwCW2tcOgTyFD9Na-j5wcGOY8WAEVRXjEnG6ypT6ZApEyltwAni-g1Gm7w-ANJ6Qs0uzicdRBd2rt34Kb0dkOErtzr3IdH4UTP5pZSDpq-A; cid=9; retina=1; webp=1; __wga=1701829849046.1701828996065.1701067667008.1690941155328.4.18; __jdv=122270672|www.linkstars.com|t_1000089893_156_0_184__a166ebfa78acde91|tuiguang|f49a446e9aff4729aec6f650d457d63d|1701680526613; ipLoc-djd=12-904-907-50559; pin=15951003078_p; unick=%E5%86%A5%E7%8E%8B%E4%B9%8B%E6%AD%8C; _tp=ak3bQDgGku8%2BskP5GCRaiw%3D%3D; _pst=15951003078_p; warehistory="10091517815466,100068431529,100058134266,100035340746,"; equipmentId=7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4; fingerprint=fa88edb26806f6bacfa75d54b30b53f8; deviceVersion=120.0; deviceOS=; deviceOSVersion=; deviceName=Firefox; sc_width=1920; areaId=12; 3AB9D23F7A4B3C9B=7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4; thor=BF80140138890A11F2001240DE13FB3F3C61C0880504BFA8A1E9BDE57F39C6545B0BF4C6C21D32156BC98C736F4464D10776E3795FBB91D349D4ACFE0711B5C6DAE2FF594B86E1166072FC25012ECF15459145CE6D5D66BAA8A5D22DA31A07D8B3C8B4A673A3E7233FA11CF90F01F647C6A7D80CF3BDA2960FD141BB435664F3759D36BA7992D641C944D48FFA05E0FE; flash=2_OWTzgfZjyYwLuvimc-Iw6rIgZe4EB-b2nqZHyMkY0Pa56coRy4alnA08lSl-hnHNltVzekspyioCb72B5cboQGWmtlhkPnGNnPK31c6gE6s*; TARGET_UNIT=bjcenter; cn=5; ceshi3.com=201; wlfstk_smdl=nrmxjlejnqd9ou6q2y4ubb7nbpvyutzh; p-request-id=15951003078_p2023111016bfdq5Tez4v; share_cpin=; share_open_id=; share_gpin=; shareChannel=; source_module=; erp=; appCode=ms0ca95114; plusCustomBuryPointToken=1698131788185_4020; __jdc=122270672; __jdb=122270672.8.1668069089029464342293|187.1701828983; mba_sid=17018289839268268800914776656.8; wxa_level=1; wqmnx1=MDEyNjM3NHNwZG9zdHlkNDgxcjE1LiYzNTF1MDJtODE3MW81YzsgIDUyZTFGLzRZZi00WUQjKEg%3D; jxsid=17018289959745092554; PPRD_P=UUID.1668069089029464342293; jxsid_s_t=1701829849061; jxsid_s_u=https%3A//coupon.m.jd.com/coupons/show.action; _gia_d=1; pt_key=AAJlb9zXADA9AbRpjfqBvdqwt8D8xljlEfaEjmdDETiec3NsBU6EOJf4V3w8_BQjVg0kq_R4y1I; pt_pin=15951003078_p; pt_token=7xmyw9hl; pwdt_id=15951003078_p; sfstoken=tk01maa671c2da8sMngyKzErM09kaCKF+FQGpKu9JFn+bjD5lqTcXxXpMhmEd9s8Wa3Bz2/R5rQBv2OjGoiOJvRDevcT; __jd_ref_cls=MProductCoupon_WaitGetCoupon',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}


params = {
    'appid': 'h5_awake_wxapp',
    'functionId': 'mfreecoupon_tws_getcoupon',
    'client': 'wh5',
    't': '1701829855817',
    'body': '{"key":"c0m5c1s2o1a046ada0c9ec77a9e23506","roleId":"131923362","to":"m.jd.com"}',
    '_stk': 'appid,body,client,functionId,t',
    '_ste': '1',
    '_': '1701829855837',
    'sceneval': '2',
    'g_login_type': '1',
    'appCode': 'ms0ca95114',
    'g_ty': 'ajax',
}

def send_request():
    res = requests.post('https://api.m.jd.com/client.action', params=params, headers=headers, cookies=cookies)
    print(res.text)
    return res


target_time = datetime.datetime(2023, 11, 10, 8, 59, 59, 299999)
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
    if response.text.find('本时段优惠券已抢完'):
        print("本场已抢光，下场再来吧")
        exit()
    else:
        print('领取失败, 重新领取')
        time.sleep(0.3)
