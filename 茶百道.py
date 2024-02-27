import time
import requests
from datetime import datetime
import asyncio
from asyncio.futures import concurrent
import aiohttp

CK_LIST = [
    ('大号',
     '1708928493|JLqPCCh3qtqMUQa9.rZA4rfk+kLB+FepihYI0UJqgmaI6P64qETcq8TvG7/3aaV1SvvhK8f1SuQI91OcLMcb2zNu3JAZM4HapPUGTVQ==.9e52948ab6f5e127'),
]

headers = {
    'Host': 'chabaidao-gateway2.shuxinyc.com',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'versionName': '3.3.090',
    'Content-Type': 'application/json',
    'versionCode': '33090',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E217 MicroMessenger/6.8.0(0x16080000) NetType/WIFI Language/en Branch/Br_trunk MiniProgramEnv/Mac',
    'Referer': 'https://servicewechat.com/wx2804355dbf8d15c3/629/page-frame.html',
}

json_data = {
    'groupId': '317964',
    'memberSystemId': '21',
    'id': '5706',
    'activetype': 23,
    'unionId': 'ofD9L5h6ZXUikYFiMckY4EPQIclw',
    'shopId': -1,
    'cardId': '7116075994150115852',
    'mobile': '15951003078',
    'memberName': 'hash(闭关中)',
}

startTime = "2024-02-08 11:17:0"  # 抢购时间填进去几点就是几点跑
url = "https://chabaidao-gateway2.shuxinyc.com/marketing/minip/activity/joinActivity"


async def seek():
    start_time = time.mktime(time.strptime(
        startTime, '%Y-%m-%d %H:%M:%S')) * 1000
    now = int(round(time.time() * 1000))
    del_time = (start_time - now) / 1000
    print(f'距离开始还有{del_time}秒')
    await asyncio.sleep(del_time)
    await qiang()


async def qiang():
    print("开始抢卷")
    tasks = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        loop = asyncio.get_event_loop()
        for ck in CK_LIST:
            task1 = loop.create_task(bwcj(ck))
            tasks.extend([task1])
    # 等待所有任务完成
    await asyncio.gather(*tasks, return_exceptions=True)


async def bwcj(ck):
    async with aiohttp.ClientSession() as session:
        running = True
        while running:
            try:
                headers['CSESSION'] = ck[1]
                json_data['token'] = ck[1]
                async with session.post(url=url, headers=headers, json=json_data) as response:
                    result = await response.text()
                    now = datetime.now()
                    time_str = now.strftime("%H:%M:%S:%f")[:-3]
                    print(f'{time_str}:[{ck[0]}]:{result}')
                    if result.find('已达上限啦') != -1:
                        print(f'{ck[0]}领取成功！！！\n')
                        running = False
                    elif result.find('礼品已经送完') != -1:
                        print('已经领完了\n')
                        running = False
                    else:
                        print(f'{ck[0]}领取失败, 重新领取\n')
                        await asyncio.sleep(0.5)
            except Exception as e:
                print(f'{time_str}:[{ck[0]}]:{str(e)}')


def send_request(token):
    headers['Qm-User-Token'] = token
    res = requests.post('https://qmwebapi.qmai.cn/web/cmk-center/receive/takePartInReceive', headers=headers,
                        json=json_data)
    print(res.text)
    return res


if __name__ == '__main__':
    asyncio.run(seek())
