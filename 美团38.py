import requests
import time
import datetime

cookies = {
    'token': 'AgGoHpFlA_n8y9TqOxdr_4vpfdTC6nPfuk4qPH5VyFc7OgScKp1lbfs7Wz_j8wrcDYKZUCElPGKlDwAAAAB_HgAAWreOMRDO89XAN5wSRVAPVGAQG5E6dl8TlXaVgET2E_jtGpHN5LFiNd8wJ_F_Vh47',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://market.waimai.meituan.com/',
    'Content-Type': 'application/json',
    'mtgsig': '{"a1":"1.1","a2":1709708449151,"a3":"2843ux0706vy5z16yz9x1705v995z33y81z5vyx69wy9795864v28400","a5":"hzgIzbWFPZAEeH1v9KbUt5SoitUDIUGqUI==","a6":"h1.5IGjA0OyPhGEZh8oLgkwFZKV7OKoRqqo7Ckn7m5y6YFP6hfHZ+y+AbP151No0KZjdeNo02zVmhgsGzb25MGI34MzSG9sif5Nj+kOhnIw2NKY+ASv/gxPaglEWvqWt0f7PRcsKUP8lFBjr5TJAEIHx+JUh3B0hyST2b2K3uasy4AWD0f09qdwAIWPEDEP8eFxVXT2mErwdRd7B92njA9SSJeLMBpf90gyVVmNZ5djsl2ta/7LHg23wO4wl8FvnpB27Cy81OmTmvmLztwOHoIqD8QGKomQ4dVzHz3uPfylRgFfpT2blioZAF9a41JKd1CAF","x0":4,"d1":"e86a160c4ba05f19c5039151a3ca4926"}',
    'Origin': 'https://market.waimai.meituan.com',
    'Connection': 'keep-alive',
    # 'Cookie': '_lxsdk_cuid=18a4ebc0c21c8-04accbc922e3808-41282c3d-1fa400-18a4ebc0c21c8; _lxsdk=09471AFFB3E4A37A41A3300DBD94FDB4AE933EC10E5077A1950C26B5E49848FD; WEBDFPID=2843ux0706vy5z16yz9x1705v995z33y81z5vyx69wy9795864v28400-2008898070691-1693538061601OCKIMKKdae4fde6328734eee0d0f7108610a9081705; uuid=b45290bce1ed497a8a6a.1706777495.1.0.0; iuuid=09471AFFB3E4A37A41A3300DBD94FDB4AE933EC10E5077A1950C26B5E49848FD; token=AgFOI77NcBoq7lFmQBDelMfoFllYoRZn0Dcc_vtkKM0TxhB1L9TRkyXVDM9bIzcP1RwITkrHNllNhQAAAABgHgAAoeUzNwvKu8shpmW-78DW_OTDRbrewqK2lqdHRBW_YGfPgGIujzlA3NLNbtZolROs; mt_c_token=AgFOI77NcBoq7lFmQBDelMfoFllYoRZn0Dcc_vtkKM0TxhB1L9TRkyXVDM9bIzcP1RwITkrHNllNhQAAAABgHgAAoeUzNwvKu8shpmW-78DW_OTDRbrewqK2lqdHRBW_YGfPgGIujzlA3NLNbtZolROs; oops=AgFOI77NcBoq7lFmQBDelMfoFllYoRZn0Dcc_vtkKM0TxhB1L9TRkyXVDM9bIzcP1RwITkrHNllNhQAAAABgHgAAoeUzNwvKu8shpmW-78DW_OTDRbrewqK2lqdHRBW_YGfPgGIujzlA3NLNbtZolROs; userId=4412312696; u=4412312696; isid=AgFOI77NcBoq7lFmQBDelMfoFllYoRZn0Dcc_vtkKM0TxhB1L9TRkyXVDM9bIzcP1RwITkrHNllNhQAAAABgHgAAoeUzNwvKu8shpmW-78DW_OTDRbrewqK2lqdHRBW_YGfPgGIujzlA3NLNbtZolROs; ta.uuid=1752978637768691805; isUuidUnion=true; IJSESSIONID=node0d4bqd7yxd63013ul6br7qtxul45100730; au_trace_key_net=default; openh5_uuid=09471AFFB3E4A37A41A3300DBD94FDB4AE933EC10E5077A1950C26B5E49848FD; isIframe=false; _lxsdk_s=18e127934b4-f7c-b90-054%7C%7C1126; wm_order_channel=default; utm_source=; _lx_utm=utm_campaign%3DAwaimaiBwaimai%26utm_source%3Dappshare; latlng=31.971883%2C118.758979%2C1709707808606; ci=55; cityname=%E5%8D%97%E4%BA%AC',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
}

