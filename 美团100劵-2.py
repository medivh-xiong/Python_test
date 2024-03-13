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
    ('大号',
     'AgGoHpFlA_n8y9TqOxdr_4vpfdTC6nPfuk4qPH5VyFc7OgScKp1lbfs7Wz_j8wrcDYKZUCElPGKlDwAAAAB_HgAAWreOMRDO89XAN5wSRVAPVGAQG5E6dl8TlXaVgET2E_jtGpHN5LFiNd8wJ_F_Vh47'),
]

startTime = "2024-03-08 13:0:0"  # 抢购时间填进去几点就是几点跑
couponReferId = ""

params = [
    ('couponReferId', 'CD3E100EAAB54673A36BF507FA311429'),
    ('geoType', '2'),
    ('gdPageId', '549085'),
    ('pageId', '556519'),
    ('version', '1'),
    ('utmSource', 'AppStore'),
    ('utmCampaign', '1'),
    ('instanceId', '17095594923790.010483167848327035'),
    ('utmCampaign', '17095594923790.010483167848327035'),
    ('componentId', ''),
    ('ctype', ''),
    ('utmMedium', 'iphone'),
    ('gSource', ''),
    ('dpSource', ''),
    ('yodaReady', 'h5'),
    ('csecplatform', '4'),
    ('csecversion', '2.3.1'),
]

url = "https://promotion.waimai.meituan.com/lottery/limitcouponcomponent/fetchcoupon"


