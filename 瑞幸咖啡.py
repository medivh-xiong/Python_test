from concurrent.futures import ThreadPoolExecutor
import aiohttp
import asyncio
import json
import time
import datetime
from asyncio.futures import concurrent
import requests
from datetime import datetime, timedelta

startTime = "2024-11-11 12:00:0"  # 抢购时间填进去几点就是几点跑

json_data = {
    'cid': '230101',
    'q': 'HYeJKekUfZVYNXdcfbzcloWZB0coxwg1O_j2w7eZxw0wprvrIlyJUJrya8PpWlm_tFCHE3RrPXqpRGrZIPPSGpMacfwjDqvwK56nqKsFjKEZL4xBghR_o8fYZNzOB4dWxjgUXhb5t3JDiwT05xC5828H4N7E1ACN95MKPoUpxs8=',
    'dk': '1',
    'sign': '144239735066825660014588477052021135108',
}

url = "https://capi.lkcoffee.com/resource/core/v2/virtual/product/limited"

cookies = {
    'uid': 'd2c53ab8-73d1-4ec4-bb6b-4302185eef161731294759583',
}

headers = {
    'Host': 'capi.lkcoffee.com',
    # 'Cookie': 'uid=d2c53ab8-73d1-4ec4-bb6b-4302185eef161731294759583',
    'x-lk-akv': 'lk-wxmp-v5.1.72',
    'x-lk-sid': '601989',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/6.8.0(0x16080000) NetType/WIFI MiniProgramEnv/Mac MacWechat/WMPF MacWechat/3.8.7(0x13080712) XWEB/1191',
    'x-lk-csid': 'bfec78d3-0694-a1c9-856b-60376a854655',
    'content-type': 'application/x-www-form-urlencoded',
    'xweb_xhr': '1',
    'x-lk-mid': '263905160',
    'accept': '*/*',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://servicewechat.com/wx21c7506e98a2fe75/719/page-frame.html',
    'accept-language': 'zh-CN,zh;q=0.9',
}

async def qiang_shenquan():
    async with aiohttp.ClientSession() as session:
        for i in range(500):
            try:
                print("开始" + str(i) + "次：\n")
                async with session.post(url=url, headers=headers, data=json_data,
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
