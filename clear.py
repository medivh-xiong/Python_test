import requests
import time
import datetime
from requests.exceptions import Timeout

cookies = {
    'br-session-js-sdk': '9ea3a9b5-5620-4a13-b842-bbf276a94375|1715306721028|1715306746056|26',
    'OF_WEB_SESSION': '',
    'unionToken_P1197956369804165120': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0TjhiRUFadGZnSFVxR1BQdVhmOVNEKzhMRlFpV3JZTCIsImFjY291bnQiOiJ0TjhiRUFadGZnSFVxR1BQdVhmOVNEKzhMRlFpV3JZTCIsInVzZXJJZCI6IjExNTU5NTUwOSIsIm1JZCI6IjAwMDAwMDExMDYiLCJwaG9uZU5vIjoiMTU5NTEwMDMwNzgiLCJzY29wZVByb21vdGVJZCI6IlAxMTk3OTU2MzY5ODA0MTY1MTIwIiwic2NvcGVUb2tlbiI6IjY3OGU1ODEyOTA2YjQzOWVlY2FhMzJlN2YzMjNkNWFlIiwiZW50cnlUeXBlIjoiaWNiY0VsaWZlSWdvUnVpeGluZyIsImVudHJ5UGxhdGZvcm0iOiJINSIsImN1c3RvbWVySW5mbyI6IntcImVudHJ5VHlwZVwiOlwiaWNiY0VsaWZlSWdvUnVpeGluZ1wiLFwiY2l0eV9uYW1lXCI6XCLljZfkuqzluIJcIixcImRldmljZV9pZFwiOlwiNDhCRUQ5QjItMDBGNy00RTY5LUE4OTctNUZCQjM4N0YzQTREXCIsXCJwaG9uZVwiOlwiMTU5NTEwMDMwNzhcIixcImN1cnJlbnRUaW1lTWlsbGlzXCI6XCIxNzE1MzA2NzIwNTEwXCIsXCJlbnRyeVBsYXRmb3JtXCI6XCJINVwiLFwiY2l0eV9jb2RlXCI6XCIzMjAxMDBcIixcImNpc25vXCI6XCJKeXZxK0dxTEtrOVY4Z0tnZ3RISlFBPT1cIixcImlzTmV3VXNlclwiOlwiMFwiLFwic2NvcGVQcm9tb3RlSWRcIjpcIlAxMTk3OTU2MzY5ODA0MTY1MTIwXCIsXCJjdXN0X2lkXCI6XCJ0TjhiRUFadGZnSFVxR1BQdVhmOVNEKzhMRlFpV3JZTFwifSIsImlhdCI6MTcxNTMwNjcyMSwiZXhwIjoxNzE1MzkzMTIxfQ.rq2450XavBQD_dmMJ-VZFl-izAimySXd8aGwmVsWszE',
    'ARK_ID': 'JS48539a3286cc77e856a810f11b16dec34853',
    'FZ_STROAGE.ofpay.com': 'eyJBUktTVVBFUiI6eyJncHNfY2l0eSI6IiIsInByb2plY3RfdHlwZSI6IueIsei0rTguOOa0u%2BWKqCJ9LCJTRUVTSU9OSUQiOiJmYjY4ZTFmOTU0ZTBmMDA0IiwiU0VFU0lPTkRBVEUiOjE3MTI1MzUxODAyNDIsIkFOU0FQUElEIjoiZXNoZW5naHVvdGVzdCIsIkFOUyRERUJVRyI6MiwiQU5TVVBMT0FEVVJMIjoiaHR0cHM6Ly9lbGlmZS11cC5hbmFseXN5c2RhdGEuY29tLyIsIkZSSVNUREFZIjoiMjAyNDAzMjUiLCJGUklTVElNRSI6ZmFsc2UsIkFSS19MT0dJTklEIjoidE44YkVBWnRmZ0hVcUdQUHVYZjlTRCs4TEZRaVdyWUwiLCJBUktfSUQiOiJKUzQ4NTM5YTMyODZjYzc3ZTg1NmE4MTBmMTFiMTZkZWMzNDg1MyIsIkFSS0ZSSVNUUFJPRklMRSI6IjIwMjQtMDMtMjUgMDk6MTU6MzEuOTYyIn0%3D',
}

