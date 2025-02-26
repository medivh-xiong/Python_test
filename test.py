import requests

cookies = {
    'zzhh_2132_auth': '6f47RH4dbBArCiWCAInZs%2FxztS0tuoVaD%2BAGca0aWQbwz85dV4%2BJvMqjTsKc9Oudrfh%2FczQfU5uINhm5BREQtxhD',
    'zzhh_2132_saltkey': 'zq4NcCno',
}

headers = {
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

params = {
    'operation': 'qiandao',
    'format': 'global_usernav_extra',
    'formhash': '2bf535e2',
    'inajax': '1',
    'ajaxtarget': 'k_misign_topb',
}

response = requests.get('https://www.ruike1.com/k_misign-sign.html', params=params, cookies=cookies, headers=headers)
print(response.text)