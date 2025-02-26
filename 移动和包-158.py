from concurrent.futures import ThreadPoolExecutor
import aiohttp
import asyncio
import json
import time
import datetime
from asyncio.futures import concurrent
import requests
from datetime import datetime, timedelta

startTime = "2025-02-26 15:00:0"  # 抢购时间填进去几点就是几点跑

json_data = {
    'prizeNo': 'JFMS20231221',
    'opDfp': 'bK8G4IiYx29l-j6jAHh8yUTyP4W_sybKs-Otg0iHsaLDuPI5csU-ugpVWLG6DnKXFV0lP5wZzea7lYzOT2QD0isIHJFiPxOLW2CMllsnebQAZmfeqmXMqQUBbHOSDeg9d7CMcHFANkADAEAQGBsP3a9YC9j8e4yf',
    'sign': 'B',
}

url = "https://ump.cmpay.com/activities/v1/members/integralTicketReceive"

cookies = {
    'sid': 'MCALOGIN-e6dde90b-4168-46d2-89b3-ed736cb19d8c',
    'act_sid': 'act-dacc6c76-ea38-4a3e-8ecb-7d69b1a03f61',
}

headers = {
    'Host': 'ump.cmpay.com',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    # 'Cookie': 'sid=MCALOGIN-533424f2-6040-46df-b2c0-c32044dc6655; act_sid=act-dc0bf311-2bc6-4164-af2e-6e234190743e',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Html5Plus/1.0 (Immersed/20) uni-app',
    'X-Requested-With': 'XMLHttpRequest',
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
