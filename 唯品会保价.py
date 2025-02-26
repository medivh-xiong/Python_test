import requests
import time

cookies = {
    'mars_cid': '1599307241540_2cf21867f93b286396e6bdc67a4f48d2',
    'userId': '407664155',
    'warehouse': 'VIP_SH',
    'VIP_TANK': '59F9046D57BD74C45BF5C571B73A1872F05CF180',
    'wap_consumer': 'C2-1',
    'fdc_area_id': '932101109107',
}

headers = {
    'Host': 'wxapi.appvipshop.com',
    # 'Cookie': 'mars_cid=1599307241540_2cf21867f93b286396e6bdc67a4f48d2;userId=407664155;warehouse=VIP_SH;VIP_TANK=59F9046D57BD74C45BF5C571B73A1872F05CF180;wap_consumer=C2-1;fdc_area_id=932101109107',
    'accept': '*/*',
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E217 MicroMessenger/6.8.0(0x16080000) NetType/WIFI Language/en Branch/Br_trunk MiniProgramEnv/Mac',
    'referer': 'https://servicewechat.com/wxe9714e742209d35f/1169/page-frame.html',
    'accept-language': 'zh-CN,zh-Hans;q=0.9',
}

params = {
    'api_key': 'ce29a51aa5c94a318755b2529dcb8e0b',
    '_xcxid': '1711597304559',
    'app_name': 'shop_weixin_mina',
    'client': 'wechat_mini_program',
    'source_app': 'shop_weixin_mina',
    'app_version': '4.0',
    'client_type': 'wap',
    'format': 'json',
    'mobile_platform': '2',
    'ver': '2.0',
    'standby_id': 'native',
    'union_mark': 'nature',
    'sd_tuijian': '0',
    'mobile_channel': 'nature',
    'mars_cid': '1599307241540_2cf21867f93b286396e6bdc67a4f48d2',
    'warehouse': 'VIP_SH',
    'fdc_area_id': '932101109107',
    'province_id': '103102',
    'wap_consumer': 'C2-1',
    't': '1711597303',
    'net': 'wifi',
    'width': '414',
    'height': '852',
    'order_sn': '24032648060735',
    'size_id': '6920549355391983640',
    'check_coupon': '0',
    'coupon_sn': '',
}

def bj():
    response = requests.get(
        'https://wxapi.appvipshop.com/vips-mobile/rest/order/after_sale/insure_price_apply',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    print(response.text)

while True:
    bj()
    time.sleep(65)
