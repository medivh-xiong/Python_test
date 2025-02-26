from concurrent.futures import ThreadPoolExecutor
import aiohttp
import asyncio
import json
import time
import datetime
from asyncio.futures import concurrent
import requests
from datetime import datetime, timedelta

startTime = "2024-12-31 11:00:0"  # 抢购时间填进去几点就是几点跑

json_data = {
    'activityNo': 'oBGT9eX2x74yS8V7kNWTwtUFwakGkeSeL1bGO_SC9QQ',
    'mobile': '17895003078',
    'comeFrom': '4',
    'openid': None,
    'blackBox': 'lWPHD1735613630h1YpKUH6L16',
    'shopMdCode': None,
}

url = "https://ma.cotticoffee.com/cotti-capi/universal/coupon/receiveLaunchRewardH5"

cookies = {
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2221580456410%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk0MWFhMWRmYmUyNTEtMGY1ODI0ODU3MTZkMzctZDQ3NzA1Yy0yNTAxMjUtMTk0MWFhMWRmYmY5MzEifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D',
    'HWWAFSESID': '9ddf810f919e03bffb4',
    'HWWAFSESTIME': '1735613603999',
    'sajssdk_2015_cross_new_user': '1',
}

headers = {
    'Host': 'ma.cotticoffee.com',
    # 'Cookie': 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2221580456410%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk0MWFhMWRmYmUyNTEtMGY1ODI0ODU3MTZkMzctZDQ3NzA1Yy0yNTAxMjUtMTk0MWFhMWRmYmY5MzEifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D; HWWAFSESID=9ddf810f919e03bffb4; HWWAFSESTIME=1735613603999; sajssdk_2015_cross_new_user=1',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.54(0x18003638) NetType/WIFI Language/zh_CN miniProgram/wxe766d738ad655e8c',
    'Referer': 'https://m.cotticoffee.com/',
    'split_timestamp': '0',
    'Origin': 'https://m.cotticoffee.com',
    'Sec-Fetch-Dest': 'empty',
    'version': 'v1',
    'Sec-Fetch-Site': 'same-site',
    'sign': 'A0B19D088F6FD0A1B23D965650B4B539',
    'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ7XCJpc05ld01lbWJlclwiOnRydWUsXCJtZW1iZXJJZFwiOjIxNTgwNDU2NDEwLFwibWVtYmVyTm9cIjpcIjIxNTgwNDU2NDEwXCIsXCJtZW1iZXJUeXBlXCI6MCxcIm1vYmlsZVwiOlwiMTc4OTUwMDMwNzhcIixcIm9wZW5JZFwiOlwib1E5WlY1T1N6aVgwS2w5c3F6T0N0b0VzMUpJTVwiLFwidGVybWluYWxUeXBlXCI6XCI5MDFcIixcInVuaW9uSWRcIjpcIm8yU19MNTVUQnNzNm85dzJOUFhKNlZIWTFIeDBcIixcInZlcnNpb25cIjoxNzM1NjEzNjI4MjczfSIsImlzcyI6ImNvdHRpIiwiZXhwIjoxNzQwNzk3NjI4LCJpYXQiOjE3MzU2MTM2MjgsImp0aSI6IjRlY2QwYjc5N2JhNzQzNzdhNWExYWY5MDkwNmM0YjEyIn0.Ho-1o_YrnI8A2vjq9zHmXmpWxRNE31_BHF39IOvfaPY',
    'timestamp': str(int(time.time()) * 1000),
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'api-version': 'v1',
    'Accept': '*/*',
    'Content-Type': 'application/json',
    'brandMdCode': '20200000006',
    'appKey': '2YAhmad694MnzqmcPQ5X6TJ6EoSx6sYx',
    'Sec-Fetch-Mode': 'cors',
}

async def qiang_shenquan():
    async with aiohttp.ClientSession() as session:
        for i in range(500):
            try:
                print("开始" + str(i) + "次：\n")
                async with session.post(url=url, headers=headers, json=json_data,
                                        cookies=cookies) as response:
                    result = await response.text()
                    now = datetime.now()
                    time_str = now.strftime("%H:%M:%S:%f")[:-3]
                    print(f'{time_str}:[{result}')
            except Exception as e:
                continue  # 如果发生异常，继续尝试下一轮


async def qiang_shenquan_wrapper():
    print("开始抢卷")
    tasks = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        loop = asyncio.get_event_loop()
        task1 = loop.create_task(qiang_shenquan())
        tasks.extend([task1])
    # 等待所有任务完成
    await asyncio.gather(*tasks, return_exceptions=True)


async def main(d):
    if d == 14:
        time_str = startTime
    start_time = time.mktime(time.strptime(
        time_str, '%Y-%m-%d %H:%M:%S')) * 1000
    now = int(round(time.time() * 1000))
    del_time = (start_time - now) / 1000
    print(f'距离开始还有{del_time}秒')
    await asyncio.sleep(del_time)
    await qiang_shenquan_wrapper()


if __name__ == '__main__':
    asyncio.run(main(14))
