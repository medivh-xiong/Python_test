import requests
import time
import datetime

cookies = {
    '__jda': '122270672.1668069089029464342293.1668069089.1699588680.1699594969.167',
    'b_dw': '1905',
    'b_dh': '927',
    'b_dpr': '2',
    'b_webp': '1',
    'b_avif': '1',
    'shshshfpb': 'AAug1YbeLEg7yo5wUWyRlNuVrILDzmCIKtzs4_wAAAAA',
    'shshshfp': 'b6ec8c37a67e0e37fd7f25ffacb1dc2b',
    'shshshfpa': '3910eb4c-77a3-c4d8-4a59-99a21ffd1286-1668069091',
    'jcap_dvzw_fp': 'MStjxvc74o8PNBQNWwvkqMy4UUC2oFU3mziJBO7xwNEc-qWJfCkVnJtoSp00zaKo8Gu2BA==',
    '__jdu': '1668069089029464342293',
    'shshshfpx': '3910eb4c-77a3-c4d8-4a59-99a21ffd1286-1668069091',
    '3AB9D23F7A4B3CSS': 'jdd037XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4AAAAMLW7ASE3QAAAAAD46WMYSI2ESBNQX',
    'unpl': 'JF8EAKZnNSttWkgHUEhVHxsRS1QEW10ATkQKbW4BXQoNSl0HGlAdEBB7XlVdXxRLFx9vZhRUXVNPXQ4aAysSEHteVV1ZDUsQAWhiNWRdWUpUBBwLGBsSe15Ublw4SxAEZmYCXFxRQ1UGEwccFxJOXldWXzhKJwNnYDVkbVl7VTUbAhgSFEpdVV9eCk4nSAFmSFRaX0JVAhMDEhoRSFVRWVgKThQAZ2U1VW1b',
    'pinId': '9zvM1MUZPR30TcKyARJfCQ',
    'whwswswws': '',
    'TrackID': '1tBSM6p1R1xOtdo8Uk3GX-Y8nVFQt40bIz_g8DZSq2jTZWhWtugQk-RUP2iijSjmE2xqKwyUs0mcput0vfGAXp0Ea_oKSCbqlcLGorYI9MnvCC1vs8qc5DwZen9N5YLra',
    'qid_uid': '92095ee1-5b27-46be-8b6a-1bc810458c13',
    'qid_fs': '1686190520449',
    'qid_ls': '1686190520449',
    'qid_ts': '1686190520450',
    'qid_vis': '1',
    'mba_muid': '1668069089029464342293',
    'joyya': '1699588683.1699588686.60.1cfuc41i6',
    'visitkey': '737803510179678',
    'TrackerID': '0cg5NqeVDJnY-hI4zwRvGGjRM03e6KG-Z99E9VlA79jCbqTT0JLoyducSj8Rp6C9q-1Dp8PjOLP1yJi_cyie6w5LViY5ZMfo0sJs-4_Ghd8L2Ms4SvO7IAJ36pAGctANIlerdPu9Fi9oZlxhrRS3yg',
    'cid': '9',
    'retina': '1',
    'webp': '1',
    '__wga': '1699437683562.1699437683562.1699404283878.1690941155328.1.12',
    '__jdv': '122270672%7Ckong%7Ct_2025416364_%7Cjingfen%7C32bdbf58018a4194b83858fd0830c731%7C1699588682794',
    'pt_key': 'AAJlNyU4ADDddlzBn2367E81jOV5T9oCvnu9i9wpVn_sMGDkkIffDxxVB9o0YiuTFYufpsuxFdE',
    'pt_pin': '15951003078_p',
    'pt_token': 'gff3s2oq',
    'pwdt_id': '15951003078_p',
    'ipLoc-djd': '12-904-907-50559',
    'pin': '15951003078_p',
    'unick': '%E5%86%A5%E7%8E%8B%E4%B9%8B%E6%AD%8C',
    '_tp': 'ak3bQDgGku8%2BskP5GCRaiw%3D%3D',
    '_pst': '15951003078_p',
    'PPRD_P': 'UUID.1668069089029464342293',
    'areaId': '12',
    'thor': 'BF80140138890A11F2001240DE13FB3F3C61C0880504BFA8A1E9BDE57F39C654C714A1860119787ACEF4F08031825962BD7945907A3EC992BA451EBBE2F664F61EB1AD88765C6EBC5F65B3A1DC4051B057862E6126E0BA088028F91AD9DB2394C37DCB8F4A497A43EA43FEC38B3903F69A9C67E73B817B7EEE16E24C9F6A623F102BD8E2DB796834FAA910C4F31B5B0C',
    'flash': '2_eNDTpeyjxY4oYUgwJ8A1syjFQD1NtrlyehTmAowLCyXTwHSIv5MafKJmRdTIW7VMB4ap1DmLw-b4chDWOEUYPqrvVXvIDJGSukSwQ7hG8JM*',
    '3AB9D23F7A4B3C9B': '7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4',
    'cn': '5',
    'ceshi3.com': '201',
    'wlfstk_smdl': 'x3g7lj35l3hytqm7kg9xcvf4ffh84b12',
    'p-request-id': '15951003078_p2023111013Kmi2b3TfKI',
    'share_cpin': '',
    'share_open_id': '',
    'share_gpin': '',
    'shareChannel': '',
    'source_module': '',
    'erp': '',
    'appCode': 'ms0ca95114',
    'plusCustomBuryPointToken': '1698131788185_4020',
    '__jdc': '122270672',
    'joyytokem': 'babel_3jMb3me56Zfmwm1Bep5X4U9L2oJrMDF6SWNLVjk5MQ==.S39acmNCcVVzZkJxUDUTDz9aID4MeDUFKEtlVWdnVngdeShLNyIKOTMhFXwRNgwLDyQuAQYhLjQhKBwMFyArFGYpIQsROTg5IBkwDQgiChdKMS0fPUsENwohNzMieBk8cBQ1KA==.30d530bf',
    'wxa_level': '1',
    '__jdb': '122270672.2.1668069089029464342293|167.1699594969',
    '_gia_d': '1',
    'mba_sid': '1699594969739300327341188256.2',
    '__jd_ref_cls': 'MPlusCoupon_Get_noticexpo',
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
    'body': '{"batchId":1064567537,"platform":3,"eventId":"MPlusCoupon_Get","eid":"7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4","fp":"a17b431a375db42b8014889d5d64a9dd","activityId":"qyb_1038"}',
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
