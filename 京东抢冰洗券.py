import requests
import time
import datetime


# cookies = {
#     '__jda': '122270672.1668069089029464342293.1668069089.1698802313.1699404179.160',
#     'b_dw': '1905',
#     'b_dh': '942',
#     'b_dpr': '2',
#     'b_webp': '1',
#     'b_avif': '1',
#     'shshshfpb': 'AAurqYayLEhDrTHejxNhKWZmiH_0ShhZoBpCRewAAAA0xNTk1MTAwMzA3OF9w',
#     'shshshfp': 'b6ec8c37a67e0e37fd7f25ffacb1dc2b',
#     'shshshfpa': '3910eb4c-77a3-c4d8-4a59-99a21ffd1286-1668069091',
#     'jcap_dvzw_fp': 'MStjxvc74o8PNBQNWwvkqMy4UUC2oFU3mziJBO7xwNEc-qWJfCkVnJtoSp00zaKo8Gu2BA==',
#     '__jdu': '1668069089029464342293',
#     'shshshfpx': '3910eb4c-77a3-c4d8-4a59-99a21ffd1286-1668069091',
#     '3AB9D23F7A4B3CSS': 'jdd037XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4AAAAMLVRQ6V4AAAAAACH7ZWGOXOXJXSUX',
#     'unpl': 'JF8EAL1nNSttX0pXVhMDS0VCHFwHWw9aGx8LPzQCAF1dHlJWE1VJQhR7XlVdXxRLFh9tZxRUVVNJVQ4bCysSEHtdVV9dD0MTA2hkNWRdWUpUBBwLGBsSe15Ublw4SxAEZmYCXFxRQ1UGEwccFxJOXldWXzhKJwNnYDVUXFlKUgAaChgQFkJtZF9tCEoXAmdXB1RcWUpRAx8GHyJGJV1VX1wIShMLZm5IVFpfQlUCEwMSGhFIVVFZWApOFABnZTVVbVs',
#     'pinId': '9zvM1MUZPR30TcKyARJfCQ',
#     'whwswswws': '',
#     'TrackID': '1Y6lJgvDKu9fQQiCBZ2gKWHDGjD02z9dRmGJLU3bRJMxphFAtxhLqW7i1mhW4X6KNCO3r5BcOwk9Pxp-6_PFhc071YdoodWpnA4XXq5KAxqLpSYEHb6QfF5bNGWl_tWFc',
#     'qid_uid': '92095ee1-5b27-46be-8b6a-1bc810458c13',
#     'qid_fs': '1686190520449',
#     'qid_ls': '1686190520449',
#     'qid_ts': '1686190520450',
#     'qid_vis': '1',
#     'mba_muid': '1668069089029464342293',
#     'joyya': '1699404179.1699404241.64.1lrwpje',
#     'visitkey': '737803510179678',
#     'TrackerID': '0cg5NqeVDJnY-hI4zwRvGGjRM03e6KG-Z99E9VlA79jCbqTT0JLoyducSj8Rp6C9q-1Dp8PjOLP1yJi_cyie6w5LViY5ZMfo0sJs-4_Ghd8L2Ms4SvO7IAJ36pAGctANIlerdPu9Fi9oZlxhrRS3yg',
#     'cid': '9',
#     'warehistory': '"100069093655,100067571661,100060368518,100060368518,100064695864,10081455960159,10076966961724,"',
#     'retina': '1',
#     'webp': '1',
#     'equipmentId': '7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4',
#     'fingerprint': 'a6bb8db393d09f2b1c7b87c0eabd54a6',
#     'deviceVersion': '118.0',
#     'deviceOS': '',
#     'deviceOSVersion': '',
#     'deviceName': 'Firefox',
#     '__wga': '1698199206987.1698199183696.1698135769994.1690941155328.2.10',
#     '__jdv': '122270672%7Cweixin%7Ct_1000072672_17053_001%7Cweixin%7C619e6946110444418cddb9717ec73b47%7C1699404179622',
#     'sc_width': '1920',
#     'pt_key': 'AAJlNyU4ADDddlzBn2367E81jOV5T9oCvnu9i9wpVn_sMGDkkIffDxxVB9o0YiuTFYufpsuxFdE',
#     'pt_pin': '15951003078_p',
#     'pt_token': 'gff3s2oq',
#     'pwdt_id': '15951003078_p',
#     'ipLoc-djd': '12_904_3379_0',
#     'pin': '15951003078_p',
#     'unick': '%E5%86%A5%E7%8E%8B%E4%B9%8B%E6%AD%8C',
#     '_tp': 'ak3bQDgGku8%2BskP5GCRaiw%3D%3D',
#     '_pst': '15951003078_p',
#     '3AB9D23F7A4B3C9B': '7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4',
#     'TARGET_UNIT': 'bjcenter',
#     'cn': '5',
#     'ceshi3.com': '201',
#     'wlfstk_smdl': '1iw9vghnbdkpu174ax3ijmndtq9neqmf',
#     'p-request-id': '15951003078_p2023102415cHyNZQ0NDa',
#     'share_cpin': '',
#     'share_open_id': '',
#     'share_gpin': '',
#     'shareChannel': '',
#     'source_module': '',
#     'erp': '',
#     'appCode': 'ms0ca95114',
#     'plusCustomBuryPointToken': '1698131788185_4020',
#     '__jdc': '122270672',
#     'joyytokem': 'babel_3ZCXjnEc7H3LTYRMXHr34tVBtayZMDFFa0F6TDk5MQ==.dF14Q3h1X3BNdX1TeAQJIiUwQnV8WgBMMnRHd1Z9aVo/SDJ0FQA7ImhbJ04bCS4pPj4RIyQQNAsDCi0WKAIJJXwWAykgIwcbAigpMioAOw11Ew8uJ3QmFTs7CBEASQMDUjYEMg==.e811faf0',
#     '__jdb': '122270672.1.1668069089029464342293|160.1699404179',
#     'mba_sid': '16994041796235438569331905415.1',
#     '__jd_ref_cls': 'Babel_FinanceCoupon',
#     '_gia_d': '1',
# }
#
headers = {
    'Cookie': 'wskey=AAJkp68BAEAAT__RR1J5cCnXS7BITtynCCpRe38Y4zBCfpNjg1QAgOmFftcZFeqtmuYiD-8-Mg75LRip3R_icByDYayKJi2b;whwswswws=JD012145b99Ow2wqj6M4169948740672203OcFkA6ylwCB66ITeigM1mQbi6kYWLWz9CRaLkAsYrbl0L2obuh8_rJwGc5zEqb2hCMihmzAq-7wmBzWWwoQAgw1pk7k4e~AAhlFWbGLEAAAAAAAAAAAAAAAAP7AwFLqt7uNfwAAAA0xNTk1MTAwMzA3OF9w;unionwsws={devicefinger:eidAeceb812290s4AEzAUMQFTlOcsJBUQlcC5gBMwdUUmwi+3LXgoOmzWMLEKjdE3ANJpm1kQuOWo4OZ3IsrFpemmviPKAWONxrMIQYgjX+/rGcbE9Nn,jmafinger:JD012145b99Ow2wqj6M4169948740672203OcFkA6ylwCB66ITeigM1mQbi6kYWLWz9CRaLkAsYrbl0L2obuh8_rJwGc5zEqb2hCMihmzAq-7wmBzWWwoQAgw1pk7k4e~AAhlFWbGLEAAAAAAAAAAAAAAAAP7AwFLqt7uNfwAAAA0xNTk1MTAwMzA3OF9w};pin_hash=423487328;',
    'J-E-C': '%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1699487396380%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22pin%22%3A%22CJU5DJOmCNCmDzrpcK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D',
    'X-Rp-Client': 'android_3.0.0',
    'jdgs': '{b1:9af5485e-0cb5-4f3a-a8f7-e8dc2026a8d8,b2:3.2.4_0,b3:2.1,b4:DqKeVZcFuvQCVSnny02m/tpurvRU5hj3t3+Q0hpCaE3EC6UEMBp1tsHx5ZV/7moQdtgUkiZ91y3CZE2MDv07Zct+AMO5E8BH9R07nKsR3UhF8dAY43ihhZuA5g1f5OQ7qimQQC743yhzW5QOAUAN6GzD4A5n6ZNmr0k3gXF0f6LJUM4gei1OjEkvkJsCZPMfT2ZxmZILnaIAXkkGD2p2bKfdZ93xfgk+mXp2SpI4zCFyNfbGVPT2vJOjNPoTKHMGXDu9h0bKqNSTEbB9mV/xTGDvTnCDxh3yjjbegmRCwwgxvQ5fjQtVI54/fpxogcs33gzo29OQTfWZwcr4f0aprEZNgdZQxWMHvoBeww9039Cfyi5BMRlo3XBRFKSMKWZbEw==,b5:369bc19c7ab32eb18ec2e7024d9c6e54cca05a06,b7:1699487520151,b6:d6733ba6fac35d8f893f029052dee36acdfb6863}',
    'Connection': 'keep-alive',
    'User-Agent': 'okhttp/3.12.16;jdmall;android;version/12.2.2;build/98996;',
    'X-Referer-Package': 'com.jingdong.app.mall',
    'Charset': 'UTF-8',
    'X-Referer-Page': 'com.jd.lib.babel.view.activity.BabelActivity',
    # 'Accept-Encoding': 'br,gzip,deflate',
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Content-Length': '875',
    'Host': 'api.m.jd.com',
}


