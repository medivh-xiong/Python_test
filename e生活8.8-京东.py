import requests
import time
import datetime
from requests.exceptions import Timeout

cookies = {
    'ARK_ID': 'JS63bcc2ea95e3b0d2d80bfb27f710230463bc',
    'FZ_STROAGE.ofpay.com': 'eyJBUktTVVBFUiI6eyJncHNfY2l0eSI6IiIsInByb2plY3RfdHlwZSI6IueIsei0rTguOOa0u%2BWKqCJ9LCJTRUVTSU9OSUQiOiJhZTc3Y2QyNjVmNTRhYTFlIiwiU0VFU0lPTkRBVEUiOjE3MTA3MjUxNjM5NTgsIkFOU0FQUElEIjoiZXNoZW5naHVvdGVzdCIsIkFOUyRERUJVRyI6MiwiQU5TVVBMT0FEVVJMIjoiaHR0cHM6Ly9lbGlmZS11cC5hbmFseXN5c2RhdGEuY29tLyIsIkFSS19JRCI6IkpTNjNiY2MyZWE5NWUzYjBkMmQ4MGJmYjI3ZjcxMDIzMDQ2M2JjIiwiRlJJU1RJTUUiOmZhbHNlLCJBUktGUklTVFBST0ZJTEUiOiIyMDI0LTAzLTA0IDA5OjU4OjI5LjY0NiIsIkFSS19MT0dJTklEIjoidE44YkVBWnRmZ0hVcUdQUHVYZjlTRCs4TEZRaVdyWUwifQ%3D%3D',
    'br-session-js-sdk': '80aefb27-6313-4bf8-bde5-cea0b5bc5005|1710725148486|1710725163362|20',
    'ARK_STARTUP': 'eyJTVEFSVFVQIjp0cnVlLCJTVEFSVFVQVElNRSI6IjIwMjQtMDMtMTggMDk6MjU6NDkuMTY4In0%3D',
    'OF_WEB_SESSION': '',
    't_s_interactiveIGoChoose': '6eeb9b4af00d9f540302ce0852a2ae8c',
    'unionToken_interactiveIGoChoose': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJKeXZxK0dxTEtrOVY4Z0tnZ3RISlFBPT0iLCJhY3Rpdml0eU5vIjoiIiwiYWNjb3VudCI6Ikp5dnErR3FMS2s5VjhnS2dndEhKUUE9PSIsInVzZXJJZCI6IjMzMTY0NjcwIiwibWVyY2hhbnRJZCI6IjAwMDAwMDAxOTEiLCJjdXN0b21lckluZm8iOiJ7XCJkZXZpY2VfaWRcIjpcIjdBNTYxMTA4LTM2ODAtNDEzQi04REEyLTExMDczNkI2MEJBNlwiLFwibG9naW5UeXBlXCI6XCJpbnRlcmFjdGl2ZUlHb0Nob29zZVwiLFwiY2l0eV9jb2RlXCI6XCIzMjAxMDBcIixcImNpc25vXCI6XCJKeXZxK0dxTEtrOVY4Z0tnZ3RISlFBPT1cIixcImlzTmV3VXNlclwiOlwiMFwiLFwibWFya2V0SWRcIjpcIk05MjMxNTYyODkwMTY2OTI3MzZcIixcImNpdHlfbmFtZVwiOlwi5Y2X5Lqs5biCXCIsXCJwaG9uZVwiOlwiMTU5NTEwMDMwNzhcIixcImZyb21FbnRyeVwiOlwiQVBQXCIsXCJjdXJyZW50VGltZU1pbGxpc1wiOlwiMTcxMDcyNTE0Nzg1NVwiLFwidXNlclV1aWRcIjpcInROOGJFQVp0ZmdIVXFHUFB1WGY5U0QrOExGUWlXcllMXCIsXCJjdXN0X2lkXCI6XCJ0TjhiRUFadGZnSFVxR1BQdVhmOVNEKzhMRlFpV3JZTFwiLFwiaW52aXRhdGlvbkNvZGVcIjpcIlc0RlRHWFwifSIsImNpc25vIjoiSnl2cStHcUxLazlWOGdLZ2d0SEpRQT09IiwibG9naW5UeXBlIjoiaW50ZXJhY3RpdmVJR29DaG9vc2UiLCJ1bmlvbk1hcmtldElkIjoiTTkyMzE1NjI4OTAxNjY5MjczNiIsImlhdCI6MTcxMDcyNTE0OCwiZXhwIjoxNzEwNzI2OTQ4fQ.Tq21L6qiInBPRhzSuvpLhTtj377FKWowlAHt4BiZIkE',
    'unionToken_interactiveIGoChoose_loginParam': 'YWZzZ1RDZnNyYjJKSlVBUU8vVTNuNjd1Wkd3UXdtYmZ3THJkejBZWFZ6aEdJVVNHOWJWSDhCbmsxeEhKNjV1dUxxTG9RSEg1TzJtUlh5VUM4VUpUY1lBR1FoQVlJSDQ0ejRBRUE0M1pEdHpHUnJmUVFFaXRCUzd1V0JXLzh1WVI4RXNPUnpnUlNMWURMai9qUTVlUWt4RkNickNqc0VPIG82cWVYTHo4QUFaZ2p4UmtjWTRTVTBMaXNJVEZ1MEpWamNSUEt3N0Q5alBHc1dYWUhyQjhwNVgwYWpZQnpxWnpzTTVVanR4NVN4WnhZNUxwZ2xaWVIwektNV3l3R1NPcmllbXgyVmFPaDJQNm54USB3dDhzc1NzVndRNFZMY2FldlB1VTFINHpKVllDNVVrWXJGL1dFbHlZaGpFTFZ2bGxGZHFXWVQ4TSBQQi8gRVY2bTgyMTFnbTVSSlB3em13cURqblJySmRIbzAgRzVVRzlRZVdOVjdUQnBIMVNUbnpMYW45SUJkRHFqMTNMcHVVUlhNdzc0VGs5RmtsRlNhOHAvUDFtSjhwYnNBN1p0bVBYTlF3eExJSzV6cGZGUnI2YWY3dU4yc2VjYk9WRTZ6YXcyRTlhQzU5OXd1ODBLZzVFdGhJRFhTWTdxVGpHVG1XVGVLdkFtSm85eWRJd3ViIGZCVUNGaU5kaFBlN0FRY2c4VzhjejRKZUhzNDBzam5hajkwMUZnRWU0S094TFloV0RPVVRXWUlsYTA1VzhGNERaL1lEb3BuWGpoVU16bzJ6MXBJNGowODF5cmV4ZFo3ZktZIDZCMEFBUSB6OGN4ay92eW1OcFRNdVdmVk01MElBMnZjQ2drcEpoZkdOenhrOFRWUnpTRnVQbzhKUG1wN1FKdVJZUWtablByMmtxSjR5Wkt3UVpmVTZPcklRS0JESDlTdHRsaU5uM3c0c0JVd2p1anJoeHNtaERvSnBXNGxxOW1keWM1MGxqVHZKVlRsY2c4UDgzb2hkQ0Z4QWVlR2Zl',
}

