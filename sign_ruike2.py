import requests

cookies = {
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

params = {
    'mod': 'logging',
    'action': 'login',
    'loginsubmit': 'yes',
    'infloat': 'yes',
    'lssubmit': 'yes',
    'inajax': '1',
}

data = {
    'fastloginfield': 'username',
    'username': 'xxshijian',
    'password': 'asd123',
    'formhash': '01b02ef4',
    'quickforward': 'yes',
    'handlekey': 'ls',
}

response = requests.post('https://www.ruike1.com/member.php', params=params, cookies=cookies, headers=headers, data=data)