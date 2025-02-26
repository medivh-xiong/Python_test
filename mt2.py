from concurrent.futures import ThreadPoolExecutor
import aiohttp
import asyncio
import json
import time
import datetime
from bs4 import BeautifulSoup
from asyncio.futures import concurrent
import requests

CK_LIST = [
    ('2',
     'AgH0Ir5r-DShkh8gRV0VUX_0p8zp0LDIx4sJKQwJZ8kYGzsGUcu_aOA_2PmeR9ZN_EpSN0WZckjk9wAAAADWHQAA_hHXLcLldovdCnSBMXFu0isti0fH1KkfyR9ESU3ixV6xA3h1Ui-2E-MCaJSNnrUm'),
]

couponReferId = '4F2DAF7D9A3A496F8A4E0E8D8CDD7EBE'
kaishi = "1:18:59"

gdPageId = "493088"
url = f"https://promotion.waimai.meituan.com/lottery/limitcouponcomponent/fetchcoupon?couponReferId={couponReferId}&gdPageId={gdPageId}"


async def qiang_shenquan(ck):
    async with aiohttp.ClientSession() as session:
        for i in range(50):
            try:
                headers = {
                    'mtgsig': '{"a1":"1.0","a2":1684381815795,"a3":"y9x3yw89032v5zy809zx500854wwzu9w8117xv8339y979581w68xxu6","a4":"0229b3be92f9b03dbeb329023db0f9924d60d32e70d02abc","a5":"Doyac/b9dZhzgLc+rc9/w+8rVaCoD9RpcxZLBWEND+5qGpCliIpO63wfSq7DBSPUizlhVAyVIMLli0Z+K7Df2j1QYvP=","a6":"h1.2mThBxa1tn0U/ouY7Dc9Ohtm4cTPsL70rjbOWEhzjH0CMLEUSJu/aD7uc6UL2kz3MjrW6VEPJQrzxbbLmztW7kwO2VXIcgIwt4PZ2q4J0HTJGS9T+zdMcHCLaW8xPXBLoaOyg0DI/V7B73aqQ9g7+q0aPcbo1OPxZAANc0H8nS7AYEV2KwzJXLYMAL5kvNdgZoRuLb1l/KE+Z21UAtdCh6r0db2bowT/mMWlx67zROTkU2XEb2oPvWBwg4/o/hAxDd3MlVS7oqXcXjMev6vIPVFEhfktEbvTE7JG+ghB7gwi9qh8KvCU5wD2xVSUJsjtD5CFaVRQ5spc2Hs0v4rhjtFZo/0IPjW0PNySBDXRzk5zKwR5DGl7RzWzYv8SM6Uav","a7":"","x0":4,"d1":"5f352439e3884b5198a56ad94870402c"}',
                    'Connection': 'keep-alive',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Content-Type': 'application/json',
                    'Origin': 'https://market.waimai.meituan.com',
                    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.32(0x18002038) NetType/4G Language/zh_CN',
                    'Host': 'promotion.waimai.meituan.com',
                    'Referer': 'https://market.waimai.meituan.com/',
                    'Accept-Language': 'zh-cn',
                    'Accept': 'application/json, text/plain, */*'
                }
                params = {"token": ck[1]
                          }
                payload = json.dumps({
                    "cType": "wx_wallet",
                    "fpPlatform": 13,
                    "wxOpenId": "",
                    "appVersion": "",
                    "mtFingerprint": "H5dfp_1.8.2_tttt_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"
                })

                async with session.post(url=url, headers=headers, data=payload, params=params) as response:
                    result = await response.text()
                    result_json = json.loads(result)
                    msg = result_json.get("msg", result)
                    now = datetime.datetime.now()
                    time_str = now.strftime("%H:%M:%S:%f")[:-3]
                    print(f'{ck[0]} - {time_str}: {msg}')
                    if "来晚了，券抢完了~" in msg:
                        print('来晚了，卷抢完了')
                        return  # 如果已经领取到了代金券，就退出循环
            except json.decoder.JSONDecodeError:
                msg = BeautifulSoup(result, 'html.parser').find(
                    'title').get_text()
                print(f"{ck[0]} - {time_str}：{msg}")
                continue  # 如果发生异常，继续尝试下一轮


async def qiang_shenquan_wrapper():
    tasks = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        loop = asyncio.get_event_loop()
        for ck in CK_LIST:
            # 将每个 CK 对象分别放入两个不同的线程池中并行执行两个协程
            task1 = loop.create_task(qiang_shenquan(ck))
            task2 = loop.create_task(qiang_shenquan(ck))
            tasks.extend([task1, task2])
    # 等待所有任务完成
    await asyncio.gather(*tasks, return_exceptions=True)


async def main(d):
    if d == 14:
        time_str = f"{time.strftime('%Y-%m-%d', time.localtime(time.time()))} {kaishi}"
    start_time = time.mktime(time.strptime(
        time_str, '%Y-%m-%d %H:%M:%S')) * 1000 + 800
    now = int(round(time.time() * 1000))
    del_time = (start_time - now) / 1000
    print(f'距离开始还有{del_time}秒')
    await asyncio.sleep(del_time)
    await qiang_shenquan_wrapper()


def sx():
    for ck in CK_LIST:
        session = requests.Session()
        url = "https://promotion.waimai.meituan.com/lottery/limitcouponcomponent/info?"
        headers = {
            'Host': 'promotion.waimai.meituan.com',
            'Origin': 'https://market.waimai.meituan.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.32(0x18002038) NetType/4G Language/zh_CN',
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            'Referer': 'https://market.waimai.meituan.com/'
        }
        params = {"token": ck[1], 'couponReferIds': {couponReferId}}

        response = session.get(url=url, headers=headers, params=params)

        data = response.json()
        if data['code'] == 0:
            print(
                f"{ck[0]}:刷新成功:{data['data']['couponInfo'][couponReferId]['priceLimit']}-{data['data']['couponInfo'][couponReferId]['couponValue']}")
        else:
            print(data['errorMsg'])


if __name__ == '__main__':
    sx()
    asyncio.run(main(14))
