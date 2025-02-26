import requests
import time
import datetime

cookies = {
    'OF_WEB_SESSION': '',
    'br-session-js-sdk': '67c6af4f-72f9-4502-997a-a1d5159fdc87|1720401920265|1720401991960|24',
    't_s_interactiveIGoChoose': 'ebc97a688f06fcdca65adaaaecedbde1',
    'unionToken_interactiveIGoChoose': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJKeXZxK0dxTEtrOVY4Z0tnZ3RISlFBPT0iLCJhY3Rpdml0eU5vIjoiIiwiYWNjb3VudCI6Ikp5dnErR3FMS2s5VjhnS2dndEhKUUE9PSIsInVzZXJJZCI6IjMzMTY0NjcwIiwibWVyY2hhbnRJZCI6IjAwMDAwMDAxOTEiLCJjdXN0b21lckluZm8iOiJ7XCJkZXZpY2VfaWRcIjpcIjdBNTYxMTA4LTM2ODAtNDEzQi04REEyLTExMDczNkI2MEJBNlwiLFwibG9naW5UeXBlXCI6XCJpbnRlcmFjdGl2ZUlHb0Nob29zZVwiLFwiY2l0eV9jb2RlXCI6XCIzMjAxMDBcIixcImNpc25vXCI6XCJKeXZxK0dxTEtrOVY4Z0tnZ3RISlFBPT1cIixcImlzTmV3VXNlclwiOlwiMFwiLFwiY2lzbm9faHNtXCI6XCI4MGY4YWEyYWMyMmM1OTAzMDExYjYxYTIyMzE1NDdmNFwiLFwibWFya2V0SWRcIjpcIk05MjMxNTYyODkwMTY2OTI3MzZcIixcImNpdHlfbmFtZVwiOlwi5Y2X5Lqs5biCXCIsXCJwaG9uZVwiOlwiMTU5NTEwMDMwNzhcIixcImZyb21FbnRyeVwiOlwiQVBQXCIsXCJjdXJyZW50VGltZU1pbGxpc1wiOlwiMTcyMDQwMTkxOTkxNFwiLFwidXNlclV1aWRcIjpcInROOGJFQVp0ZmdIVXFHUFB1WGY5U0QrOExGUWlXcllMXCIsXCJjdXN0X2lkXCI6XCJ0TjhiRUFadGZnSFVxR1BQdVhmOVNEKzhMRlFpV3JZTFwiLFwiaW52aXRhdGlvbkNvZGVcIjpcIlc0RlRHWFwifSIsImNpc25vIjoiSnl2cStHcUxLazlWOGdLZ2d0SEpRQT09IiwibG9naW5UeXBlIjoiaW50ZXJhY3RpdmVJR29DaG9vc2UiLCJ1bmlvbk1hcmtldElkIjoiTTkyMzE1NjI4OTAxNjY5MjczNiIsImlhdCI6MTcyMDQwMTk5MiwiZXhwIjoxNzIwNDAzNzkyfQ.0ZnNVNgdiSYBnZRhkLbsEUST31XuaU_Hfq_uV4IpGRs',
    'ARK_ID': 'JSe602ec205fd3598be7a567b790e2a2cde602',
    'ARK_STARTUP': 'eyJTVEFSVFVQIjp0cnVlLCJTVEFSVFVQVElNRSI6IjIwMjQtMDctMDggMDk6MjU6MjEuNjMyIn0%3D',
    'FZ_STROAGE.ofpay.com': 'eyJTRUVTSU9OSUQiOiJhZDlhNjJhOGJmMmQ3ZjNmIiwiU0VFU0lPTkRBVEUiOjE3MjA0MDE5MjE5MDksIkFOU0FQUElEIjoiZXNoZW5naHVvdGVzdCIsIkFOUyRERUJVRyI6MiwiQU5TVVBMT0FEVVJMIjoiaHR0cHM6Ly9lbGlmZS11cC5hbmFseXN5c2RhdGEuY29tLyIsIkZSSVNUREFZIjoiMjAyNDA3MDgiLCJGUklTVElNRSI6ZmFsc2UsIkFSS1NVUEVSIjp7Imdwc19jaXR5IjoiIiwicHJvamVjdF90eXBlIjoi54ix6LStOC445rS75YqoIn0sIkFSS19JRCI6IkpTZTYwMmVjMjA1ZmQzNTk4YmU3YTU2N2I3OTBlMmEyY2RlNjAyIiwiQVJLRlJJU1RQUk9GSUxFIjoiMjAyNC0wNy0wOCAwOToyNToyMS42MzkiLCJBUktfTE9HSU5JRCI6InROOGJFQVp0ZmdIVXFHUFB1WGY5U0QrOExGUWlXcllMIn0%3D',
}