headers = {
    'Host': 'market-web.ofpay.com',
    'Accept': '*/*',
    'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJKeXZxK0dxTEtrOVY4Z0tnZ3RISlFBPT0iLCJhY3Rpdml0eU5vIjoiIiwiYWNjb3VudCI6Ikp5dnErR3FMS2s5VjhnS2dndEhKUUE9PSIsInVzZXJJZCI6IjMzMTY0NjcwIiwibWVyY2hhbnRJZCI6IjAwMDAwMDAxOTEiLCJjdXN0b21lckluZm8iOiJ7XCJkZXZpY2VfaWRcIjpcIjdBNTYxMTA4LTM2ODAtNDEzQi04REEyLTExMDczNkI2MEJBNlwiLFwibG9naW5UeXBlXCI6XCJpbnRlcmFjdGl2ZUlHb0Nob29zZVwiLFwiY2l0eV9jb2RlXCI6XCIzMjAxMDBcIixcImNpc25vXCI6XCJKeXZxK0dxTEtrOVY4Z0tnZ3RISlFBPT1cIixcImlzTmV3VXNlclwiOlwiMFwiLFwibWFya2V0SWRcIjpcIk05MjMxNTYyODkwMTY2OTI3MzZcIixcImNpdHlfbmFtZVwiOlwi5Y2X5Lqs5biCXCIsXCJwaG9uZVwiOlwiMTU5NTEwMDMwNzhcIixcImZyb21FbnRyeVwiOlwiQVBQXCIsXCJjdXJyZW50VGltZU1pbGxpc1wiOlwiMTcxMDcyNTE0Nzg1NVwiLFwidXNlclV1aWRcIjpcInROOGJFQVp0ZmdIVXFHUFB1WGY5U0QrOExGUWlXcllMXCIsXCJjdXN0X2lkXCI6XCJ0TjhiRUFadGZnSFVxR1BQdVhmOVNEKzhMRlFpV3JZTFwiLFwiaW52aXRhdGlvbkNvZGVcIjpcIlc0RlRHWFwifSIsImNpc25vIjoiSnl2cStHcUxLazlWOGdLZ2d0SEpRQT09IiwibG9naW5UeXBlIjoiaW50ZXJhY3RpdmVJR29DaG9vc2UiLCJ1bmlvbk1hcmtldElkIjoiTTkyMzE1NjI4OTAxNjY5MjczNiIsImlhdCI6MTcxMDcyNTE0OCwiZXhwIjoxNzEwNzI2OTQ4fQ.Tq21L6qiInBPRhzSuvpLhTtj377FKWowlAHt4BiZIkE',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Sec-Fetch-Mode': 'cors',
    'UUID': '1710725163965PCOR45JL',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 F-OFST  elife_moblie_ios  fullversion:6.0.2  BSComponentVersion:5.4 WorkStationChannel:0 isBreak:0  ICBCiPhoneBSNew 6.0.2 iphone os wkwebview:true',
    'Referer': 'https://market-web.ofpay.com/h5/union/interactiveIGoChoose/index?loginParams=afsgTCfsrb2JJUAQO/U3n67uZGwQwmbfwLrdz0YXVzhGIUSG9bVH8Bnk1xHJ65uuLqLoQHH5O2mRXyUC8UJTcYAGQhAYIH44z4AEA43ZDtzGRrfQQEitBS7uWBW/8uYR8EsORzgRSLYDLj/jQ5eQkxFCbrCjsEO+o6qeXLz8AAZgjxRkcY4SU0LisITFu0JVjcRPKw7D9jPGsWXYHrB8p5X0ajYBzqZzsM5Ujtx5SxZxY5LpglZYR0zKMWywGSOriemx2VaOh2P6nxQ+wt8ssSsVwQ4VLcaevPuU1H4zJVYC5UkYrF/WElyYhjELVvllFdqWYT8M+PB/+EV6m8211gm5RJPwzmwqDjnRrJdHo0+G5UG9QeWNV7TBpH1STnzLan9IBdDqj13LpuURXMw74Tk9FklFSa8p/P1mJ8pbsA7ZtmPXNQwxLIK5zpfFRr6af7uN2secbOVE6zaw2E9aC599wu80Kg5EthIDXSY7qTjGTmWTeKvAmJo9ydIwub+fBUCFiNdhPe7AQcg8W8cz4JeHs40sjnaj901FgEe4KOxLYhWDOUTWYIla05W8F4DZ/YDopnXjhUMzo2z1pI4j081yrexdZ7fKY+6B0AAQ+z8cxk/vymNpTMuWfVM50IA2vcCgkpJhfGNzxk8TVRzSFuPo8JPmp7QJuRYQkZnPr2kqJ4yZKwQZfU6OrIQKBDH9SttliNn3w4sBUwjujrhxsmhDoJpW4lq9mdyc50ljTvJVTlcg8P83ohdCFxAeeGfe',
    # 'Cookie': 'ARK_ID=JS63bcc2ea95e3b0d2d80bfb27f710230463bc; FZ_STROAGE.ofpay.com=eyJBUktTVVBFUiI6eyJncHNfY2l0eSI6IiIsInByb2plY3RfdHlwZSI6IueIsei0rTguOOa0u%2BWKqCJ9LCJTRUVTSU9OSUQiOiJhZTc3Y2QyNjVmNTRhYTFlIiwiU0VFU0lPTkRBVEUiOjE3MTA3MjUxNjM5NTgsIkFOU0FQUElEIjoiZXNoZW5naHVvdGVzdCIsIkFOUyRERUJVRyI6MiwiQU5TVVBMT0FEVVJMIjoiaHR0cHM6Ly9lbGlmZS11cC5hbmFseXN5c2RhdGEuY29tLyIsIkFSS19JRCI6IkpTNjNiY2MyZWE5NWUzYjBkMmQ4MGJmYjI3ZjcxMDIzMDQ2M2JjIiwiRlJJU1RJTUUiOmZhbHNlLCJBUktGUklTVFBST0ZJTEUiOiIyMDI0LTAzLTA0IDA5OjU4OjI5LjY0NiIsIkFSS19MT0dJTklEIjoidE44YkVBWnRmZ0hVcUdQUHVYZjlTRCs4TEZRaVdyWUwifQ%3D%3D; br-session-js-sdk=80aefb27-6313-4bf8-bde5-cea0b5bc5005|1710725148486|1710725163362|20; ARK_STARTUP=eyJTVEFSVFVQIjp0cnVlLCJTVEFSVFVQVElNRSI6IjIwMjQtMDMtMTggMDk6MjU6NDkuMTY4In0%3D; OF_WEB_SESSION=; t_s_interactiveIGoChoose=6eeb9b4af00d9f540302ce0852a2ae8c; unionToken_interactiveIGoChoose=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJKeXZxK0dxTEtrOVY4Z0tnZ3RISlFBPT0iLCJhY3Rpdml0eU5vIjoiIiwiYWNjb3VudCI6Ikp5dnErR3FMS2s5VjhnS2dndEhKUUE9PSIsInVzZXJJZCI6IjMzMTY0NjcwIiwibWVyY2hhbnRJZCI6IjAwMDAwMDAxOTEiLCJjdXN0b21lckluZm8iOiJ7XCJkZXZpY2VfaWRcIjpcIjdBNTYxMTA4LTM2ODAtNDEzQi04REEyLTExMDczNkI2MEJBNlwiLFwibG9naW5UeXBlXCI6XCJpbnRlcmFjdGl2ZUlHb0Nob29zZVwiLFwiY2l0eV9jb2RlXCI6XCIzMjAxMDBcIixcImNpc25vXCI6XCJKeXZxK0dxTEtrOVY4Z0tnZ3RISlFBPT1cIixcImlzTmV3VXNlclwiOlwiMFwiLFwibWFya2V0SWRcIjpcIk05MjMxNTYyODkwMTY2OTI3MzZcIixcImNpdHlfbmFtZVwiOlwi5Y2X5Lqs5biCXCIsXCJwaG9uZVwiOlwiMTU5NTEwMDMwNzhcIixcImZyb21FbnRyeVwiOlwiQVBQXCIsXCJjdXJyZW50VGltZU1pbGxpc1wiOlwiMTcxMDcyNTE0Nzg1NVwiLFwidXNlclV1aWRcIjpcInROOGJFQVp0ZmdIVXFHUFB1WGY5U0QrOExGUWlXcllMXCIsXCJjdXN0X2lkXCI6XCJ0TjhiRUFadGZnSFVxR1BQdVhmOVNEKzhMRlFpV3JZTFwiLFwiaW52aXRhdGlvbkNvZGVcIjpcIlc0RlRHWFwifSIsImNpc25vIjoiSnl2cStHcUxLazlWOGdLZ2d0SEpRQT09IiwibG9naW5UeXBlIjoiaW50ZXJhY3RpdmVJR29DaG9vc2UiLCJ1bmlvbk1hcmtldElkIjoiTTkyMzE1NjI4OTAxNjY5MjczNiIsImlhdCI6MTcxMDcyNTE0OCwiZXhwIjoxNzEwNzI2OTQ4fQ.Tq21L6qiInBPRhzSuvpLhTtj377FKWowlAHt4BiZIkE; unionToken_interactiveIGoChoose_loginParam=YWZzZ1RDZnNyYjJKSlVBUU8vVTNuNjd1Wkd3UXdtYmZ3THJkejBZWFZ6aEdJVVNHOWJWSDhCbmsxeEhKNjV1dUxxTG9RSEg1TzJtUlh5VUM4VUpUY1lBR1FoQVlJSDQ0ejRBRUE0M1pEdHpHUnJmUVFFaXRCUzd1V0JXLzh1WVI4RXNPUnpnUlNMWURMai9qUTVlUWt4RkNickNqc0VPIG82cWVYTHo4QUFaZ2p4UmtjWTRTVTBMaXNJVEZ1MEpWamNSUEt3N0Q5alBHc1dYWUhyQjhwNVgwYWpZQnpxWnpzTTVVanR4NVN4WnhZNUxwZ2xaWVIwektNV3l3R1NPcmllbXgyVmFPaDJQNm54USB3dDhzc1NzVndRNFZMY2FldlB1VTFINHpKVllDNVVrWXJGL1dFbHlZaGpFTFZ2bGxGZHFXWVQ4TSBQQi8gRVY2bTgyMTFnbTVSSlB3em13cURqblJySmRIbzAgRzVVRzlRZVdOVjdUQnBIMVNUbnpMYW45SUJkRHFqMTNMcHVVUlhNdzc0VGs5RmtsRlNhOHAvUDFtSjhwYnNBN1p0bVBYTlF3eExJSzV6cGZGUnI2YWY3dU4yc2VjYk9WRTZ6YXcyRTlhQzU5OXd1ODBLZzVFdGhJRFhTWTdxVGpHVG1XVGVLdkFtSm85eWRJd3ViIGZCVUNGaU5kaFBlN0FRY2c4VzhjejRKZUhzNDBzam5hajkwMUZnRWU0S094TFloV0RPVVRXWUlsYTA1VzhGNERaL1lEb3BuWGpoVU16bzJ6MXBJNGowODF5cmV4ZFo3ZktZIDZCMEFBUSB6OGN4ay92eW1OcFRNdVdmVk01MElBMnZjQ2drcEpoZkdOenhrOFRWUnpTRnVQbzhKUG1wN1FKdVJZUWtablByMmtxSjR5Wkt3UVpmVTZPcklRS0JESDlTdHRsaU5uM3c0c0JVd2p1anJoeHNtaERvSnBXNGxxOW1keWM1MGxqVHZKVlRsY2c4UDgzb2hkQ0Z4QWVlR2Zl',
    'Sec-Fetch-Dest': 'empty',
}
params = {
    'awardId': 'W1190950079482429441',
    'goodsId': '',
    'invitationCode': '',
    'gameAccount': '15951003078',
    'eventVisitorId': 'RE_9fb3abb5185cb29fb3145060cf9147b41709517505517B1LIBKQF',
}

def send_request():
    try:
        res = requests.get(url='https://market-web.ofpay.com/h5/union/api/draw/interactiveIGoChoose/A1190947451528544256', headers=headers, cookies=cookies, params=params, timeout=2)
        print(res.text)
        return res
    except Timeout:
        print("请求超时，但程序没有崩溃！")

target_time = datetime.datetime(2024, 3, 18, 9, 30, 0)
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
    if response.text.find('W1190950079482429441') != -1:
        print("抢购成功")
        exit()
    elif response.text.find('您存在待支付订单') != -1:
        print("抢购成功")
        exit()
    else:
        print('领取失败, 重新领取')
        time.sleep(2)
