import requests
import time
import datetime


headers = {
    'Host': 'mrp.creditcard.hxb.com.cn',
    'Accept': 'application/json, text/plain, */*',
    'timestamp': '1710827639395',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Sec-Fetch-Mode': 'cors',
    'sessionId': 'c7c216b0-1304-48d0-b465-b418ee05e32b',
    'Origin': 'https://mrp.creditcard.hxb.com.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) MicroMessenger/6.8.0(0x16080000) MacWechat/3.7(0x13070011) Safari/605.1.15 NetType/WIFI',
    'Referer': 'https://mrp.creditcard.hxb.com.cn/veryinterested/index.html?responseCode=00&isFirstLogin=0&pageSwitch=null&surname=%E7%86%8A%E6%AC%A3',
    'Sec-Fetch-Dest': 'empty',
    'sign': 'L5msOCoUq4+J1RnVWaK4F0o23HpGI71nlTxNUebX95MVC+vfPE7kud0mWHN8wB+gSAy0K5Mhh7i+5HZX+HiTKHVKEsgAs4VJo2M4c/JG1M3IZGhsl3EyLY6QMVpN1+IgdrSbWvd/16NC3u7UWXV3mSYmxj+W1TS9wYTqNfwiO38Ld87ptcaIDSo4v2ZGxDc+MULgL7X59ZOjJ63ic6fynlKYFHeWxQi6kVEjk/xw0z3kPessXSSVOChVxcblXVxrSZ4GtDpujtLso9OhbDyAUfG1qnIIyokjkl5a8qedV+3cRBDbYmB6Weh+C90HRdDVg0TuYeYgGtIxtaSURSVSNw==',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
    'cur_data': '{"issueNum":1,"prodCode":"SPSJ002615"}',
    'sessionId': '618b58b3-6c7c-4851-a034-b319c20f2212'
}

def send_request():
    res = requests.post('https://mrp.creditcard.hxb.com.cn/online/3009', headers=headers, data=data)
    print(res.text)
    return res


target_time = datetime.datetime(2025, 2, 19, 14, 0, 0)
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
