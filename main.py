import hashlib
import json
import requests
import time

QYWX_AGENTID = 1000004
QYWX_CORPID = 'ww53c95c6827fc9478'
QYWX_CORPSECRET = 'SfMQubr-Qv5p0FCA5duHjU-2DaMS-n5lmMs6LhZn5y4'
QYWX_TOUSER = 'XiongXin'


def message2qywxapp(qywx_corpid, qywx_agentid, qywx_corpsecret, qywx_touser, content, title):
    print("企业微信应用消息推送开始")
    res = requests.get(
        f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={qywx_corpid}&corpsecret={qywx_corpsecret}"
    )
    token2 = res.json().get("access_token", False)
    data2 = {
        "touser": qywx_touser,
        "agentid": qywx_agentid,
        "msgtype": "textcard",
        "textcard": {
            "title": title,
            "description": content,
            "url": "https://www.smzdm.com/",
            "btntxt": "详情",
        },
    }
    requests.post(url=f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={token2}", data=json.dumps(data2))


# 配置cookie 支持多账号一行一个 放单引号里面 根据实际需求增删
cookie = [
    '__ckguid=jAgL936po9C2T62tWJFVU57; device_id=21307064331672890790738551ba267c42096d5ea85a0b78887bc469ac; '
    'homepage_sug=c; r_sort_type=score; _zdmA.uid=ZDMA.0GekqFQe6.1672892582.2419200; _zdmA.vid=*; '
    'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22185800fb50adf-03c84c98c0ca7c-40262c3c-2073600'
    '-185800fb50b13a1%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B'
    '%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7'
    '%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A'
    '%22185800fb50adf-03c84c98c0ca7c-40262c3c-2073600-185800fb50b13a1%22%7D; sajssdk_2015_cross_new_user=1; '
    'Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1672890791; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1672892582; '
    'footer_floating_layer=0; ad_date=5; bannerCounter=%5B%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number'
    '%22%3A0%2C%22surplus%22%3A7%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus'
    '%22%3A1%7D%2C%7B%22number%22%3A2%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%5D; '
    'ad_json_feed=%7B%7D; amvid=fbcc89e030537a6adaa6171fca22f68c; '
    '_zdmA.time=1672892841042.0.https%3A%2F%2Fwww.smzdm.com%2F; '
    'sess=BA-0vZVXvopIiJCGVEaIT0YxphK0yo9lUD5sSdTbmW5JslaDfIw2QCbYTqSCTA1Yb0mWuK3%2F1q88fYk1y4dVn9Fxq4OSYVsD'
    '%2F0ab3sBj%2BXpjTAA50Ri6HWbRCnR; user=user%3A8215148701%7C8215148701; smzdm_id=8215148701',

    "__ckguid=wha6P93Jsq4UYobVWCVfc32; device_id=2130706433167291064383939400eb75ffcc8592f1f20f584b3fa506c6; "
    "homepage_sug=d; r_sort_type=score; _zdmA.uid=ZDMA._RIxewhko.1672910659.2419200; _zdmA.vid=*; "
    "sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22185813ea460a-06bbb302f1f4588-40262c3c-2073600-185813ea461d08"
    "%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6"
    "%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC"
    "%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2F%22%7D%2C%22%24device_id%22%3A%22185813ea460a"
    "-06bbb302f1f4588-40262c3c-2073600-185813ea461d08%22%7D; sajssdk_2015_cross_new_user=1; footer_floating_layer=0; "
    "ad_date=5; bannerCounter=%5B%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A2"
    "%7D%2C%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22"
    "%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%5D; ad_json_feed=%7B%7D; "
    "Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1672910646; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1672910659; "
    "amvid=2bf171ae56899458ac644c88afe05c2e; _zdmA.time=1672910659449.0.https%3A%2F%2Fwww.smzdm.com%2F; "
    "sess=BA-0L6cJJxvqK5XcSlH7TD2LIeStqCKbnP0yduujmJCNb%2Bu1ylHfF387X%2F3XxWDnZgTgYjVvbMA9WR0sMLhD0f6iC"
    "%2BqGjt87HBZww3r4u3WZbVp2aP08rsYOJI0; user=user%3A5357793255%7C5357793255; smzdm_id=5357793255",

    '__ckguid=NCT6P93nI4FyAs3tusnQxf; device_id=213070643316729117357397462a48a3c4fe7f9edae9d584478219ff9c; '
    'homepage_sug=d; r_sort_type=score; _zdmA.uid=ZDMA.eGQhpe0Qn.1672911753.2419200; _zdmA.vid=*; '
    'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22185814f4d60816-0f955b498de88b-40262c3c-2073600'
    '-185814f4d61fbe%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87'
    '%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5'
    '%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2F%22%7D%2C%22%24device_id%22%3A'
    '%22185814f4d60816-0f955b498de88b-40262c3c-2073600-185814f4d61fbe%22%7D; sajssdk_2015_cross_new_user=1; '
    'Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1672911736; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1672911753; '
    'footer_floating_layer=0; ad_date=5; bannerCounter=%5B%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number'
    '%22%3A0%2C%22surplus%22%3A2%7D%2C%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus'
    '%22%3A1%7D%2C%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%5D; '
    'ad_json_feed=%7B%7D; amvid=a6b47822d17bc2790eca8f994aa402f2; '
    '_zdmA.time=1672911753291.0.https%3A%2F%2Fwww.smzdm.com%2F; '
    'sess=BA-2IafqWZR5nmD%2F5mIoLpZleji1sX5auxM0B0ms93b98DrMa9%2Fp8HlQgyJR2'
    '%2FifBJNoDHHB0K3zTMqU4YiHzgytW275YnLKEqkvOE87hDiGcvDRR6JRgj%2FxVAK; user=user%3A4724251029%7C4724251029; '
    'smzdm_id=4724251029'
]

for i in range(len(cookie)):
    msg = ""
    print(f'开始第{i + 1}个帐号签到')

    ts = int(round(time.time() * 1000))
    url = 'https://user-api.smzdm.com/robot/token'
    headers = {
        'Host': 'user-api.smzdm.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': f'{cookie[i]}',
        'User-Agent': 'smzdm_android_V10.4.1 rv:841 (22021211RC;Android12;zh)smzdmapp',
    }
    data = {
        "f": "android",
        "v": "10.4.1",
        "weixin": 1,
        "time": ts,
        "sign": hashlib.md5(bytes(f'f=android&time={ts}&v=10.4.1&weixin=1&key=apr1$AwP!wRRT$gJ/q.X24poeBInlUJC',
                                  encoding='utf-8')).hexdigest().upper()
    }
    session = requests.Session()
    html = session.post(url=url, data=data)
    html = requests.post(url=url, headers=headers, data=data)
    result = html.json()
    token = result['data']['token']

    Timestamp = int(round(time.time() * 1000))
    data = {
        "f": "android",
        "sk": "ierkM0OZZbsuBKLoAgQ6OJneLMXBQXmzX+LXkNTuKch8Ui2jGlahuFyWIzBiDq/L",
        "v": "10.4.1",
        "weixin": 1,
        "time": Timestamp,
        "token": token,
        "sign": hashlib.md5(bytes(
            f'f=android&sk=ierkM0OZZbsuBKLoAgQ6OJneLMXBQXmzX+LXkNTuKch8Ui2jGlahuFyWIzBiDq/L&time={Timestamp}&token={token}&v=10.4.1&weixin=1&key=apr1$AwP!wRRT$gJ/q.X24poeBInlUJC',
            encoding='utf-8')).hexdigest().upper()
    }
    url = 'https://user-api.smzdm.com/checkin'
    url2 = 'https://user-api.smzdm.com/checkin/all_reward'
    headers = {
        'Host': 'user-api.smzdm.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': f'{cookie[i]}',
        'User-Agent': 'smzdm_android_V10.4.1 rv:841 (22021211RC;Android12;zh)smzdmapp',
    }
    html = session.post(url=url, headers=headers, data=data)
    html2 = session.post(url=url2, headers=headers, data=data)
    result = json.loads(html.text)['error_msg']
    msg += (f'第{i + 1}个帐号: \n' + result + '\n' + html2.text)
    message2qywxapp(QYWX_CORPID, QYWX_AGENTID, QYWX_CORPSECRET, QYWX_TOUSER, "什么值得买", msg)




