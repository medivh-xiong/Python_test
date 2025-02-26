import aiohttp
import asyncio
import time
from datetime import datetime

# 配置区（请检查以下参数有效性）
startTime = "2025-02-26 15:00:00"
json_data = {
    'prizeNo': 'JFMS20231221',
    'opDfp': 'bK8G4IiYx29l-j6jAHh8yUTyP4W_sybKs-Otg0iHsaLDuPI5csU-ugpVWLG6DnKXFV0lP5wZzea7lYzOT2QD0isIHJFiPxOLW2CMllsnebQAZmfeqmXMqQUBbHOSDeg9d7CMcHFANkADAEAQGBsP3a9YC9j8e4yf',
    'sign': 'B',
}
cookies = {
    'sid': 'MCALOGIN-e6dde90b-4168-46d2-89b3-ed736cb19d8c',
    'act_sid': 'act-dacc6c76-ea38-4a3e-8ecb-7d69b1a03f61',
}  # 保持原有cookies不变

url = "https://ump.cmpay.com/activities/v1/members/integralTicketReceive"
headers = {
    'Host': 'ump.cmpay.com',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    # 'Cookie': 'sid=MCALOGIN-e6dde90b-4168-46d2-89b3-ed736cb19d8c; act_sid=act-dacc6c76-ea38-4a3e-8ecb-7d69b1a03f61',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Html5Plus/1.0 (Immersed/20) uni-app',
    'X-Requested-With': 'XMLHttpRequest',
}

# 新增参数
REQUEST_DELAY = 0.1  # 请求间隔(秒)，根据网络环境调整

async def qiang_shenquan():
    """新版低并发异步方案"""
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            try:
                async with session.post(
                        url=url,
                        headers=headers,
                        json=json_data,
                        cookies=cookies,
                        timeout=3
                ) as response:
                    result = await response.text()
                    print(f"[第{i + 1}次] {datetime.now().strftime('%H:%M:%S:%f')[:-3]} -> {result}")
            except Exception as e:
                print(f"[异常] {type(e).__name__}: {str(e)}")

            # 控制请求节奏
            await asyncio.sleep(REQUEST_DELAY)


async def main():
    target_time = datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S")
    while datetime.now() < target_time:
        remaining = (target_time - datetime.now()).total_seconds()
        print(f"\r等待抢购开始 | 剩余时间: {remaining:.2f}s", end="")
        await asyncio.sleep(0.1)
    print("\n🔔 开始低并发模式抢购！")
    await qiang_shenquan()


if __name__ == '__main__':
    asyncio.run(main())