params = {
    'functionId': 'newBabelAwardCollection',
    'clientVersion': '12.2.2',
    'build': '98996',
    'client': 'android',
    'partner': 'xiaomi001',
    'oaid': '1782da4474c95477',
    'sdkVersion': '33',
    'lang': 'zh_CN',
    'harmonyOs': '0',
    'networkType': 'wifi',
    'uts': '0f31TVRjBSss9v6Wmp+A5RH6/jXkbRHVN2k9yjJ/AITfJB3G8rkNu3gBpYMiyOsz+w6UWLOWllnSCBOeK1M0+TBOb9nFAkX0rtuhgC3D/LGxC1P4AfgknhNcKX5zCfwolS+QpKVwnHEv9fY0MXXjwxnXqAPqe+WyLNZpFVjwP0R/Ixq5PKxbvhFJK/bj88c0zHfvSB9q7NS1ddhSV5jJYg==',
    'uemps': '0-2-2',
    'ext': '{"prstate":"0","pvcStu":"1","cfgExt":"{\\"privacyOffline\\":\\"0\\"}"}',
    'avifSupport': '1',
    'eid': 'eidAeceb812290s4AEzAUMQFTlOcsJBUQlcC5gBMwdUUmwi+3LXgoOmzWMLEKjdE3ANJpm1kQuOWo4OZ3IsrFpemmviPKAWONxrMIQYgjX+/rGcbE9Nn',
    'x-api-eid-token': 'jdd01SQJTXMLZI3I6ON4GPM3ILZN3FZYKZTWHATLKQ45K4GKKTN7KNWTSQ4IKLVOVNXMD3XQCRKTZSQIPTD7REGOYOT25UVDROAU3HJ376MA01234567',
    'ef': '1',
    'ep': '{"hdid":"JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw=","ts":1699487396352,"ridx":-1,"cipher":{"area":"CJTpEJK0XzCzDzZpDJc4Dzu=","d_model":"UwVubWvBDJLVbRHyYG==","wifiBssid":"dW5hbw93bq==","osVersion":"CJC=","d_brand":"WQvrb21f","screen":"CtU3DsenCtSm","uuid":"ZwVtCQCmDJTvYWS3YwS4ZK==","aid":"ZwVtCQCmDJTvYWS3YwS4ZK==","openudid":"ZwVtCQCmDJTvYWS3YwS4ZK=="},"ciphertype":5,"version":"1.2.0","appname":"com.jingdong.app.mall"}',
    'st': '1699487520150',
    'sign': 'f08f16a7ccfec7c0ca6d86f591a3656e',
    'sv': '101',
}