headers = {
    'Host': 'market-web.ofpay.com',
    'Accept': '*/*',
    'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJKeXZxK0dxTEtrOVY4Z0tnZ3RISlFBPT0iLCJhY3Rpdml0eU5vIjoiIiwiYWNjb3VudCI6Ikp5dnErR3FMS2s5VjhnS2dndEhKUUE9PSIsInVzZXJJZCI6IjMzMTY0NjcwIiwibWVyY2hhbnRJZCI6IjAwMDAwMDAxOTEiLCJjdXN0b21lckluZm8iOiJ7XCJkZXZpY2VfaWRcIjpcIjdBNTYxMTA4LTM2ODAtNDEzQi04REEyLTExMDczNkI2MEJBNlwiLFwibG9naW5UeXBlXCI6XCJpbnRlcmFjdGl2ZUlHb0Nob29zZVwiLFwiY2l0eV9jb2RlXCI6XCIzMjAxMDBcIixcImNpc25vXCI6XCJKeXZxK0dxTEtrOVY4Z0tnZ3RISlFBPT1cIixcImlzTmV3VXNlclwiOlwiMFwiLFwiY2lzbm9faHNtXCI6XCI4MGY4YWEyYWMyMmM1OTAzMDExYjYxYTIyMzE1NDdmNFwiLFwibWFya2V0SWRcIjpcIk05MjMxNTYyODkwMTY2OTI3MzZcIixcImNpdHlfbmFtZVwiOlwi5Y2X5Lqs5biCXCIsXCJwaG9uZVwiOlwiMTU5NTEwMDMwNzhcIixcImZyb21FbnRyeVwiOlwiQVBQXCIsXCJjdXJyZW50VGltZU1pbGxpc1wiOlwiMTcyMDQwMTkxOTkxNFwiLFwidXNlclV1aWRcIjpcInROOGJFQVp0ZmdIVXFHUFB1WGY5U0QrOExGUWlXcllMXCIsXCJjdXN0X2lkXCI6XCJ0TjhiRUFadGZnSFVxR1BQdVhmOVNEKzhMRlFpV3JZTFwiLFwiaW52aXRhdGlvbkNvZGVcIjpcIlc0RlRHWFwifSIsImNpc25vIjoiSnl2cStHcUxLazlWOGdLZ2d0SEpRQT09IiwibG9naW5UeXBlIjoiaW50ZXJhY3RpdmVJR29DaG9vc2UiLCJ1bmlvbk1hcmtldElkIjoiTTkyMzE1NjI4OTAxNjY5MjczNiIsImlhdCI6MTcyMDQwMTk5MiwiZXhwIjoxNzIwNDAzNzkyfQ.0ZnNVNgdiSYBnZRhkLbsEUST31XuaU_Hfq_uV4IpGRs',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Sec-Fetch-Mode': 'cors',
    'UUID': '1720401992733NO01RCA0',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 F-OFST  elife_moblie_ios  fullversion:6.1.2  BSComponentVersion:5.4 WorkStationChannel:0 isBreak:0  ICBCiPhoneBSNew 6.1.2 iphone os wkwebview:true',
    'Referer': 'https://market-web.ofpay.com/h5/union/interactiveIGoChoose/index?loginParams=afsgTCfsrb2JJUAQO/U3n67uZGwQwmbfwLrdz0YXVzhGIUSG9bVH8Bnk1xHJ65uuLqLoQHH5O2mRXyUC8UJTcYAGQhAYIH44z4AEA43ZDtzGRrfQQEitBS7uWBW/8uYR8EsORzgRSLYDLj/jQ5eQkxFCbrCjsEO+o6qeXLz8AAZgjxRkcY4SU0LisITFu0JVvP1hIaaAFrAEGnDz0J/47+II6nGly+k2h6otKUFzA/l4ln0rKAZo5qVG2WADi/Vzp5YjrZXeMlnjW+H7P4MLMkKsCyeOHxj2wQaTHIAKe2omYNuFHSJAQP6M7XZ2l9r+SSDctLiVDuihhk0UUvdrTjAFnxuWyeMfiIbgeCWCJdBedNLOGKR+bCZscSfcAKLgFUtVn/wJUH5MbVefwq8n+EeAzPwQiBHhMHdTBZcMvvJ8yQvA79WWv0jCCNz8aQdZ3rKMljoOg9GCrbr6vfHuCJCL3UYq3V8cy1KdkzxuLMKE62qR8+eba9t05HsXzH7VxwqVEHQpID1HwaJAMuyRGsTMYHJDWY//l9mlKvKNrKmDwPJEjYhKQUbGUt0F2F4g0/zl0/tKGE4R/gzwE8fSeTetOs1o52NSrVxA1PZVf5oH0BFMXgbFvGAnwWTNApRq5Sk9nd9Uh9WZKUD2C5VVHxmbpjNkpjy2frE814VaD1rcu3GFqI3sRJ6vrH/nBEHXTQhTKpNwD7CLq5cni3r3UaebVVA8w3tW+TkpdiGQmDbiAuZMP7ZFlzZQmKL8rUtv',
    # 'Cookie': 'OF_WEB_SESSION=; br-session-js-sdk=67c6af4f-72f9-4502-997a-a1d5159fdc87|1720401920265|1720401991960|24; t_s_interactiveIGoChoose=ebc97a688f06fcdca65adaaaecedbde1; unionToken_interactiveIGoChoose=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJKeXZxK0dxTEtrOVY4Z0tnZ3RISlFBPT0iLCJhY3Rpdml0eU5vIjoiIiwiYWNjb3VudCI6Ikp5dnErR3FMS2s5VjhnS2dndEhKUUE9PSIsInVzZXJJZCI6IjMzMTY0NjcwIiwibWVyY2hhbnRJZCI6IjAwMDAwMDAxOTEiLCJjdXN0b21lckluZm8iOiJ7XCJkZXZpY2VfaWRcIjpcIjdBNTYxMTA4LTM2ODAtNDEzQi04REEyLTExMDczNkI2MEJBNlwiLFwibG9naW5UeXBlXCI6XCJpbnRlcmFjdGl2ZUlHb0Nob29zZVwiLFwiY2l0eV9jb2RlXCI6XCIzMjAxMDBcIixcImNpc25vXCI6XCJKeXZxK0dxTEtrOVY4Z0tnZ3RISlFBPT1cIixcImlzTmV3VXNlclwiOlwiMFwiLFwiY2lzbm9faHNtXCI6XCI4MGY4YWEyYWMyMmM1OTAzMDExYjYxYTIyMzE1NDdmNFwiLFwibWFya2V0SWRcIjpcIk05MjMxNTYyODkwMTY2OTI3MzZcIixcImNpdHlfbmFtZVwiOlwi5Y2X5Lqs5biCXCIsXCJwaG9uZVwiOlwiMTU5NTEwMDMwNzhcIixcImZyb21FbnRyeVwiOlwiQVBQXCIsXCJjdXJyZW50VGltZU1pbGxpc1wiOlwiMTcyMDQwMTkxOTkxNFwiLFwidXNlclV1aWRcIjpcInROOGJFQVp0ZmdIVXFHUFB1WGY5U0QrOExGUWlXcllMXCIsXCJjdXN0X2lkXCI6XCJ0TjhiRUFadGZnSFVxR1BQdVhmOVNEKzhMRlFpV3JZTFwiLFwiaW52aXRhdGlvbkNvZGVcIjpcIlc0RlRHWFwifSIsImNpc25vIjoiSnl2cStHcUxLazlWOGdLZ2d0SEpRQT09IiwibG9naW5UeXBlIjoiaW50ZXJhY3RpdmVJR29DaG9vc2UiLCJ1bmlvbk1hcmtldElkIjoiTTkyMzE1NjI4OTAxNjY5MjczNiIsImlhdCI6MTcyMDQwMTk5MiwiZXhwIjoxNzIwNDAzNzkyfQ.0ZnNVNgdiSYBnZRhkLbsEUST31XuaU_Hfq_uV4IpGRs; ARK_ID=JSe602ec205fd3598be7a567b790e2a2cde602; ARK_STARTUP=eyJTVEFSVFVQIjp0cnVlLCJTVEFSVFVQVElNRSI6IjIwMjQtMDctMDggMDk6MjU6MjEuNjMyIn0%3D; FZ_STROAGE.ofpay.com=eyJTRUVTSU9OSUQiOiJhZDlhNjJhOGJmMmQ3ZjNmIiwiU0VFU0lPTkRBVEUiOjE3MjA0MDE5MjE5MDksIkFOU0FQUElEIjoiZXNoZW5naHVvdGVzdCIsIkFOUyRERUJVRyI6MiwiQU5TVVBMT0FEVVJMIjoiaHR0cHM6Ly9lbGlmZS11cC5hbmFseXN5c2RhdGEuY29tLyIsIkZSSVNUREFZIjoiMjAyNDA3MDgiLCJGUklTVElNRSI6ZmFsc2UsIkFSS1NVUEVSIjp7Imdwc19jaXR5IjoiIiwicHJvamVjdF90eXBlIjoi54ix6LStOC445rS75YqoIn0sIkFSS19JRCI6IkpTZTYwMmVjMjA1ZmQzNTk4YmU3YTU2N2I3OTBlMmEyY2RlNjAyIiwiQVJLRlJJU1RQUk9GSUxFIjoiMjAyNC0wNy0wOCAwOToyNToyMS42MzkiLCJBUktfTE9HSU5JRCI6InROOGJFQVp0ZmdIVXFHUFB1WGY5U0QrOExGUWlXcllMIn0%3D',
    'Sec-Fetch-Dest': 'empty',
}

