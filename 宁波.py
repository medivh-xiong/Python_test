import time
import datetime
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

data = '170f52cccd2565cbd6fe8e7ec682fb53\x1dP/e3bz7WdFLYT/nx836YbNMdSp701bkyRZ0i+CPwNednxKx2NhyX5Pp+10I9bLHT+p6m+Xe01piW1cVE/v7kzv8VgUHqvBnORG6BY81AcRe+vQxGwgXookh7RKsiQgnFg+HfmeYniN4dAePV3eV8ixDjSFc4Kjl5uM1wFelQC/LYvgE9te9Si3zHt09WTHRlbw1mHWtoQJZ4WLoeGz7bFfkR3xkfrIk5L7cD/rg+F4wnxBkxd8LtmnOXmey4tGYtOtb3iFULewq7aA366dYlXi59TEniOkChfD/eHujWw39ElFXgYiwnlAnFKdiNW7dOT0UVhzBCNz0YN8YmicqjW/3F2HhMKSv2xvE3ExYwb2s=\x1dbciDGbOkiquOaRMaFtYdnS2QgufNgp28z4TDGnL00J2XWijuahGksN8bPcU+lZgae9Pg/nlaTLWAURst1LfgLPt7iWchwX0jdt7H9v9WyYSxEyuMhy/nEr5wtmhtcOja5+P6obhiUhuNRwUbDZ/vi5dg0RG85HHMByMYK6/u1cYl8jqbqf4dwjffuuSfG1H1L2JPcZ8Yl0cJkR8JRFg8pb7AACkDnnqugfWKyMOXJBMxh/bopP5jgpX4yCNDP73xic6BeJcUOO00Lu4lVIsgFRERReStLdUN91HYPBCjEv8rLsabFpp4gV1qEDv2anDA/mi6XQ8UeZkElCp6RktuUg=='

def send_request():
    res = requests.post('https://aaph.nbcb.com.cn/cpa-wx/api/cpaActCenter/joinAct', cookies=cookies,
                             headers=headers, data=data)
    print(res.text)
    return res


target_time = datetime.datetime(2024, 1, 29, 10, 0, 0)
time_diff = (target_time - datetime.datetime.now()).total_seconds()
if time_diff > 0:
    time.sleep(time_diff)

result = True

while result:
    response = send_request()
    if response.status_code != 200:
        print('请求失败')
        time.sleep(0.1)
        continue
    if response.text.find('兑换未开始'):
        print('还未开始')
        time.sleep(0.1)
        continue
    elif response.text.find('很抱歉,您目前尚未具备资格'):
        print('领取成功')
        exit()
    else:
        print('领取失败, 重新领取')
        time.sleep(0.1)