headers = {
    'Host': 'market-web.ofpay.com',
    'UUID': '1715306745046EVEQ1S5F',
    'Accept': 'application/json, text/plain, */*',
    'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0TjhiRUFadGZnSFVxR1BQdVhmOVNEKzhMRlFpV3JZTCIsImFjY291bnQiOiJ0TjhiRUFadGZnSFVxR1BQdVhmOVNEKzhMRlFpV3JZTCIsInVzZXJJZCI6IjExNTU5NTUwOSIsIm1JZCI6IjAwMDAwMDExMDYiLCJwaG9uZU5vIjoiMTU5NTEwMDMwNzgiLCJzY29wZVByb21vdGVJZCI6IlAxMTk3OTU2MzY5ODA0MTY1MTIwIiwic2NvcGVUb2tlbiI6IjY3OGU1ODEyOTA2YjQzOWVlY2FhMzJlN2YzMjNkNWFlIiwiZW50cnlUeXBlIjoiaWNiY0VsaWZlSWdvUnVpeGluZyIsImVudHJ5UGxhdGZvcm0iOiJINSIsImN1c3RvbWVySW5mbyI6IntcImVudHJ5VHlwZVwiOlwiaWNiY0VsaWZlSWdvUnVpeGluZ1wiLFwiY2l0eV9uYW1lXCI6XCLljZfkuqzluIJcIixcImRldmljZV9pZFwiOlwiNDhCRUQ5QjItMDBGNy00RTY5LUE4OTctNUZCQjM4N0YzQTREXCIsXCJwaG9uZVwiOlwiMTU5NTEwMDMwNzhcIixcImN1cnJlbnRUaW1lTWlsbGlzXCI6XCIxNzE1MzA2NzIwNTEwXCIsXCJlbnRyeVBsYXRmb3JtXCI6XCJINVwiLFwiY2l0eV9jb2RlXCI6XCIzMjAxMDBcIixcImNpc25vXCI6XCJKeXZxK0dxTEtrOVY4Z0tnZ3RISlFBPT1cIixcImlzTmV3VXNlclwiOlwiMFwiLFwic2NvcGVQcm9tb3RlSWRcIjpcIlAxMTk3OTU2MzY5ODA0MTY1MTIwXCIsXCJjdXN0X2lkXCI6XCJ0TjhiRUFadGZnSFVxR1BQdVhmOVNEKzhMRlFpV3JZTFwifSIsImlhdCI6MTcxNTMwNjcyMSwiZXhwIjoxNzE1MzkzMTIxfQ.rq2450XavBQD_dmMJ-VZFl-izAimySXd8aGwmVsWszE',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Sec-Fetch-Mode': 'cors',
    'Content-Type': 'application/json',
    'Origin': 'https://market-web.ofpay.com',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 F-OFST  elife_moblie_ios  fullversion:6.0.6  BSComponentVersion:5.4 WorkStationChannel:0 isBreak:0  ICBCiPhoneBSNew 6.0.6 iphone os wkwebview:true',
    'Referer': 'https://market-web.ofpay.com/h5/event/P1197956369804165120/standard/icbcElifeIgoRuixing/entry?promoteId=P1197956369804165120&method=index',
    'Sec-Fetch-Dest': 'empty',
    # 'Cookie': 'br-session-js-sdk=9ea3a9b5-5620-4a13-b842-bbf276a94375|1715306721028|1715306741526|24; OF_WEB_SESSION=; unionToken_P1197956369804165120=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0TjhiRUFadGZnSFVxR1BQdVhmOVNEKzhMRlFpV3JZTCIsImFjY291bnQiOiJ0TjhiRUFadGZnSFVxR1BQdVhmOVNEKzhMRlFpV3JZTCIsInVzZXJJZCI6IjExNTU5NTUwOSIsIm1JZCI6IjAwMDAwMDExMDYiLCJwaG9uZU5vIjoiMTU5NTEwMDMwNzgiLCJzY29wZVByb21vdGVJZCI6IlAxMTk3OTU2MzY5ODA0MTY1MTIwIiwic2NvcGVUb2tlbiI6IjY3OGU1ODEyOTA2YjQzOWVlY2FhMzJlN2YzMjNkNWFlIiwiZW50cnlUeXBlIjoiaWNiY0VsaWZlSWdvUnVpeGluZyIsImVudHJ5UGxhdGZvcm0iOiJINSIsImN1c3RvbWVySW5mbyI6IntcImVudHJ5VHlwZVwiOlwiaWNiY0VsaWZlSWdvUnVpeGluZ1wiLFwiY2l0eV9uYW1lXCI6XCLljZfkuqzluIJcIixcImRldmljZV9pZFwiOlwiNDhCRUQ5QjItMDBGNy00RTY5LUE4OTctNUZCQjM4N0YzQTREXCIsXCJwaG9uZVwiOlwiMTU5NTEwMDMwNzhcIixcImN1cnJlbnRUaW1lTWlsbGlzXCI6XCIxNzE1MzA2NzIwNTEwXCIsXCJlbnRyeVBsYXRmb3JtXCI6XCJINVwiLFwiY2l0eV9jb2RlXCI6XCIzMjAxMDBcIixcImNpc25vXCI6XCJKeXZxK0dxTEtrOVY4Z0tnZ3RISlFBPT1cIixcImlzTmV3VXNlclwiOlwiMFwiLFwic2NvcGVQcm9tb3RlSWRcIjpcIlAxMTk3OTU2MzY5ODA0MTY1MTIwXCIsXCJjdXN0X2lkXCI6XCJ0TjhiRUFadGZnSFVxR1BQdVhmOVNEKzhMRlFpV3JZTFwifSIsImlhdCI6MTcxNTMwNjcyMSwiZXhwIjoxNzE1MzkzMTIxfQ.rq2450XavBQD_dmMJ-VZFl-izAimySXd8aGwmVsWszE; ARK_ID=JS48539a3286cc77e856a810f11b16dec34853; FZ_STROAGE.ofpay.com=eyJBUktTVVBFUiI6eyJncHNfY2l0eSI6IiIsInByb2plY3RfdHlwZSI6IueIsei0rTguOOa0u%2BWKqCJ9LCJTRUVTSU9OSUQiOiJmYjY4ZTFmOTU0ZTBmMDA0IiwiU0VFU0lPTkRBVEUiOjE3MTI1MzUxODAyNDIsIkFOU0FQUElEIjoiZXNoZW5naHVvdGVzdCIsIkFOUyRERUJVRyI6MiwiQU5TVVBMT0FEVVJMIjoiaHR0cHM6Ly9lbGlmZS11cC5hbmFseXN5c2RhdGEuY29tLyIsIkZSSVNUREFZIjoiMjAyNDAzMjUiLCJGUklTVElNRSI6ZmFsc2UsIkFSS19MT0dJTklEIjoidE44YkVBWnRmZ0hVcUdQUHVYZjlTRCs4TEZRaVdyWUwiLCJBUktfSUQiOiJKUzQ4NTM5YTMyODZjYzc3ZTg1NmE4MTBmMTFiMTZkZWMzNDg1MyIsIkFSS0ZSSVNUUFJPRklMRSI6IjIwMjQtMDMtMjUgMDk6MTU6MzEuOTYyIn0%3D',
}

