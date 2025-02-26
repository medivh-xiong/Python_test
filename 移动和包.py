from concurrent.futures import ThreadPoolExecutor
import aiohttp
import asyncio
import json
import time
import datetime
from asyncio.futures import concurrent
import requests
from datetime import datetime, timedelta

startTime = "2024-09-25 15:00:0"  # 抢购时间填进去几点就是几点跑

json_data = {
    'prizeNo': 'JFMS20239004',
    'sign': 'B',
}

url = "https://ump.cmpay.com/activities/v1/members/integralTicketReceive"


cookies = {
    'sid': 'MCALOGIN-3b02baa4-3525-4048-a5ab-152531a83c94',
    'act_sid': 'act-80061143-60fb-4efd-9c91-644e721be64d',
}

headers = {
    'Host': 'ump.cmpay.com',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    # 'Cookie': 'sid=MCALOGIN-89444a9b-a260-4512-8939-6fda808d6ede; act_sid=act-41e47668-b5fe-406f-9813-33e9c68a249d',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Html5Plus/1.0 (Immersed/20) uni-app',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'X-Requested-With': 'XMLHttpRequest',
}

async def qiang_shenquan():
    async with aiohttp.ClientSession() as session:
        for i in range(500):
            try:
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
    tasks = [qiang_shenquan() for _ in range(2)]
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
