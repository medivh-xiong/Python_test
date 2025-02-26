import requests
import time
import datetime
from requests.exceptions import Timeout

cookies = {
    'OF_WEB_SESSION': '',
    'br-session-js-sdk': '7485b8b2-d464-4966-a6f2-741564ba3126|1721006490890|1721006580738|15',
    't_s_interactiveIGoChoose': 'bd7a37722b3c54a35b8492e6d0429d1a',
    'unionToken_interactiveIGoChoose': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJKeXZxK0dxTEtrOVY4Z0tnZ3RISlFBPT0iLCJhY3Rpdml0eU5vIjoiIiwiYWNjb3VudCI6Ikp5dnErR3FMS2s5VjhnS2dndEhKUUE9PSIsInVzZXJJZCI6IjMzMTY0NjcwIiwibWVyY2hhbnRJZCI6IjAwMDAwMDAxOTEiLCJjdXN0b21lckluZm8iOiJ7XCJkZXZpY2VfaWRcIjpcIjdBNTYxMTA4LTM2ODAtNDEzQi04REEyLTExMDczNkI2MEJBNlwiLFwibG9naW5UeXBlXCI6XCJpbnRlcmFjdGl2ZUlHb0Nob29zZVwiLFwiY2l0eV9jb2RlXCI6XCIzMjAxMDBcIixcImNpc25vXCI6XCJKeXZxK0dxTEtrOVY4Z0tnZ3RISlFBPT1cIixcImlzTmV3VXNlclwiOlwiMFwiLFwiY2lzbm9faHNtXCI6XCI4MGY4YWEyYWMyMmM1OTAzMDExYjYxYTIyMzE1NDdmNFwiLFwibWFya2V0SWRcIjpcIk05MjMxNTYyODkwMTY2OTI3MzZcIixcImNpdHlfbmFtZVwiOlwi5Y2X5Lqs5biCXCIsXCJwaG9uZVwiOlwiMTU5NTEwMDMwNzhcIixcImZyb21FbnRyeVwiOlwiQVBQXCIsXCJjdXJyZW50VGltZU1pbGxpc1wiOlwiMTcyMTAwNjQ5MDQxN1wiLFwidXNlclV1aWRcIjpcInROOGJFQVp0ZmdIVXFHUFB1WGY5U0QrOExGUWlXcllMXCIsXCJjdXN0X2lkXCI6XCJ0TjhiRUFadGZnSFVxR1BQdVhmOVNEKzhMRlFpV3JZTFwiLFwiaW52aXRhdGlvbkNvZGVcIjpcIlc0RlRHWFwifSIsImNpc25vIjoiSnl2cStHcUxLazlWOGdLZ2d0SEpRQT09IiwibG9naW5UeXBlIjoiaW50ZXJhY3RpdmVJR29DaG9vc2UiLCJ1bmlvbk1hcmtldElkIjoiTTkyMzE1NjI4OTAxNjY5MjczNiIsImlhdCI6MTcyMTAwNjU4MCwiZXhwIjoxNzIxMDA4MzgwfQ.vxYn1MJsfyeW6yENgB5KY4-9bqp6kS_JS5awwfo76Uo',
    'unionToken_interactiveIGoChoose_loginParam': 'YWZzZ1RDZnNyYjJKSlVBUU8vVTNuNjd1Wkd3UXdtYmZ3THJkejBZWFZ6aEdJVVNHOWJWSDhCbmsxeEhKNjV1dUxxTG9RSEg1TzJtUlh5VUM4VUpUY1lBR1FoQVlJSDQ0ejRBRUE0M1pEdHpHUnJmUVFFaXRCUzd1V0JXLzh1WVI4RXNPUnpnUlNMWURMai9qUTVlUWt4RkNickNqc0VPIG82cWVYTHo4QUFaZ2p4UmtjWTRTVTBMaXNJVEZ1MEpWN3NFZU41OElmaXluUW8wYjBEVlQvUUhTZE05RkxRVFp1YXltcXgyd3BwenF4WUxFR2NxOEUzMzdwRCBQNDZRYjA3U2pIUXlzNlBqQzBaWTltWVVyVnpEUVFmL0ZRc2RYMCBTMzl1aEFnb3BSZTFBWElocXdXQzZrQ3dOL01KanVHTEwxWGFDbll6aHFrajg2Rm9sa0NSQXlNR1FkTWJucjBOd0JmIG1kRk9SS0wwRCB3MVFpIEZ6d2UvVmgvbkEgNk9DZU9rUUk0cUhmQS82bTczdkE3c0xnSTZFR0hZT1JuR09UaktXektoaGd0elJFMUJuM1kxS1RaS0RpUFUgWFgxMXZuWW1ZYnQ5SDFFZWtQY2lHVFZnb3lTIFhNIHhMV1lOaEFaYm0wMEdkTzJpSmd0ajJHVi92Z2Y1MU92akY5OEt4eEg0eXY1ME5SUDA4L0RLa2U4ankvRGp0QVVLb0NpNzZnNXhmRTUvaHFMUC91eXR4OXZqdmFRZHFwM3Ruelg0Vk1JdmlVZGZnRFlreHhrYVF0WGtROTM5cnEvTXFGQmlzOUliQ2JDTnkzZnNvOHprazQgcGdoZUlxdEEvSW00OUh6TElybVp3OVR6RmptaWZtRkhBUW9odGY3MlJjRDhtMDBBaDdzVjQycVpwTXd2IERZWXFsYk8gNmlmQndxVy8gS01BM2VDV0EyNzlIMnJ4L1N5UjVlZUhXbVV0cFBGIGhWMzZCRGNucVRUMFVEUWlwWUlJQ3FuY2pWRHlR',
    'ARK_ID': 'JSe602ec205fd3598be7a567b790e2a2cde602',
    'FZ_STROAGE.ofpay.com': 'eyJBUktTVVBFUiI6eyJncHNfY2l0eSI6IiIsInByb2plY3RfdHlwZSI6IueIsei0rTguOOa0u%2BWKqCJ9LCJTRUVTSU9OSUQiOiI1MDY3MGRmNDVjOWE5Y2ZmIiwiU0VFU0lPTkRBVEUiOjE3MjEwMDY1Mzg1NDAsIkFOU0FQUElEIjoiZXNoZW5naHVvdGVzdCIsIkFOUyRERUJVRyI6MiwiQU5TVVBMT0FEVVJMIjoiaHR0cHM6Ly9lbGlmZS11cC5hbmFseXN5c2RhdGEuY29tLyIsIkZSSVNUREFZIjoiMjAyNDA3MDgiLCJGUklTVElNRSI6ZmFsc2UsIkFSS19JRCI6IkpTZTYwMmVjMjA1ZmQzNTk4YmU3YTU2N2I3OTBlMmEyY2RlNjAyIiwiQVJLRlJJU1RQUk9GSUxFIjoiMjAyNC0wNy0wOCAwOToyNToyMS42MzkiLCJBUktfTE9HSU5JRCI6InROOGJFQVp0ZmdIVXFHUFB1WGY5U0QrOExGUWlXcllMIn0%3D',
    'ARK_STARTUP': 'eyJTVEFSVFVQIjp0cnVlLCJTVEFSVFVQVElNRSI6IjIwMjQtMDctMTUgMDk6MjE6MzIuNDA1In0%3D',
}

