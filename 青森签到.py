# -*- coding:utf-8 -*-
import json
import requests

headers = {
    'Host': 'www.cyanmori.com',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'accept': '*/*',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'origin': 'https://www.cyanmori.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.cyanmori.com/auth/login',
    'accept-language': 'zh-CN,zh;q=0.9',
}

sign_headers = {
    'Host': 'www.cyanmori.com',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'origin': 'https://www.cyanmori.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.cyanmori.com/user',
    'accept-language': 'zh-CN,zh;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
    'email': '296853461@qq.com',
    'passwd': 'x83229837',
}

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
            "url": "https://www.cyanmori.com/user",
            "btntxt": "详情",
        },
    }
    requests.post(url=f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={token2}", data=json.dumps(data2))


proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
}

def handler():
    session = requests.Session()
    loginRes = session.post(url='https://www.cyanmori.com/auth/login', headers=headers, data=data, timeout=5, proxies=proxies)
    loginJson = json.loads(loginRes.content)
    print(loginRes.text)
    if loginJson['msg'] == "登录成功":
        print("登录成功")
        signRes = session.post(url='https://www.cyanmori.com/user/checkin', headers=sign_headers, timeout=5, proxies=proxies)
        signJson = json.loads(signRes.content)
        msg = signJson['msg']
        print(msg)
        message2qywxapp(QYWX_CORPID, QYWX_AGENTID, QYWX_CORPSECRET, QYWX_TOUSER, "青森机场", msg)


handler()