params = {
    'couponReferId': '0BE96CC34EFE4D9AA60F8AC693F2C932',
    'actualLng': '118.764059',
    'actualLat': '31.970358',
    'geoType': '2',
    'gdPageId': '549085',
    'pageId': '556519',
    'version': '1',
    'utmSource': '',
    'utmCampaign': '',
    'instanceId': '17095402938880.12613102333857262',
    'componentId': '17095402938880.12613102333857262',
    'ctype': '',
    'utmMedium': '',
    'gSource': '',
    'dpSource': '',
    'yodaReady': 'h5',
    'csecplatform': '4',
    'csecversion': '2.4.0',
}

json_data = {
    'cType': 'mtiphone',
    'fpPlatform': 5,
    'wxOpenId': '',
    'appVersion': '',
    'mtFingerprint': 'i2HKpOmsirDPavelVfQBZMt2sJ8xjID5YgSwAfbxEDxOZHmu0PUbnWXZcLCDzCvGNUoKj1qnLl/T9cjYV2QHY3+HVLgbmzpf5F7g/yiPvKn82b3RiZLIdgeBpoR1/c5ndBwF/VUAGWqVtIsVfNNDXnpUqFF3ycvP+2R/v80Sz58fz6WE8oztrs5Go1WFPd4DsPOkXQ1F5kX0v0ndbFdnN9d7Z10k+OgTeuvoK32PCSxn9AnRCIoAHttBeNWKlP/banW/9jD3QUZnNaoYeuL0kfU77PNjD7k6XJ2d1rtprHlP7oWKoSWzoBaFIAsqk1oaRLYwNzPh2GTYSAWoEyT+tUQNC2Lsihptmnmxd84aacQ9GJIgpBvP2eGS9vyB4YtPouBEmqNaaLwOiZ5uffMjwN0y+Ashwmh74WuoaF+zcZkkswhb/w2qAQW5WB+E8DNpSfsw8CE9qhKkgm1K8BomBM9ZtMpevrHeCfwWRVBVJvsW+oX61vnfps7ZSLKYLv9sIzUshQbxNyH9zuR6h5/4yGialyMqiOFdjFGt2hPQr3dgwNPg3nA8nuXcgly5R0ziavuggu+YguKiypjLF59aIrO3Du7ZXc1pF7etiB190GJbtXxUzwELkEtkc909A7JLhr81GZ7PGmf/8hDxsgt66aJLzVI4oOaKn61AOccVrDRkQ3dwO6LgBLMfawNhjgWl597gF3aT/+4oxuP3HRhwEUGcyjsFspiQQV0xI3YHAD1ydFIFrK6zQCTytK+7apAdPlvOePgbeAOi7zxJJn8QDF4cywVqYCDclcHGMy9KFnGTKfBHr8wZ6meQBo6vd63QjKBvW7CVJHNx+zbgm7t51pqNlhVb+5zOnFjTezVh1xMDEJWDat2qSobQuq4anRxKx+sHW66wNu1MOR2OepkCOLnQDrFVZkLINSsBvbWVQMf9nnPMWebVl7CrNyPlFsGqxhsQTBrhrMZ21di4FRCnzEYWpZj+9kDb2iExAYr64bruixi3Tx1qabAyjDYO1JAYeWZmWprbOuC3eSLTomNCacofg0WiqCapTaioL1UJVigNbLp76qPrpn9xQybtvmk7a9ihembGj4Wdj3Cxe8Kn4DGC87hiOqnfNEJ0iBP4X5q6zM7poWZsy4LtBEXchqfR3BCuFcr0uqIvipLL7J2DCp4p7R6FiLajyLc/HLDAEgznHUecHGpU5QNqsu4MskK42NgoQ410pQEC1usFnqL3qiCxmJrCLN3pVouTdNhVGk6OLbCDVjVsDDJ4JzUpFKqlPp/8LEyzYgufk0OB87Mp0pBo0yHwmpCJe024r8uhj/G0NDgZKr0kUeMgrXG93y0uOWUDOeXjReXk4+BaFlvDCnMwHslylsV8IEPVejbv4+aaNLjr5w/NPWjm0h34VJAn'
}

def send_request():
    res = requests.post(
        'https://promotion.waimai.meituan.com/lottery/limitcouponcomponent/fetchcoupon',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    print(res.text)
    return res


target_time = datetime.datetime(2024, 3, 6, 17, 0, 0)
time_diff = (target_time - datetime.datetime.now()).total_seconds()
if time_diff > 0:
    time.sleep(time_diff)


result = True
time.sleep(0.5)

while result:
    response = send_request()
    if response.status_code != 200:
        print('请求失败')
        time.sleep(55)
        continue
    if response.text.find('成功') != -1:
        print('领取成功')
        exit()
    else:
        print('领取失败, 重新领取')
        time.sleep(5)

