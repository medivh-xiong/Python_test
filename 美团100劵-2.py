from concurrent.futures import ThreadPoolExecutor
import aiohttp
import asyncio
import json
import time
import datetime
from asyncio.futures import concurrent
import requests
from datetime import datetime, timedelta
import logging


CK_LIST = [
    ('ys1',
     'AgFnJNaRvxj8OZIk5XkUSbEJ922enAeypKxyxPej5AEtmwcpNIZVzuUkyQVGmG3cMcz3RTWtsrK_eAAAAADWHQAAp8WG3d2rrtdAd7V1_E3Mz0UyC7Wyh_5T1je9DBfaAumcUAYwuhpKEVloFPLpnBDb'),
    ('ys2',
     'AgFaJCYr5tLkvCTcpHdpOLWt4HAsOpaaY4wapS8RV_nY6tT3Z1YKM1dQevQZONTMkSmcWdmShJAJ6gAAAAC3HQAACD7cuip22PG_t8ffeiPYoYqQjj_yff2wSf30CfpqLQTePy0wrtEsp1izqJhyUzS_'),
    ('ys3',
     'AgGRJMuGR0V_E4SmBVfP7Qd2XHc2h-X8Dg232L7NkZF9ulj_FXXXyV37LwFXo5_Fv8isPrn8xxuYawAAAADWHQAAT-rWIEd5nS5HQxqOoYGGh6dxtU7xSdnr4-RL28lYJMpzuRo-Lo5HociIa06rF7Q1'),
]

startTime = "2024-02-04 0:0:0"  # 抢购时间填进去几点就是几点跑
couponReferId = ""

params = [
    ('yodaReady', 'h5'),
    ('csecplatform', '4'),
    ('csecversion', '2.4.0'),
    ('mtgsig',
     '{"a1":"1.1","a2":1706777696991,"a3":"2843ux0706vy5z16yz9x1705v995z33y81z5vyx69wy9795864v28400","a5":"WFyFoAbWRY3BWuAlcs91/OJF0g9fvySLwW==","a6":"hs1.4A7RoRP0dbIKmoIPl+WUiTII5DT4N5vbHgfwTGvYlf4FmXCuX9HozdPXx5cMgai36UHsT4gClDT/5IFifJg327jWXx5MgW3WMgmevHjRJ8Wg=","x0":4,"d1":"aacc609581f1ceb8d99ad3172b3dae3f"}'),
]

url = "https://cactivityapi-sc.waimai.meituan.com/api/coupon/outer/sendV3"

async def qiang_shenquan(ck):
    async with aiohttp.ClientSession() as session:
        for i in range(50):
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:122.0) Gecko/20100101 Firefox/122.0',
                    'Accept': 'application/json, text/plain, */*',
                    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                    'Referer': 'https://market.waimai.meituan.com/',
                    'Content-Type': 'application/json;charset=utf-8',
                    'Origin': 'https://market.waimai.meituan.com',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-site',
                }
                payload = {
                    'couponLocation': 'item5_2',
                    'channelUrlKey': '1516915820',
                    'type': 2,
                    'couponShowId': '3606805002421EB1C6BA6E9B42FF4E3DTOWG2mbUxNxPnbGVaEkKDQ%3D%3D',
                    'couponType': 2,
                    'discountType': 1,
                    'couponAmount': 100,
                    'orderAmountLimit': 999,
                    'latitude': 31.970089,
                    'longitude': 118.764418,
                    'gdVersion': '2',
                    'pageId': 546921,
                    'gdId': 492452,
                    'uuid': '09471AFFB3E4A37A41A3300DBD94FDB4AE933EC10E5077A1950C26B5E49848FD',
                    'clientType': '',
                    'source': 0,
                    'fp_platform': 1,
                    'app_version': '',
                    'wxOpenId': '',
                    'mtFingerprint': 'H5dfp_2.4.0_tttt_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',
                }

                cookies = {
                    'token': ck[1]
                }

                async with session.post(url=url, params=params, headers=headers, json=payload,
                                        cookies=cookies) as response:
                    result = await response.text()
                    result_json = json.loads(result)
                    msg = result_json.get("data", result).get('receiveCode')
                    print("-----------------")
                    print(result_json)
                    print("-----------------")
                    now = datetime.now()
                    time_str = now.strftime("%H:%M:%S:%f")[:-3]
                    print(f'{time_str}:[{ck[0]}]:{msg}')
                    if msg == 2 or msg == 1:
                        print(f'{ck[0]}领取成功！！！')
                        print('-------结束')
                        break  # 如果已经领取到了代金券，就退出循环
                    elif msg == 3:
                        print('券已经抢光')

            except Exception as e:
                # print(f'{time_str}:[{ck[0]}]:{str(e)}')
                continue  # 如果发生异常，继续尝试下一轮


async def qiang_shenquan_wrapper():
    print("开始抢卷")
    tasks = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        loop = asyncio.get_event_loop()
        for ck in CK_LIST:
            # 将每个 CK 对象分别放入两个不同的线程池中并行执行两个协程
            task1 = loop.create_task(qiang_shenquan(ck))
            # task2 = loop.create_task(qiang_shenquan(ck))
            tasks.extend([task1])
    # 等待所有任务完成
    await asyncio.gather(*tasks, return_exceptions=True)


def sx():
    for ck in CK_LIST:
        try:
            session = requests.Session()
            url = "https://promotion.waimai.meituan.com/lottery/limitcouponcomponent/info?"
            headers = {
                'Host': 'promotion.waimai.meituan.com',
                'Origin': 'https://market.waimai.meituan.com',
                'Connection': 'keep-alive',
                'Accept': 'application/json, text/plain, */*',
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.32(0x18002038) NetType/4G Language/zh_CN',
                'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
                'Referer': 'https://market.waimai.meituan.com/',
                'Cookie': ck[1],
            }
            params = {'couponReferIds': {couponReferId}}

            response = session.get(url=url, headers=headers, params=params)
            data = response.json()
            if data['code'] == 0:
                print(
                    f"{ck[0]}:刷新成功:{data['data']['couponInfo'][couponReferId]['priceLimit']}-{data['data']['couponInfo'][couponReferId]['couponValue']}")
            else:
                print(data['errorMsg'])
        except Exception as e:
            print(f"{ck[0]} - 发生异常：{str(e)}")
        continue  # 如果发生异常，继续尝试下一轮


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
