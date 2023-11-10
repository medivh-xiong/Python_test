import time

import requests

login_cookies = {
    'Hm_lvt_73ad58a7cf08cf5833714aed91aa7068': '1688545814',
    'zzhh_2132_sid': 'sN06n3',
    'zzhh_2132_saltkey': 'ApDTfg3R',
    'zzhh_2132_lastvisit': '1690353085',
    'zzhh_2132_onlineusernum': '603',
    'zzhh_2132_lastact': '1690356686%09home.php%09misc',
    'zzhh_2132_sendmail': '1',
    'Hm_lpvt_73ad58a7cf08cf5833714aed91aa7068': '1690356739',
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
    'formhash': '01b02ef4',
    'quickforward': 'yes',
    'handlekey': 'ls',
}

sign_params = {
    'operation': 'qiandao',
    'format': 'global_usernav_extra',
    'formhash': '6e521d90',
}

Global_saltkey = ""

sign_cookies = {
    'Hm_lvt_73ad58a7cf08cf5833714aed91aa7068': '1688545814',
    'zzhh_2132_saltkey': 'PEe3hE9U',
    'zzhh_2132_lastvisit': '1690340240',
    'zzhh_2132_sendsmscode': 'ee57c211dd4af99460e5153c95d46450',
    'zzhh_2132_validatecode': 'vt28',
    'zzhh_2132_ulastactivity': '8fdbUAT4K2si7iq7jv9woUZx7e%2F8egkziORzPsP0YuV%2B99m9Jf8U',
    'zzhh_2132_auth': 'cf84Ir714ldgKdBB3KrK3gVkqQOETxpufyARhF7qZ1ICM%2FFGNqiavhuYPPFNzj2I7BRCOPVRpqRXcg2mWjvF2NDRIA',
    'zzhh_2132_myrepeat_rr': 'R0',
    'zzhh_2132_connect_is_bind': '0',
    'zzhh_2132_nofavfid': '1',
    'zzhh_2132_noticeTitle': '1',
    'zzhh_2132_onlineusernum': '628',
    'zzhh_2132_sid': 'w45626',
    'zzhh_2132_lip': '180.111.122.241%2C1690350221',
    'zzhh_2132_sendmail': '1',
    'Hm_lpvt_73ad58a7cf08cf5833714aed91aa7068':  str(int(time.time())),
    'zzhh_2132_lastact': str(int(time.time()) + 48) + '%09misc.php%09patch',
}


login_url = "https://www.ruike1.com/member.php"
session = requests.session()
loginRes = session.post(url=login_url,  params=login_params, cookies=login_cookies, headers=headers, data=login_data)

auth = ''

# 生成随机8位英文字母
key = 'ApDTfg3R'

for ck in session.cookies:
    # 取出带有zzhh_2132_saltkey的ck
    if ck.name == 'zzhh_2132_saltkey':
        key = ck.value
    if ck.name == 'zzhh_2132_auth':
        auth = ck.value

sign_cookies['zzhh_2132_saltkey'] = key
sign_cookies['zzhh_2132_auth'] = auth

re = session.get("https://www.ruike1.com/", headers=headers, cookies=sign_cookies)
# 从re.text中取得formhash=53042f33&中formhash的值
formhash = re.text[re.text.find('formhash=') + 9:re.text.find('formhash=') + 9 + 8]
# print(formhash)
print(re.text)


sign_params['formhash'] = formhash

print('\n------------')
print(sign_cookies)
print('------------')

print('\n------------')
print(sign_params)
print('------------\n')

sign_rsp = requests.get('https://www.ruike1.com/k_misign-sign.html', cookies=sign_cookies, params=sign_params, headers=headers)
print(sign_rsp.text)
