import time

import requests

cookies = {
    'zzhh_2132_sid': 'W4551b',
    'zzhh_2132_saltkey': 'YO7Irbsb',
}

headers = {
    'Host': 'www.ruike1.com',
    # 'Cookie': 'Hm_lvt_73ad58a7cf08cf5833714aed91aa7068=1688545814; zzhh_2132_sid=sN06n3; zzhh_2132_saltkey=ApDTfg3R; zzhh_2132_lastvisit=1690353085; zzhh_2132_onlineusernum=603; zzhh_2132_lastact=1690356686%09home.php%09misc; zzhh_2132_sendmail=1; Hm_lpvt_73ad58a7cf08cf5833714aed91aa7068=1690356739',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'upgrade-insecure-requests': '1',
    'origin': 'https://www.ruike1.com',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'iframe',
    'referer': 'https://www.ruike1.com/',
    'accept-language': 'zh-CN,zh;q=0.9',
}

login_params = {
    'mod': 'logging',
    'action': 'login',
    'loginsubmit': 'yes',
    'infloat': 'yes',
    'lssubmit': 'yes',
    'inajax': '1',
}

login_data = {
    'fastloginfield': 'username',
    'username': 'xxshijianjs',
    'password': 'x83229837',
    'quickforward': 'yes',
    'handlekey': 'ls',
}

sign_params = {
    'operation': 'qiandao',
    'format': 'global_usernav_extra',
    'inajax': '1',
    'ajaxtarget': 'k_misign_topb',
}

pre_res = requests.get('https://www.ruike1.com/index.php', cookies=cookies, headers=headers)
formhash = pre_res.text[pre_res.text.find('formhash=') + 9:pre_res.text.find('formhash=') + 9 + 8]
login_data['formhash'] = formhash
login_url = "https://www.ruike1.com/member.php"
session = requests.session()
loginRes = session.post(url=login_url, params=login_params, cookies=cookies, headers=headers, data=login_data)

auth = ''
# 生成随机8位英文字母
key = ''


for ck in session.cookies:
    # 取出带有zzhh_2132_saltkey的ck
    if ck.name == 'zzhh_2132_auth':
        auth = ck.value

sign_cookies = {
    "zzhh_2132_auth": auth,
    "zzhh_2132_saltkey": "YO7Irbsb"
}

print(sign_cookies)

re = session.get("https://www.ruike1.com/", headers=headers, cookies=sign_cookies)
formhash = re.text[re.text.find('formhash=') + 9:re.text.find('formhash=') + 9 + 8]
# print(formhash)

sign_params['formhash'] = formhash

sign_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:122.0) Gecko/20100101 Firefox/122.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://www.ruike1.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}


sign_rsp = session.get('https://www.ruike1.com/k_misign-sign.html', cookies=sign_cookies, params=sign_params,
                        headers=sign_headers)


print(sign_rsp.text)
