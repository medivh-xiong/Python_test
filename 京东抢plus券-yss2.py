import requests
import time
import datetime

cookies = {
    '__jda': '181111935.1668069089029464342293.1668069089.1706057699.1706061988.217',
    'b_dw': '1905',
    'b_dh': '927',
    'b_dpr': '2',
    'b_webp': '1',
    'b_avif': '1',
    'shshshfpb': 'BApXeox4wOuhA5kVcheQqbPiQ8NWkO6NcBypHl75X9xJ1MuQLHC62',
    'shshshfp': 'b6ec8c37a67e0e37fd7f25ffacb1dc2b',
    'shshshfpa': '3910eb4c-77a3-c4d8-4a59-99a21ffd1286-1668069091',
    'jcap_dvzw_fp': 'MStjxvc74o8PNBQNWwvkqMy4UUC2oFU3mziJBO7xwNEc-qWJfCkVnJtoSp00zaKo8Gu2BA==',
    '__jdu': '1668069089029464342293',
    'shshshfpx': '3910eb4c-77a3-c4d8-4a59-99a21ffd1286-1668069091',
    '3AB9D23F7A4B3CSS': 'jdd037XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4AAAAMNHE6B7EAAAAAACD7X4JXC3GJKJ4X',
    'unpl': 'JF8EALJnNSttXx5QBU9WExAYTwgHW11YTR4BPDJXAA8IS1ENTAYcRxZ7XlVdWBRKFx9sZRRUW1NPUw4YAysSEHteVV5dC0kQB2djNWRVUCVUSBtsGHwQBhAZbl4IexYzb2ACXVxfQ1UMEwMYGhVMWFZbXgtDFTNuVwVSbVhKVQQcBxwaFEJaUW5tCXsWM25XUzpdWUpVBBoHGBYYBl1TWVQJTB8CZm8EV1VdTFEHHgEYGhJ7XGRd',
    'pinId': '9zvM1MUZPR30TcKyARJfCQ',
    'whwswswws': '',
    'TrackID': '1O8-FAi9tckEVkIEmbm2hNtwoPlFXFm2v-KqQyDAQSzeISDztvAVvuADJo7yFdKm9X6cKEle5OE1mP2FTpgdsvSNgv3BOgxFIm8KLBUHhigJo0VvYe2PVG_dzR9IFPMuX',
    '__jdv': '181111935%7Ckong%7Ct_2011236595_%7Cjingfen%7C6d51ee9395db41a783bdceca149f56d7%7C1706057699857',
    'ipLoc-djd': '12-904-907-50559',
    'pin': '15951003078_p',
    'unick': '%E5%86%A5%E7%8E%8B%E4%B9%8B%E6%AD%8C',
    '_tp': 'ak3bQDgGku8%2BskP5GCRaiw%3D%3D',
    '_pst': '15951003078_p',
    'warehistory': '"100064695864,100064695864,10081479480401,10081479480401,100066206148,10086397575079,10091517815466,100068431529,100058134266,100035340746,"',
    'mba_muid': '1668069089029464342293',
    'retina': '1',
    'cid': '9',
    'webp': '1',
    'visitkey': '737803510179678',
    '__wga': '1706057699856.1706057699856.1706003781458.1702965512523.1.6',
    'equipmentId': '7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4',
    'fingerprint': '1dc9dfcf2fec5b8f4a25614cebb99e70',
    'deviceVersion': '121.0',
    'deviceOS': '',
    'deviceOSVersion': '',
    'deviceName': 'Firefox',
    'thor': 'BF80140138890A11F2001240DE13FB3F3C61C0880504BFA8A1E9BDE57F39C654A40D131BE0F1A893847064C9B2D96600BC9D9D8ABFD7BE5B6933BC954C6F872F0F90BC5EF2AFD3EC957E9C56B3259F8E6E6DA325D6C36F7A0A7E4735AACBF72A45D2C1198B09A457066786935549575591F37C4D6AF22561371D24DE14BC73E3BAD69BB77BA4B0B33351A70A1C432CB2',
    'flash': '2_nk78bvAdrY3KhqCK20IX4RfYYXFE8kJBGz77-E9VNO9RqOVmtYhZlN78aqi9t-fF99vDWScSHNyk0JqYR3QaQNbWkcGpd558I2ulKn0K825*',
    '3AB9D23F7A4B3C9B': '7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4',
    'PPRD_P': 'UUID.1668069089029464342293-LOGID.1706057699859.1901683595',
    'sc_width': '1920',
    'wxa_level': '1',
    'jxsid': '17060037809851029159',
    'TARGET_UNIT': 'bjcenter',
    'ceshi3.com': '201',
    'wlfstk_smdl': 'huqcx7eo4acem513okq7arhz85fnhq0y',
    'source': 'PC',
    'platform': 'pc',
    'lpkLoginType': '3',
    'appCode': 'ms0ca95114',
    '__jdc': '181111935',
    'cd_eid': 'jdd037XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4AAAAMNGW75O6IAAAAADRCAK223S43VXUX',
    '__jdb': '181111935.4.1668069089029464342293|217.1706061988',
    'mba_sid': '17060619886606169320731042039.3',
    'token': '752092fdb59ec966187fe3ee262effdc,3,947812',
    '__tk': 'jpqDJUtyJsupJve5JckiJca0kpIwlUA0kDI0lUAzjsG,3,947812',
    'shshshsID': 'f8000d3171e671cdb290adabebd7e40f_1_1706062022466',
    'jsavif': '1',
    'areaId': '12',
    'TrackerID': 'rzxofsK8hC8RfqQcpzEGs3qWcpZoEmaMYlxd46Xna_oEQ-zrkkdpDUhLPTeVy8cFIU9pi2FRjMgHIpEiZ833FTJYErEoeMhp8-FpefcgGwPwuD5Vcz5Wm3Itkj-2Hbp1RiKafpGCYvunX2zTpevkJw',
    'pt_key': 'AAJlsHGxADAb1U70-t6r6lSPC70ieQRFsnm_m02LNkCkYBfv3ydR4QKdFoGoN42ch6VAgIdEN50',
    'pt_pin': '13605176365_p',
    'pt_token': '61avi92z',
    'pwdt_id': '13605176365_p',
    'sfstoken': 'tk01me2981d81a8sMSsyKzErMiszuPCAAY3DSj49mZXKasJhXUuNkomQ8wbHOcJaadYz+MOxvNZmnK/SXGSPxIEnTjml',
    'p-request-id': '13605176365_p2024012410JILPVm6mlL',
    '_gia_d': '1',
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
    'body': '{"batchId":1063732465,"platform":3,"eventId":"MPlusCoupon_Get",'
            '"eid":"7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4",'
            '"fp":"a17b431a375db42b8014889d5d64a9dd","activityId":"qyb_1052"}',
    'scval': '',
    '_': '1685522971069',
}


# 早上10点准点请求
def send_request():
    res = requests.get('https://api.m.jd.com/api', params=params, cookies=cookies, headers=headers)
    print(res.text)
    return res



target_time = datetime.datetime(2023, 5, 31, 22, 0, 0)
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
        result = False
        exit()
    elif rspCode == "1760010":
        print("本场已抢光，下场再来吧")
        exit()
    else:
        print('领取失败, 重新领取')
        time.sleep(0.4)