async def qiang_shenquan(ck):
    async with aiohttp.ClientSession() as session:
        for i in range(50):
            try:
                headers = {
                    'Host': 'promotion.waimai.meituan.com',
                    'Content-Type': 'application/json',
                    'Accept': 'application/json, text/plain, */*',
                    'Sec-Fetch-Site': 'same-site',
                    'dj-token': 'BUtNUwMAAABuBktNUwMaOQIAAAABO5rMWgAAACyQ2GvX3flmYoryInDPvI1DDK2AF3V0UiUO+OgBR8h7goamLPbE41wOQcM4YCIsjaOwh2+TNk5PA6kuaOH0P3lz4ChL1E17vO9tmcuAVPAstXZB+MKX81EzgHQAAABOj0aAcMzCpbw3bQAVnmJ91X8QvoOKTZWtR+GkMJadI4+11ND+YAw+92ZFJQOiOSDvUtMQbfekPQZxU1xv3ksHAqV7PwZAh+V/AMcg6Ppj',
                    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
                    'Sec-Fetch-Mode': 'cors',
                    'Origin': 'https://market.waimai.meituan.com',
                    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 TitansX/20.25.1 KNB/1.0 iOS/16.5.1 meituangroup/com.meituan.imeituan/12.18.402 meituangroup/12.18.402 App/10110/12.18.402 iPhone/iPhone8 WKWebView',
                    'Referer': 'https://market.waimai.meituan.com/',
                    'mtgsig': '{"a0":"3.0","a1":"6f50fb51-23ee-4173-ab33-6ee69ed0ef29","a3":24,"a4":1709787600,"a5":"kHTSBJPmiiZI5IE/J5se3tKxwVOPmVkACeruh5EdRn3cPpSV9lroHdk4rWMthSGCGqQnewHtBNaIMMjNbXL5y/spuYmKEm1D0tOqDs2JKMkU9aE+s9xnnrBqAQ+KKDoTiqmGWD/ZlNPUNbTVHiz2D50vlwW2Qeco6B1KeI+lnPa2xurrW1PiMhqt2jdoqaKhVI+QsQTmQEwJu16t+qPdUwgUXxjIFJ6M+UZhR/ZJsDeAQ8/4tjtLZ2wVl1dExMZ/4e/MbcM3C1Jr4Ty6eq+Z3INbEFMEs47od1uELtvzGkht9HugAHtQRSk3S1kiNE5IvhALVeCZafoi9qIA9Mx7wLogWLCrsmCpNBUwmGyzj149VHmG28nsAVow5AxoqZbHMM6dGQWoV98EvohcLOti0k23mA==","a6":0,"a7":"zSLG1xQ/F1+OxH+DOexwOMCarm1XMRhygTJ5FR8ONUPGLjgGOEaaq2+nVF7pVITvCcPft2A1NgsZvcl4mhX49xgxeDVpLfuMqwH9wHwGpjs=","a8":"39a2c331f8b489e9dd2f800cd1a1453d9200ff18cff2a81d244e77e5","a9":"2913f87dmuYzzgjCGueSANTuDHNTdzzMhrbFaALEgbRHRTT6pDRT4TEmcYohjk/qwSyhAr35tF/1KUXQ9OtuwEAMzcuVfMw/jouhGROSZsWtsEA+JZ3pw6Aesa4aUKois00fMThoE73Vg0AsBvN+OH2SUAzltKOGcfOKPmMEIzFnWAMVl5bUUy5oz7z3C4u2TBLO9SWByLMCxdg4c95Rl0m6kzNpHS3E0c9v3HcMlowWKDI3xsatvCwImQN7edhjj5CS/BPJ+Z5Mfneag4xIRa5GkbLHdGiqSPPCTQyA3ohxVhm7KZtfXBEYfwhpuyWcGEjBLghFyLMbpPzQxljz6BT+G9lwIxrsVO49mAlAFlneeswLalpMvveNL+/7z8vdLIhZi3LfbkCWQvxqVOIiVxZoXzxGUgZ9aH/uA1OlcVW6Xk+Guib8TUtD2UV3yCTRDSDfxoZDlwgrk0FUP2Ug/VYW1lVig3895nPNpKXy78ph4UGttx/ORxPZO8zFvwUSgjYrKXnVW/aWPfmtzwc17Q4ILr8Km5oKjZJNTbROvuDsV9XTsoEl/rWee0T1lY1sXt8y2xc/BalIiroFwGAFOAjiyljlgEB2oafzh4t5wVC8Y+vQKsxaBeox247wAHERvCIKRMKBA+O9upNWcFQ3NaVAlCuKxfjUJTpZ7SWdmHnOPE5AXZJi0WOqiIHBjdCWUps3/fCN0XEHQpJU4/ttijJ/qQ8OC5MO6h1YM1u39yKUyfkNcVvdmMJWGPjOdBThjFwSSv8B","a10":"5,186,1.1.8","x0":2,"a2":"8c8abc70faa46ec80fbb1eeb156e36ea"}',
                    'Sec-Fetch-Dest': 'empty',
                    # 'Cookie': 'isUuidUnion=true; iuuid=0000000000000A73DDC9201C9499BA2134A99A5C759CDA168460156076763327; network=wifi; _lx_utm=utm_campaign%3D1%26utm_term%3D12.18.402%26utm_source%3DAppStore%26utm_content%3D0000000000000A73DDC9201C9499BA2134A99A5C759CDA168460156076763327%26utm_medium%3Diphone; WEBDFPID=8v1z6z5673065347yv181798y169504981w4ww099yy979586w45u233-2022036519293-1706676519293MUIUQME868c0ee73ab28e1d0b03bc83148500061515; _utm_campaign=AgroupBgroupD100H0; _utm_content=0000000000000A73DDC9201C9499BA2134A99A5C759CDA168460156076763327; _utm_medium=iphone; _utm_source=AppStore; _utm_term=12.18.402; cityid=55; dpid=; token=AgFDLHvIf7vI-7q5Gb5QwshDSeBc54wqXvlmuajfZLfSCz-78wD-d0lYbp30nMYe2FKhcCWSWtSL4xEAAABgHgAAYJjikhPA3nduOULpRDv5CGeBVfhdtk8SvDWZ2OYQTqMNcvY7FcLNc7OGKTtKwfXXMVD2NAfImuiEdeX7MNQPlQ; uuid=0000000000000A73DDC9201C9499BA2134A99A5C759CDA168460156076763327; mt_c_token=AgFDLHvIf7vI-7q5Gb5QwshDSeBc54wqXvlmuajfZLfSCz-78wD-d0lYbp30nMYe2FKhcCWSWtSL4xEAAABgHgAAYJjikhPA3nduOULpRDv5CGeBVfhdtk8SvDWZ2OYQTqMNcvY7FcLNc7OGKTtKwfXXMVD2NAfImuiEdeX7MNQPlQ; ta.uuid=1752554450864390169; _lxsdk=0000000000000A73DDC9201C9499BA2134A99A5C759CDA168460156076763327; _lxsdk_cuid=18d5dd8eb65c8-0bef285aee3a56-6e7f2023-3d10d-18d5dd8eb66c8; _lxsdk_dpid=a73ddc9201c9499ba2134a99a5c759cda168460156076763327; _lxsdk_unoinid=a73ddc9201c9499ba2134a99a5c759cda168460156076763327',
                }
                payload = {
                    'cType': 'mtiphone',
                    'fpPlatform': 5,
                    'wxOpenId': '',
                    'appVersion': '12.18.402',
                    'mtFingerprint': 'i2HKpOmsirDPavelVfQBZOQmtrzeq+1nOcGupX4lqdbh0o51x/aLJnFZgOxGOjYq+VH4oUTz5JB4XgV1Jnbzj3Mg18tj5Q+xHXdLhW2PxmDs4Nyqgo9gcDTT+9stXI7pp/YRx+g1XK+r6xskb/dXxEex/ye3eSEEE0nE3rXMtMzNVQZZe8zJSEr18aPCpN9n/ROMLvI/ntH8fFaoDKBp8g79i64R/bSb4oeHx9X5AusaT7ynUlYspVrP1KCZKgDX7pe/9J7wj9i2okZ06Hzk1UuGQsNaWUnjEQ6eO5dwHeyYEhU1W2PSRjjbORNw0ZqCEEEegpr51ctpp7/XayRX5lRT4K2iTCr3Zh5LOtsN9Nwxbj8v9fGAkTbp9N22f4Q/eaoGVYyFXhC+jqo2BtsREJrzk+0wsZkNonkjYCyXGfMv5E8MwPf7QAM4YPNRurcDJ/CRKeOgBkbaRtRdq/5wbi5WD7McJf/VJPZEuwx7ZTVkP+Tew5FDD7U82M/cvRP3eeBy96bwSI3WJomfqo2w4uO7N8cKGJbAbZ+8JXVuS8BzP74qjMp9E5XBw5AJHQqY0oE6WXgpbhbQRE4jUrrcivxptPQWgDUmLUQ4VrgK/bbHBwgOMvDx+Iywo91fVGUqkx34LqR3K9xE0R9Bt8nrfYNv4zrPao5RdAJqvT5V9ZLGY3X2HFuZsnFtRaLPFuQPQ4OH9bJ38ECvjmKYBSgY/MrNNs0cJCoygwCLJfTKkUUr6k/rvhyRog1ye3gS+5i2f+HRwupGCMHzgbgF0OR6PI+nGDJ3EVFvKMlIBj/GPg5720vqxi8CC+0KNcwWbQPhXPWusT45OLOTIDcodyQy9gSCt79jj/tWbyB+pGNF8uXqCv2KoNUU33NyvcSltiroOpgC1qovKb+ArZD1Mccwcm4vh1uTFLCPJk1qy0SZLs4Q5FLQ+ZUXOAx9mfOcJCMkDRmJ84+GaijWjwkOY9/SGJTOdzSc1dh7rqD1FuR8OWGIqAZ7qix7My570Yi77PDoQBhiE3a7/yggaSMkib2AK7qEA4BdSskosNEhyPotGIriLLypO3Z98zBmfboOWPMDceIO5RaTBFJOP0iDki/Yf0oiP6o2MZBWt4MJAxvJZ00XkwFH78/tf6blaSj3MvA+tHUrovt3JF7n+Kj5AnBHmuGZDThn/L3nkgg7uoFaGpT9IXD2BGbEunLc9MprBWiO03HdcSDv2NehsqTLOLSUPrsor7xajdv78siCH5hlbhdboH3F41yPSnWSCXRYWPxvUhC9ZzvhccPUYviNi0kH40eHjzZsvSSWWjfIw4ipK14fCp5YFAB+/B+QuEmc6B+yTfW/v//CoDJweNEsvVmfwzeRdIO19JTp+DPUXm1VllIjui28uzob8Dxe/oWFuWngE18xYUqJl7QZPy3Xq4HY9PyIva1JMqKZNkougIQaO4qzlkhxCooZ1CZ32riXMyPa',
                }

                cookies = {
                    'token': ck[1]
                }

                async with session.post(url=url, params=params, headers=headers, json=payload,
                                        cookies=cookies) as response:
                    result = await response.text()
                    now = datetime.now()
                    time_str = now.strftime("%H:%M:%S:%f")[:-3]
                    print(f'{time_str}:[{ck[0]}]:{result}')
                    if result.find('抢卷成功') != -1:
                        print(f'{ck[0]}:成功')
                        break
                    else:
                        await asyncio.sleep(0.6)
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