headers = {
    'Host': 'market-web.ofpay.com',
    'Accept': '*/*',
    'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJKeXZxK0dxTEtrOVY4Z0tnZ3RISlFBPT0iLCJhY3Rpdml0eU5vIjoiIiwiYWNjb3VudCI6Ikp5dnErR3FMS2s5VjhnS2dndEhKUUE9PSIsInVzZXJJZCI6IjMzMTY0NjcwIiwibWVyY2hhbnRJZCI6IjAwMDAwMDAxOTEiLCJjdXN0b21lckluZm8iOiJ7XCJkZXZpY2VfaWRcIjpcIjdBNTYxMTA4LTM2ODAtNDEzQi04REEyLTExMDczNkI2MEJBNlwiLFwibG9naW5UeXBlXCI6XCJpbnRlcmFjdGl2ZUlHb0Nob29zZVwiLFwiY2l0eV9jb2RlXCI6XCIzMjAxMDBcIixcImNpc25vXCI6XCJKeXZxK0dxTEtrOVY4Z0tnZ3RISlFBPT1cIixcImlzTmV3VXNlclwiOlwiMFwiLFwiY2lzbm9faHNtXCI6XCI4MGY4YWEyYWMyMmM1OTAzMDExYjYxYTIyMzE1NDdmNFwiLFwibWFya2V0SWRcIjpcIk05MjMxNTYyODkwMTY2OTI3MzZcIixcImNpdHlfbmFtZVwiOlwi5Y2X5Lqs5biCXCIsXCJwaG9uZVwiOlwiMTU5NTEwMDMwNzhcIixcImZyb21FbnRyeVwiOlwiQVBQXCIsXCJjdXJyZW50VGltZU1pbGxpc1wiOlwiMTcyMTAwNjQ5MDQxN1wiLFwidXNlclV1aWRcIjpcInROOGJFQVp0ZmdIVXFHUFB1WGY5U0QrOExGUWlXcllMXCIsXCJjdXN0X2lkXCI6XCJ0TjhiRUFadGZnSFVxR1BQdVhmOVNEKzhMRlFpV3JZTFwiLFwiaW52aXRhdGlvbkNvZGVcIjpcIlc0RlRHWFwifSIsImNpc25vIjoiSnl2cStHcUxLazlWOGdLZ2d0SEpRQT09IiwibG9naW5UeXBlIjoiaW50ZXJhY3RpdmVJR29DaG9vc2UiLCJ1bmlvbk1hcmtldElkIjoiTTkyMzE1NjI4OTAxNjY5MjczNiIsImlhdCI6MTcyMTAwNjU4MCwiZXhwIjoxNzIxMDA4MzgwfQ.vxYn1MJsfyeW6yENgB5KY4-9bqp6kS_JS5awwfo76Uo',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Sec-Fetch-Mode': 'cors',
    'UUID': '1721006581297QSJM78R1',
    'User-Agent': 'ICBCiPhone ICBCiPhoneBSNew F-ePass 24.06 ICBCiPhone epassComponentVersion:24.06 iPhone10,1 16.5.1 7A561108-3680-413B-8DA2-110736B60BA6 4G BSComponentVersion:24.06 ADDRs:%E5%8D%97%E4%BA%AC%E5%B8%82:ADDReMozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 F-OFST  elife_moblie_ios  fullversion:6.1.2  BSComponentVersion:5.4 WorkStationChannel:0 isBreak:0  fontsizescale:1 wkwebview:true ICBCiPhoneBSNew 6.1.2 iphone os wkwebview:true',
    'Referer': 'https://market-web.ofpay.com/h5/union/interactiveIGoChoose/index?loginParams=afsgTCfsrb2JJUAQO/U3n67uZGwQwmbfwLrdz0YXVzhGIUSG9bVH8Bnk1xHJ65uuLqLoQHH5O2mRXyUC8UJTcYAGQhAYIH44z4AEA43ZDtzGRrfQQEitBS7uWBW/8uYR8EsORzgRSLYDLj/jQ5eQkxFCbrCjsEO+o6qeXLz8AAZgjxRkcY4SU0LisITFu0JV7sEeN58IfiynQo0b0DVT/QHSdM9FLQTZuaymqx2wppzqxYLEGcq8E337pD+P46Qb07SjHQys6PjC0ZY9mYUrVzDQQf/FQsdX0+S39uhAgopRe1AXIhqwWC6kCwN/MJjuGLL1XaCnYzhqkj86FolkCRAyMGQdMbnr0NwBf+mdFORKL0D+w1Qi+Fzwe/Vh/nA+6OCeOkQI4qHfA/6m73vA7sLgI6EGHYORnGOTjKWzKhhgtzRE1Bn3Y1KTZKDiPU+XX11vnYmYbt9H1EekPciGTVgoyS+XM+xLWYNhAZbm00GdO2iJgtj2GV/vgf51OvjF98KxxH4yv50NRP08/DKke8jy/DjtAUKoCi76g5xfE5/hqLP/uytx9vjvaQdqp3tnzX4VMIviUdfgDYkxxkaQtXkQ939rq/MqFBis9IbCbCNy3fso8zkk4+pgheIqtA/Im49HzLIrmZw9TzFjmifmFHAQohtf72RcD8m00Ah7sV42qZpMwv+DYYqlbO+6ifBwqW/+KMA3eCWA279H2rx/SyR5eeHWmUtpPF+hV36BDcnqTT0UDQipYIICqncjVDyQ',
    # 'Cookie': 'OF_WEB_SESSION=; br-session-js-sdk=7485b8b2-d464-4966-a6f2-741564ba3126|1721006490890|1721006580738|15; t_s_interactiveIGoChoose=bd7a37722b3c54a35b8492e6d0429d1a; unionToken_interactiveIGoChoose=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJKeXZxK0dxTEtrOVY4Z0tnZ3RISlFBPT0iLCJhY3Rpdml0eU5vIjoiIiwiYWNjb3VudCI6Ikp5dnErR3FMS2s5VjhnS2dndEhKUUE9PSIsInVzZXJJZCI6IjMzMTY0NjcwIiwibWVyY2hhbnRJZCI6IjAwMDAwMDAxOTEiLCJjdXN0b21lckluZm8iOiJ7XCJkZXZpY2VfaWRcIjpcIjdBNTYxMTA4LTM2ODAtNDEzQi04REEyLTExMDczNkI2MEJBNlwiLFwibG9naW5UeXBlXCI6XCJpbnRlcmFjdGl2ZUlHb0Nob29zZVwiLFwiY2l0eV9jb2RlXCI6XCIzMjAxMDBcIixcImNpc25vXCI6XCJKeXZxK0dxTEtrOVY4Z0tnZ3RISlFBPT1cIixcImlzTmV3VXNlclwiOlwiMFwiLFwiY2lzbm9faHNtXCI6XCI4MGY4YWEyYWMyMmM1OTAzMDExYjYxYTIyMzE1NDdmNFwiLFwibWFya2V0SWRcIjpcIk05MjMxNTYyODkwMTY2OTI3MzZcIixcImNpdHlfbmFtZVwiOlwi5Y2X5Lqs5biCXCIsXCJwaG9uZVwiOlwiMTU5NTEwMDMwNzhcIixcImZyb21FbnRyeVwiOlwiQVBQXCIsXCJjdXJyZW50VGltZU1pbGxpc1wiOlwiMTcyMTAwNjQ5MDQxN1wiLFwidXNlclV1aWRcIjpcInROOGJFQVp0ZmdIVXFHUFB1WGY5U0QrOExGUWlXcllMXCIsXCJjdXN0X2lkXCI6XCJ0TjhiRUFadGZnSFVxR1BQdVhmOVNEKzhMRlFpV3JZTFwiLFwiaW52aXRhdGlvbkNvZGVcIjpcIlc0RlRHWFwifSIsImNpc25vIjoiSnl2cStHcUxLazlWOGdLZ2d0SEpRQT09IiwibG9naW5UeXBlIjoiaW50ZXJhY3RpdmVJR29DaG9vc2UiLCJ1bmlvbk1hcmtldElkIjoiTTkyMzE1NjI4OTAxNjY5MjczNiIsImlhdCI6MTcyMTAwNjU4MCwiZXhwIjoxNzIxMDA4MzgwfQ.vxYn1MJsfyeW6yENgB5KY4-9bqp6kS_JS5awwfo76Uo; unionToken_interactiveIGoChoose_loginParam=YWZzZ1RDZnNyYjJKSlVBUU8vVTNuNjd1Wkd3UXdtYmZ3THJkejBZWFZ6aEdJVVNHOWJWSDhCbmsxeEhKNjV1dUxxTG9RSEg1TzJtUlh5VUM4VUpUY1lBR1FoQVlJSDQ0ejRBRUE0M1pEdHpHUnJmUVFFaXRCUzd1V0JXLzh1WVI4RXNPUnpnUlNMWURMai9qUTVlUWt4RkNickNqc0VPIG82cWVYTHo4QUFaZ2p4UmtjWTRTVTBMaXNJVEZ1MEpWN3NFZU41OElmaXluUW8wYjBEVlQvUUhTZE05RkxRVFp1YXltcXgyd3BwenF4WUxFR2NxOEUzMzdwRCBQNDZRYjA3U2pIUXlzNlBqQzBaWTltWVVyVnpEUVFmL0ZRc2RYMCBTMzl1aEFnb3BSZTFBWElocXdXQzZrQ3dOL01KanVHTEwxWGFDbll6aHFrajg2Rm9sa0NSQXlNR1FkTWJucjBOd0JmIG1kRk9SS0wwRCB3MVFpIEZ6d2UvVmgvbkEgNk9DZU9rUUk0cUhmQS82bTczdkE3c0xnSTZFR0hZT1JuR09UaktXektoaGd0elJFMUJuM1kxS1RaS0RpUFUgWFgxMXZuWW1ZYnQ5SDFFZWtQY2lHVFZnb3lTIFhNIHhMV1lOaEFaYm0wMEdkTzJpSmd0ajJHVi92Z2Y1MU92akY5OEt4eEg0eXY1ME5SUDA4L0RLa2U4ankvRGp0QVVLb0NpNzZnNXhmRTUvaHFMUC91eXR4OXZqdmFRZHFwM3Ruelg0Vk1JdmlVZGZnRFlreHhrYVF0WGtROTM5cnEvTXFGQmlzOUliQ2JDTnkzZnNvOHprazQgcGdoZUlxdEEvSW00OUh6TElybVp3OVR6RmptaWZtRkhBUW9odGY3MlJjRDhtMDBBaDdzVjQycVpwTXd2IERZWXFsYk8gNmlmQndxVy8gS01BM2VDV0EyNzlIMnJ4L1N5UjVlZUhXbVV0cFBGIGhWMzZCRGNucVRUMFVEUWlwWUlJQ3FuY2pWRHlR; ARK_ID=JSe602ec205fd3598be7a567b790e2a2cde602; FZ_STROAGE.ofpay.com=eyJBUktTVVBFUiI6eyJncHNfY2l0eSI6IiIsInByb2plY3RfdHlwZSI6IueIsei0rTguOOa0u%2BWKqCJ9LCJTRUVTSU9OSUQiOiI1MDY3MGRmNDVjOWE5Y2ZmIiwiU0VFU0lPTkRBVEUiOjE3MjEwMDY1Mzg1NDAsIkFOU0FQUElEIjoiZXNoZW5naHVvdGVzdCIsIkFOUyRERUJVRyI6MiwiQU5TVVBMT0FEVVJMIjoiaHR0cHM6Ly9lbGlmZS11cC5hbmFseXN5c2RhdGEuY29tLyIsIkZSSVNUREFZIjoiMjAyNDA3MDgiLCJGUklTVElNRSI6ZmFsc2UsIkFSS19JRCI6IkpTZTYwMmVjMjA1ZmQzNTk4YmU3YTU2N2I3OTBlMmEyY2RlNjAyIiwiQVJLRlJJU1RQUk9GSUxFIjoiMjAyNC0wNy0wOCAwOToyNToyMS42MzkiLCJBUktfTE9HSU5JRCI6InROOGJFQVp0ZmdIVXFHUFB1WGY5U0QrOExGUWlXcllMIn0%3D; ARK_STARTUP=eyJTVEFSVFVQIjp0cnVlLCJTVEFSVFVQVElNRSI6IjIwMjQtMDctMTUgMDk6MjE6MzIuNDA1In0%3D',
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

target_time = datetime.datetime(2024, 7, 15, 9, 30, 0)
time_diff = (target_time - datetime.datetime.now()).total_seconds()
if time_diff > 0:
    time.sleep(time_diff)

result = True

while result:
    response = send_request()
    print(response.text)
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