params = {
    'awardId': 'W1155095480565628948',
    'goodsId': '',
    'invitationCode': '',
    'gameAccount': '15951003078',
    'eventVisitorId': 'RE_9fb3abb5185cb29fb3145060cf9147b41709517505517B1LIBKQF',
}

def send_request():
    try:
        res = requests.get(url='https://market-web.ofpay.com/h5/union/api/draw/interactiveIGoChoose/A923620157585358848',
                           headers=headers, cookies=cookies, params=params)
        print(res.text)
        return res
    except Exception as e:
        print(f"网络请求出错: {e}")
        return None


target_time = datetime.datetime(2024, 4, 1, 9, 30, 30)
time_diff = (target_time - datetime.datetime.now()).total_seconds()
if time_diff > 0:
    time.sleep(time_diff)

result = True

while result:
    response = send_request()
    if response.status_code != 200:
        print('请求失败')
        time.sleep(1)
        continue
    if response.text.find('本周名额已抢光') != -1:
        print('已经抢完')
        exit()
    elif response.text.find('您存在待支付订单') != -1:
        print("抢购成功")
        exit()
    elif response.text.find('W1155095480565628948') != -1:
        print("抢购成功")
        exit()
    else:
        print('领取失败, 重新领取')
        time.sleep(1)
