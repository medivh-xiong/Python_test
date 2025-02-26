import requests
import json

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

session = requests.Session()
loginRes = session.post(url='https://www.cyanmori.com/auth/login', headers=headers, data=data)
loginJson = json.loads(loginRes.content)
if loginJson['msg'] == "登录成功":
    print("登录成功")
    signRes = session.post(url='https://www.cyanmori.com/user/checkin', headers=sign_headers)
    signJson = json.loads(signRes.content)
    msg = signJson['msg']
    print(msg)
# response = session.post('https://www.cyanmori.com/user/checkin')
# print(response)
