import time
import requests
from datetime import datetime
import asyncio
from asyncio.futures import concurrent
import aiohttp

CK_LIST = [
    ('大号-2',
     'pSYWfuYsuK8KScBxQ2nWBF2vyBY0r05gY4JveqMgJoIRK-drcEqcbPT0raFVy3I3'),
    ('华为-1',
     'B-rlPO00gfN1S-C9xCaXKeefkHqLI6GwR53geGaa-gNEUHxvoxyHeUpH7HkpiQbV'),
    ('小米10-2',
     'Zoh6di8MRCSxVDsABlju23fgI1e9cWga1jcx_Ymt12_SKfsZ6tnNpSrlv3p_BGxS'),
    ('k40-1',
     'C-qC-SGyQl4_3iCpTGb-cG3UlF3tbmlA1G1kw2YqPHOXJJ6MT5oI8iIGNaO8pZSr'),
    ('小米8-2',
     'bejpq94rgdpfitf982XbYXevrucbUidmdZ-ZL2VZYm4mZaPqVjUDTOVkeb6LruYC'),
]

headers = {
    'Host': 'qmwebapi.qmai.cn',
    'Accept': 'v=1.0',
    'content-type': 'application/json',
    'qm-trace-store-id': '49006',
    'Qm-From': 'wechat',
    'Qm-From-Type': 'catering',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.46(0x18002e2c) NetType/WIFI Language/zh_CN',
    'Referer': 'https://servicewechat.com/wxafec6f8422cb357b/143/page-frame.html',
}

json_data = {
    'activityId': '961633325138382848',
    'keyWords': '以茶会友会友为龙',
    'appid': 'wxafec6f8422cb357b',
}

startTime = "2024-02-08 11:17:0"  # 抢购时间填进去几点就是几点跑
url = "https://qmwebapi.qmai.cn/web/cmk-center/receive/takePartInReceive"


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
                headers['Qm-User-Token'] = ck[1]
                async with session.post(url=url, headers=headers, json=json_data) as response:
                    result = await response.text()
                    now = datetime.now()
                    time_str = now.strftime("%H:%M:%S:%f")[:-3]
                    print(f'{time_str}:[{ck[0]}]:{result}')
                    if result.find('已达上限啦') != -1:
                        print(f'{ck[0]}领取成功！！！\n')
                        running = False
                    elif result.find('已被领完') != -1:
                        print('已经领完了\n')
                        running = False
                    else:
                        print('领取失败, 重新领取\n')
                        await asyncio.sleep(2)
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
