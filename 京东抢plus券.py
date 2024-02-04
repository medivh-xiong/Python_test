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
    'body': '{"batchId":1063732465,"platform":3,"eventId":"MPlusCoupon_Get","eid":"7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4","fp":"a17b431a375db42b8014889d5d64a9dd","activityId":"qyb_1052"}',
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
