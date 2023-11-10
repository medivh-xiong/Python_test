import requests
import time
import datetime

# 王林波ck
cookies = {
    'shshshfpa': 'a1ac875a-97fd-0360-ddca-7be66f4ea17b-1685522928',
    'shshshfpx': 'a1ac875a-97fd-0360-ddca-7be66f4ea17b-1685522928',
    'jcap_dvzw_fp': 'VQhYkc1IGWetfZywc7VjWr0vrpf3R0DVJXwzlkNqc6EWI9277XCKyqDTY37MvTS8XGE7W4-C9X5d8v9iHF4H4g==',
    'whwswswws': '',
    '__jdv': '122270672%7Cdirect%7C-%7Cnone%7C-%7C1698135013161',
    '__jdu': '16855229286681104609334',
    'areaId': '12',
    'ipLoc-djd': '12-904-0-0',
    '3AB9D23F7A4B3C9B': 'K5GGTC5YGI4BRKEKTFU3GZTJFQWMYXU4LNIB2IV2KGZ6J5XS2TMOYGBJ5ENB7LNQVGHOXRRBXTWEPEMTT5NCTBOWKI',
    'TrackID': '1TEpqW3lGT8NJ-EehaeM0ymQokMl_vFdVdStVDJNCWKw9aZyMQkzteVV3IoL72JLkmGC81UNxNgLOdbMtIsJzQaaOWsJfSNpXYV_rYUJ8__9rk0LLahRjzUHjZ8-bEwiO',
    'thor': 'BA62CD15BC9AECD4D884F8D4EFCA1A91545C015D778987A001AE3618D49406D0E9DF82474BC0D41B170D4A9FAF83B19B7E21127252655821DBB0D8D47E4632EFCC7AAA10944C1A7196ABF06E16CCFBEF355B0FE22EDD345ABB5F884A70CA0D04A5139B8C83C7D6ACEACB24E7A48679F3BA93FB0B4F32EE5130DDD24CF8F7DC4EDCC5146F9AB4D5C0398FBF9FD81AB855',
    'flash': '2_m-E_o61pYD-674wVBHLcPDO2pAQ-mwad50f95bdkXAFNBqshcDKmekKrKdu74A39zKHjaVn44A6nTLk1g9IlSKMCe5PRN9TzVVDHO6BKhIk*',
    'pinId': 'aGUM9nYLIXQ',
    'pin': 'KMasker',
    'unick': '%E7%9A%AE%E4%BA%86%E5%8F%88%E4%BA%86%E7%9A%AE',
    'ceshi3.com': '201',
    '_tp': '3ou1MpvsFYS%2F2b8QTF90Fw%3D%3D',
    '_pst': 'KMasker',
    '__jda': '76161171.16855229286681104609334.1685522928.1686620905.1698135013.4',
    '__jdc': '76161171',
    'wxa_level': '1',
    'retina': '1',
    'cid': '9',
    'jxsid': '16981350735591310924',
    'appCode': 'ms0ca95114',
    'webp': '1',
    'mba_muid': '16855229286681104609334',
    'visitkey': '6975564413381910996',
    'PPRD_P': 'UUID.16855229286681104609334',
    'share_cpin': '',
    'share_open_id': '',
    'share_gpin': '',
    'shareChannel': '',
    'source_module': '',
    'erp': '',
    'jxsid_s_u': 'https%3A//coupon.m.jd.com/coupons/show.action',
    'sc_width': '1920',
    'shshshsID': 'e422eceadafe0b33ea3a40a4a7f9dcd8_8_1698135077907',
    'TrackerID': 'BLZ3FZnC2eaZDFN02lU2PcphVNRvpu0GxuT0yNv91aI1KaBJphWc7y3qHQxcl_h-8iXPYZiqgbIVRd1SwHsQ6RA2VSnovpywQXOAqimH4D6AJZiDYA3EdqWnRcK3ViYE',
    'pt_key': 'AAJlN3yHADBPJ4dGcxI5XskI_nPxeExjdyZyNcj90jt8Y3dwRYeTAwpmuQlOY6d1UhaDH5kIhWI',
    'pt_pin': 'KMasker',
    'pt_token': 'uraadr04',
    'pwdt_id': 'KMasker',
    'sfstoken': 'tk01ma2351b65a8sM3gzKzN4MmZH7VnVeCrG5CamV7WixEyE59eieLWoU/iO13PFWoQmoRaA/cB3AvLSZuOMXQjDY834',
    'wqmnx1': 'MDEyNjM1M3BjbmQvb2hjP2M0YTRjZGFsMTZ0MTM4NjUzMU1sMGNzbk1TMDdwYjU2VGxHKW8xMGEvM2cuNzFGZmFhQjRRRVMpRilI',
    '__jdb': '76161171.12.16855229286681104609334|4.1698135013',
    'mba_sid': '1698135073616221496344886196.4',
    '3AB9D23F7A4B3CSS': 'jdd03K5GGTC5YGI4BRKEKTFU3GZTJFQWMYXU4LNIB2IV2KGZ6J5XS2TMOYGBJ5ENB7LNQVGHOXRRBXTWEPEMTT5NCTBOWKIAAAAMLMC7HH3YAAAAACFDHG4JNVMHDNAX',
    '_gia_d': '1',
    '__wga': '1698135176154.1698135073845.1698135073845.1698135073845.2.1',
    'jxsid_s_t': '1698135176189',
    'shshshfpb': 'AAj11vmCLEqyHWpf9A2Ddynvmb06hexaFUikoSQAAAAdLTWFza2Vy',
    '__jd_ref_cls': 'MProductCoupon_WaitGetCoupon',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://plus.m.jd.com/coupon/index',
    'Origin': 'https://plus.m.jd.com',
    'Connection': 'keep-alive',
    # 'Cookie': '__jda=122270672.1668069089029464342293.1668069089.1685516131.1685521770.88; b_dw=1905; b_dh=942; b_dpr=2; b_webp=1; b_avif=1; shshshfpb=uq9DkkDZijmtaRHkXrJ2GuA; shshshfp=b6ec8c37a67e0e37fd7f25ffacb1dc2b; shshshfpa=3910eb4c-77a3-c4d8-4a59-99a21ffd1286-1668069091; jcap_dvzw_fp=MStjxvc74o8PNBQNWwvkqMy4UUC2oFU3mziJBO7xwNEc-qWJfCkVnJtoSp00zaKo8Gu2BA==; __jdu=1668069089029464342293; mba_muid=1668069089029464342293; _gia_s_local_fingerprint=903a4f9a272101b0156a051b19da035a; joyya=1682043141.1682043142.58.1bdnrki; _gia_s_e_joint={"eid":"7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4","ma":"","im":"","os":"Mac OS X","ip":"49.65.245.187","ia":"","uu":"","at":"5"}; qid_uid=b9e84b09-0bb7-4b06-8826-374607fedc9a; qid_fs=1673511964676; qid_ls=1673511964676; qid_ts=1673511964681; qid_vis=1; visitkey=20610317072847411; webp=1; __wga=1685522252447.1685522139459.1685516131591.1674957363394.5.11; shshshfpx=3910eb4c-77a3-c4d8-4a59-99a21ffd1286-1668069091; 3AB9D23F7A4B3CSS=jdd037XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4AAAAMIOD7R3OAAAAAADKOWAXCCOYPAKMX; warehistory="100038101729,100038101729,100049357944,"; retina=1; cid=9; equipmentId=7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4; fingerprint=XKpjcGuNl2ApcqGqPynePIMtil8ks9MZ; deviceVersion=113.0; deviceOS=; deviceOSVersion=; deviceName=Firefox; _ga_3QZBFRN5GM=GS1.1.1681967732.2.1.1681969079.0.0.0; _ga=GA1.1.1463980621.1681806862; __jdv=122270672%7Ckong%7Ct_2011526755_%7Cjingfen%7C1ee21461213d433bac0822bb602be5f6%7C1685325557161; cartNum=1; ipLoc-djd=12_904_3379_0; sc_width=1920; unpl=JF8EALJnNSttWB8ABhsHHBITS18BW18KGEdRbm4GVw4LTFUGSFYfRRd7XlVdXxRKEx9sbxRVVVNPXA4bBSsSEHteVV5dDEgQBWtjNWRVUCVXSBtsGHwTBhAZbl4IexYzb2ACXVxfQ1UMEwMYGhVMWFZbXgtDFTNuVwVSbVhKVQQZCxoTFUlVVG5tCXsWM25XUzpdWUpVBBoDGxEWBl1TWVQJTB8CZm8EV1VdTFEHHgEYGhJ7XGRd; RT="z=1&dm=jd.com&si=5moaoykxcx7&ss=li87bm91&sl=2&tt=1bn&ld=1m6&ul=2hc&hd=2m4"; areaId=12; wxa_level=1; jxsid=16855161313159276793; PPRD_P=UUID.1668069089029464342293; jxsid_s_t=1685522252460; jxsid_s_u=https%3A//home.m.jd.com/myJd/newhome.action; jsavif=1; shshshsID=f8b66822db105b9006b3707016e81acd_5_1685522145656; __jdb=122270672.32.1668069089029464342293|88.1685521770; pinId=9zvM1MUZPR30TcKyARJfCQ; pin=15951003078_p; unick=%E5%86%A5%E7%8E%8B%E4%B9%8B%E6%AD%8C; _tp=ak3bQDgGku8%2BskP5GCRaiw%3D%3D; _pst=15951003078_p; 3AB9D23F7A4B3C9B=7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4; wqmnx1=MDEyNjM5NHNtbW9uMTEvaW5PNS4vIDFGZC0yVSkm; mba_sid=16855221393781947470304517464.23; cd_eid=jdd037XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4AAAAMIODY2DMIAAAAADSCF5OFMYWT6TQX; whwswswws=; TrackerID=PoyK8Low36mKIyi0bymw5mkU7w2qewScoTtGeUdcoU7JFoxzXz2mXDNHkIBj4mJgP89f3lyob8-S_dC_XzLWYoOvCml6zZynxxKdOTvhQuYUJUHjAm_ZpY-UkdclXo1uQUd8armI3Govt1B7lUvUSg; pt_key=AAJkdwdDADB0oKEc-rrx-9vAIH57jUDSVR2QOeE7pSHn5A8p4alvv8kscTa0G9iWTCpiREQDvr8; pt_pin=15951003078_p; pt_token=bsov9z9v; pwdt_id=15951003078_p; sfstoken=tk01m98ef1b25a8sMSszeDF4M3gzCTub2rdJcIAbSOr6vVzBy73USGgGFC9HDVwEG15ZmM5w10I3F3TP5ytnWKVh32gv; appCode=ms0ca95114; share_cpin=; share_open_id=; share_gpin=; shareChannel=; source_module=; erp=; wlfstk_smdl=nvwb9rqb4xj9q6115mrllyw11u00849w; thor=BF80140138890A11F2001240DE13FB3F3C61C0880504BFA8A1E9BDE57F39C654B1341A83F89F277EF9C157CAF34D5C39734ADB556CEC07DDBADB3C39A762BC60E393AB16C17C39B4A78AD1D4861D90BC0B8E7727FA616E7A275E4A15F7D3F01B84355AC69E359C0F915DC2BE7D08214BBF8209FB78DF4396E6FB0A29B6387C53F428F81B4B839991015764948ECFB81B; flash=2_djLYmwxvCDTrtd34xGZHUBBFqDAJJVcANqp7FkfPkjDcXudxM5KUukWdvVIRvZNqIcYlWlHpKIm8rTNxNvI5TLjUomVKIvXpuSwm63xiyBs*; ceshi3.com=201; p-request-id=15951003078_p20230531166jaMVMRDs3; plusCustomBuryPointToken=1685522258425_4020; __jdc=122270672; __jd_ref_cls=MPlusCoupon_Confirm; _gia_d=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
    'x-referer-page': 'https://plus.m.jd.com/coupon/index',
    'x-rp-client': 'h5_1.0.0',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

params = {
    'functionId': 'coupon_receiveDayCoupon_v2',
    'loginType': '2',
    'loginWQBiz': '',
    'appid': 'plus_business',
    'body': '{"batchId":1063732465,"platform":3,"eventId":"MPlusCoupon_Get","eid":"7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4","fp":"a17b431a375db42b8014889d5d64a9dd","activityId":"qyb_1037"}',
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