params = {
    'awardId': 'W1197960242882019330',
    'eventVisitorId': 'RE2_ee2d0f2dd754cc7ca503bead41bf2eba1715306167140714JDHO9',
}

json_data = {
    'awardId': 'W1197960242882019330',
    'eventVisitorId': 'RE2_ee2d0f2dd754cc7ca503bead41bf2eba1715306167140714JDHO9',
}


def send_request():
    try:
        res = requests.post(url='https://market-web.ofpay.com/h5/event/api/token/P1197956369804165120/act/draw',
                            headers=headers, cookies=cookies, params=params, json=json_data, timeout=2)
        print(res.text)
        return res
    except Timeout:
        print("请求超时，但程序没有崩溃！")


target_time = datetime.datetime(2024, 3, 18, 9, 30, 0)
time_diff = (target_time - datetime.datetime.now()).total_seconds()
if time_diff > 0:
    time.sleep(time_diff)

result = True


def getTicket(detailId):
    headers2 = {
        'Host': 'market-web.ofpay.com',
        'UUID': '171530646394344JGIOBC',
        'Accept': 'application/json, text/plain, */*',
        'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0TjhiRUFadGZnSFVxR1BQdVhmOVNEKzhMRlFpV3JZTCIsImFjY291bnQiOiJ0TjhiRUFadGZnSFVxR1BQdVhmOVNEKzhMRlFpV3JZTCIsInVzZXJJZCI6IjExNTU5NTUwOSIsIm1JZCI6IjAwMDAwMDExMDYiLCJwaG9uZU5vIjoiMTU5NTEwMDMwNzgiLCJzY29wZVByb21vdGVJZCI6IlAxMTk3OTU2MzY5ODA0MTY1MTIwIiwic2NvcGVUb2tlbiI6IjY3OGU1ODEyOTA2YjQzOWVlY2FhMzJlN2YzMjNkNWFlIiwiZW50cnlUeXBlIjoiaWNiY0VsaWZlSWdvUnVpeGluZyIsImVudHJ5UGxhdGZvcm0iOiJINSIsImN1c3RvbWVySW5mbyI6IntcImVudHJ5VHlwZVwiOlwiaWNiY0VsaWZlSWdvUnVpeGluZ1wiLFwiY2l0eV9uYW1lXCI6XCLljZfkuqzluIJcIixcImRldmljZV9pZFwiOlwiNDhCRUQ5QjItMDBGNy00RTY5LUE4OTctNUZCQjM4N0YzQTREXCIsXCJwaG9uZVwiOlwiMTU5NTEwMDMwNzhcIixcImN1cnJlbnRUaW1lTWlsbGlzXCI6XCIxNzE1MzA2MzM1MTI3XCIsXCJlbnRyeVBsYXRmb3JtXCI6XCJINVwiLFwiY2l0eV9jb2RlXCI6XCIzMjAxMDBcIixcImNpc25vXCI6XCJKeXZxK0dxTEtrOVY4Z0tnZ3RISlFBPT1cIixcImlzTmV3VXNlclwiOlwiMFwiLFwic2NvcGVQcm9tb3RlSWRcIjpcIlAxMTk3OTU2MzY5ODA0MTY1MTIwXCIsXCJjdXN0X2lkXCI6XCJ0TjhiRUFadGZnSFVxR1BQdVhmOVNEKzhMRlFpV3JZTFwifSIsImlhdCI6MTcxNTMwNjMzNSwiZXhwIjoxNzE1MzkyNzM1fQ.vNNfaNKgcJ5Avxm5-rNQm1NsZbCATy-fZj3z4WxugdI',
        'Sec-Fetch-Site': 'same-origin',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Sec-Fetch-Mode': 'cors',
        'Content-Type': 'application/json',
        'Origin': 'https://market-web.ofpay.com',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 F-OFST  elife_moblie_ios  fullversion:6.0.6  BSComponentVersion:5.4 WorkStationChannel:0 isBreak:0  ICBCiPhoneBSNew 6.0.6 iphone os wkwebview:true',
        'Referer': 'https://market-web.ofpay.com/h5/event/P1197956369804165120/standard/icbcElifeIgoRuixing/entry?promoteId=P1197956369804165120&method=index',
        'Sec-Fetch-Dest': 'empty',
        # 'Cookie': 'OF_WEB_SESSION=; unionToken_P1197956369804165120=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0TjhiRUFadGZnSFVxR1BQdVhmOVNEKzhMRlFpV3JZTCIsImFjY291bnQiOiJ0TjhiRUFadGZnSFVxR1BQdVhmOVNEKzhMRlFpV3JZTCIsInVzZXJJZCI6IjExNTU5NTUwOSIsIm1JZCI6IjAwMDAwMDExMDYiLCJwaG9uZU5vIjoiMTU5NTEwMDMwNzgiLCJzY29wZVByb21vdGVJZCI6IlAxMTk3OTU2MzY5ODA0MTY1MTIwIiwic2NvcGVUb2tlbiI6IjY3OGU1ODEyOTA2YjQzOWVlY2FhMzJlN2YzMjNkNWFlIiwiZW50cnlUeXBlIjoiaWNiY0VsaWZlSWdvUnVpeGluZyIsImVudHJ5UGxhdGZvcm0iOiJINSIsImN1c3RvbWVySW5mbyI6IntcImVudHJ5VHlwZVwiOlwiaWNiY0VsaWZlSWdvUnVpeGluZ1wiLFwiY2l0eV9uYW1lXCI6XCLljZfkuqzluIJcIixcImRldmljZV9pZFwiOlwiNDhCRUQ5QjItMDBGNy00RTY5LUE4OTctNUZCQjM4N0YzQTREXCIsXCJwaG9uZVwiOlwiMTU5NTEwMDMwNzhcIixcImN1cnJlbnRUaW1lTWlsbGlzXCI6XCIxNzE1MzA2MzM1MTI3XCIsXCJlbnRyeVBsYXRmb3JtXCI6XCJINVwiLFwiY2l0eV9jb2RlXCI6XCIzMjAxMDBcIixcImNpc25vXCI6XCJKeXZxK0dxTEtrOVY4Z0tnZ3RISlFBPT1cIixcImlzTmV3VXNlclwiOlwiMFwiLFwic2NvcGVQcm9tb3RlSWRcIjpcIlAxMTk3OTU2MzY5ODA0MTY1MTIwXCIsXCJjdXN0X2lkXCI6XCJ0TjhiRUFadGZnSFVxR1BQdVhmOVNEKzhMRlFpV3JZTFwifSIsImlhdCI6MTcxNTMwNjMzNSwiZXhwIjoxNzE1MzkyNzM1fQ.vNNfaNKgcJ5Avxm5-rNQm1NsZbCATy-fZj3z4WxugdI; br-session-js-sdk=52511dc3-7e6e-4cc4-968a-6b77825ff7c1|1715309899590|1715310026467|78; ARK_ID=JS48539a3286cc77e856a810f11b16dec34853; FZ_STROAGE.ofpay.com=eyJBUktTVVBFUiI6eyJncHNfY2l0eSI6IiIsInByb2plY3RfdHlwZSI6IueIsei0rTguOOa0u%2BWKqCJ9LCJTRUVTSU9OSUQiOiJmYjY4ZTFmOTU0ZTBmMDA0IiwiU0VFU0lPTkRBVEUiOjE3MTI1MzUxODAyNDIsIkFOU0FQUElEIjoiZXNoZW5naHVvdGVzdCIsIkFOUyRERUJVRyI6MiwiQU5TVVBMT0FEVVJMIjoiaHR0cHM6Ly9lbGlmZS11cC5hbmFseXN5c2RhdGEuY29tLyIsIkZSSVNUREFZIjoiMjAyNDAzMjUiLCJGUklTVElNRSI6ZmFsc2UsIkFSS19MT0dJTklEIjoidE44YkVBWnRmZ0hVcUdQUHVYZjlTRCs4TEZRaVdyWUwiLCJBUktfSUQiOiJKUzQ4NTM5YTMyODZjYzc3ZTg1NmE4MTBmMTFiMTZkZWMzNDg1MyIsIkFSS0ZSSVNUUFJPRklMRSI6IjIwMjQtMDMtMjUgMDk6MTU6MzEuOTYyIn0%3D',
    }

    jsonData = {
        'detailId': detailId,
        'account': '15951003078',
        'eventVisitorId': 'RE2_ee2d0f2dd754cc7ca503bead41bf2eba1715306167140714JDHO9',
    }

    print('jsonData', jsonData)

    try:
        res = requests.post(url='https://market-web.ofpay.com/h5/event/api/token/P1197956369804165120/act/recharge',
                            headers=headers2, cookies=cookies, params=jsonData, json=jsonData, timeout=2)
        print(res.text)
        return res
    except Timeout:
        print("请求超时，但程序没有崩溃！")


while result:
    response = send_request()
    if response.status_code != 200:
        print('请求失败')
        continue
    # if response.text.find('该奖品被领光啦') != -1:
    #     print('已经抢完')
    #     exit()
    try:
        data = response.json()
    except:
        print("json解析出错")
        continue
    detailId = data['data']['drawPrize']['awardId']
    print(detailId)
    if detailId == None:
        print("没有抢到~")
        time.sleep(10)
    else:
        getTicket(detailId)
        time.sleep(10)




