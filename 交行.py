import requests

cookies = {
    'GW_SESSION': 'e823249d-92a3-470a-b798-8d1b290a636f',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%221026660850%22%2C%22%24device_id%22%3A%2218d52ec8f06293d-0e67ea7ab0a631-2b08150b-2073600-18d52ec8f072661%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_campaign%22%3A%22%E6%96%B0%E6%98%A5%E7%A4%BC%E5%8C%85%E5%A4%A7%E6%B4%BE%E9%80%81%EF%BC%8C%E6%9C%80%E9%AB%98%E8%B5%A22000%E5%85%83%E5%B9%B4%E5%A4%9C%E9%A5%AD%E5%9F%BA%E9%87%91%22%7D%2C%22first_id%22%3A%2218d52ec8f06293d-0e67ea7ab0a631-2b08150b-2073600-18d52ec8f072661%22%7D',
    'sajssdk_2015_cross_new_user': '1',
}

headers = {
    'Host': 'aaph.nbcb.com.cn',
    'Referer': 'https://aaph.nbcb.com.cn/cpa/webview/pageTemplate/index.html',
    # 'Cookie': 'GW_SESSION=e823249d-92a3-470a-b798-8d1b290a636f; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221026660850%22%2C%22%24device_id%22%3A%2218d52ec8f06293d-0e67ea7ab0a631-2b08150b-2073600-18d52ec8f072661%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_campaign%22%3A%22%E6%96%B0%E6%98%A5%E7%A4%BC%E5%8C%85%E5%A4%A7%E6%B4%BE%E9%80%81%EF%BC%8C%E6%9C%80%E9%AB%98%E8%B5%A22000%E5%85%83%E5%B9%B4%E5%A4%9C%E9%A5%AD%E5%9F%BA%E9%87%91%22%7D%2C%22first_id%22%3A%2218d52ec8f06293d-0e67ea7ab0a631-2b08150b-2073600-18d52ec8f072661%22%7D; sajssdk_2015_cross_new_user=1',
    'X-GW-DATA-ENCRYPT-ID': '6010010005',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) MicroMessenger/6.8.0(0x16080000) MacWechat/3.7(0x13070011) Safari/605.1.15 NetType/WIFI',
    'X-GW-TIME': '1706493320119',
    'X-GW-APP-ID': '6010010005',
    'Origin': 'https://aaph.nbcb.com.cn',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Site': 'same-origin',
    'X-GW-TIME-OFFSET': '0',
    'token': '86a40b79020655c7e4a6790d21ae793a.0c143012830dae8d0dd1be914c1fc45b.57a915fa4da1ba8f3503c3d5df1c840b',
    'X-GW-NONCE': '567a0d91-92e9-4f47-8bd0-0ee794cea414',
    'Authorization': '86a40b79020655c7e4a6790d21ae793a.0c143012830dae8d0dd1be914c1fc45b.57a915fa4da1ba8f3503c3d5df1c840b',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'x-client-token': 'eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJjcGEtd3giLCJ1c2VySWQiOiI5MDEiLCJuYW1lIjoiY3BhLXd4IiwiZXhwIjoxOTk4NDcwMTE0fQ.UKzMhs7FwV0gt99LliT13Iw2RE7HSx_xnyWLIUwwF5H42qA1VunviNlSNJMkTqkFFUIWHAi8kuKHi3sCiibyWfpcWUBMa025hefk5ymaN5fIc5iJ7EIloOQWSZk6W2rUUCGYhIaWq6nnR9Y5BlzaFCtdo5Ll2v95_0KRIWoJJBY',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=UTF-8',
    'Sec-Fetch-Mode': 'cors',
}

data = '68666206b2bc11e432c8c5312503032b\x1duGUYkJZ+0r2zOySb3nDfiDQgHXxK/hRYOPTiFYupvF2xNDsLoTBp0ZWDOO+AQKL3fD4Lmh7Z4v+vhNeECFxb1+LdmKyhvCQmJhE1TkTjCv/SzOnLKDlHjkAkaCxkV7yYt0xLBZWi0faCTdrfRpSlcrQFnFPgDk1qIAf8kx0OrvzY8e38xhEeRLU3bxGmYG1aPL9qXc5mqfuw3dDVwfW8fs6Ql3C0eb/pneHB5pgaj64qSQKIP26nFHQM5W583f1z1HarCOelmSX6BNA7hSijEo4jAlTON3bbL9hbX4NjKjM9FbvVmSvkV3iEQeKZ6tL2Hj8FwOAF3PTi1cdI1mhT3UWUNX1NF5AnUZk+e7eDWxA=\x1dGof/MSXiu4y00pZFkMY4AbJupVdxGcVtd9Wa2cSwns72geh/xfGXY9UDsXqVulPCXIXagwyUF0bgUqFVDZgeLHGTtKdIreGwKymOrIOyIvPNL8gVXMr3L4UcFEBezoP3NeyE4DiisLwhKYpYa9Pgwypg5kpCe6BepEKn7q2o9pDyxhGWXS33H1+/cDleegPZHb+l9bxCItv50waRW7fCgv4kK0N7h0itZssOtBy+gdsBxmo9bDgFsc4jdttVysk3BEIYBkiXZqRllj/T0xeLUQ3xhC7uT6bYQpOD7iD2Euj3q4XnSZLBwRLcTbnpuzCWOpTi8swTtOyajpOXdGOiSA=='

response = requests.post('https://aaph.nbcb.com.cn/cpa-wx/api/cpaActCenter/joinAct', cookies=cookies, headers=headers, data=data)
print(response.text)