data = 'body=%7B%22actKey%22%3A%224A932D24ED5519BFE4D4F23DDB74AF0FEE84810904079DA75487A306EFFC5C640CB520B6BDF43FE2C467304E70A5F8536EA554E56EFAB9770C9330327C7DF4D7A3E0A953B6BAF4CA2777826712334C7B32DB670D47F267B336901493038AF50F37E6374A38016AE243BE6409591EC7148254C758043D570738FC7279A60496499B924FA69C45F0815C1AFC7985FCF686C6D94F628BFD29E94712FD55CD716D11FCF596DDDC0921EC7137F1007645C8B7AA91CBF0309F7C0A54AD1EB34E7512E7_bingo%22%2C%22activityId%22%3A%223ZCXjnEc7H3LTYRMXHr34tVBtayZ%22%2C%22args%22%3Anull%2C%22eid%22%3A%22eidAeceb812290s4AEzAUMQFTlOcsJBUQlcC5gBMwdUUmwi%2B3LXgoOmzWMLEKjdE3ANJpm1kQuOWo4OZ3IsrFpemmviPKAWONxrMIQYgjX%2B%2FrGcbE9Nn%22%2C%22moduleId%22%3Anull%2C%22pageClick%22%3A%22Babel_FinanceCoupon%22%2C%22scene%22%3A%223%22%2C%22token%22%3A%22jdd01SQJTXMLZI3I6ON4GPM3ILZN3FZYKZTWHATLKQ45K4GKKTN7KNWTSQ4IKLVOVNXMD3XQCRKTZSQIPTD7REGOYOT25UVDROAU3HJ376MA01234567%22%7D&'

def send_request():
    res = requests.post('https://api.m.jd.com/client.action', params=params, headers=headers, data=data)
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
