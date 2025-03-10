import requests
import time
import datetime

cookies = {
    '__jda': '76161171.1668069089029464342293.1668069089.1715132943.1715132963.301',
    'b_dw': '412',
    'b_dh': '915',
    'b_dpr': '2.625',
    'b_webp': '1',
    'b_avif': '1',
    'shshshfpb': 'BApXc_mjsVupA5kVcheQqbPiQ8NWkO6NcBypHl75V9xJ1P40OJNOHwkq43HyiDJa0A2Zd1g',
    'shshshfp': 'b6ec8c37a67e0e37fd7f25ffacb1dc2b',
    'shshshfpa': '3910eb4c-77a3-c4d8-4a59-99a21ffd1286-1668069091',
    'jcap_dvzw_fp': 'MStjxvc74o8PNBQNWwvkqMy4UUC2oFU3mziJBO7xwNEc-qWJfCkVnJtoSp00zaKo8Gu2BA==',
    '__jdu': '1668069089029464342293',
    'shshshfpx': '3910eb4c-77a3-c4d8-4a59-99a21ffd1286-1668069091',
    '3AB9D23F7A4B3CSS': 'jdd037XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4AAAAMPKXR667YAAAAACIH7F2JQCUCKIMX',
    'unpl': 'JF8EAJ9nNSttD0pSUhsFSRQSTllVW1gBQx4DOG5WVg0MH1NRHlZLGxR7XlVdWBRKEx9ubhRVVVNOXA4YBisSEHtdVV9dAE8RAGdiNWRdWUpXBhMHGhMYe15Ublw4SxAEZmYCXFxRQ1UGEwccFxJOXldWXzhKJwNnYDVkbVl7VwYfAhkiEXsWOl8QCEwQCm5gDVVUUEpXDR4FHhAVSF5cXG0JexQ',
    'pinId': '9zvM1MUZPR30TcKyARJfCQ',
    'whwswswws': '',
    'TrackID': '1jiZOhg8eurkv1ZfS2coHN-kgbsGLglVL63gP6uI5x8vzPFIzekf4YZ36vZFpiMSBx9rvgDw0iXeIeWR87PODWgOxq7IeJi5AFyt5HpDZJTDpe28GE76nRUSW4rjayoZX',
    'warehistory': '"10084577619755,100048859487,100048859487,100061645402,100064695864,100064695864,100044495682,10084544825151,100066921033,100088587403,100066930469,100066921033,10024782385098,100088849495,10085827003737,100064695864,100064695864,10081479480401,10081479480401,100066206148,"',
    'autoOpenApp_downCloseDate_auto': '1712541503863_1800000',
    '3AB9D23F7A4B3C9B': '7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4',
    'mba_muid': '1668069089029464342293',
    'retina': '1',
    'cid': '9',
    'webp': '1',
    'visitkey': '5995296362681319179',
    'equipmentId': '7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4',
    'fingerprint': '256920febebae7ae67c82b23818eedd7',
    'deviceVersion': '124.0',
    'deviceOS': '',
    'deviceOSVersion': '',
    'deviceName': 'Firefox',
    '__wga': '1712806089494.1712806089494.1712627781655.1711591359138.1.6',
    'joyya': '1715133019.1715133025.58.0ckqgms',
    'TrackerID': 'vhHD2FRnAUCw-h_-3eQcUmbPdhFBvwstHZg2J-GMBtPDYovSVBh2PWZb1y2JZx1KbPJgKFxYORpkZ_BFqj76PTQBI75lol8xWiU2X57_4Sqfpn1sVgQeO4gA2a4yKiV41r-GhE47WV9a5jO-LYAQKg',
    'pt_key': 'AAJmE08pADDtCQcCnf4_dE3MSDYq_mKyiC5vY7ejYvv1Jl4J__J8K14MlaHkyRQtpvSrh_SHuM4',
    'pt_pin': '15951003078_p',
    'pt_token': 'ku4yj5qz',
    'pwdt_id': '15951003078_p',
    'addrId_1': '6751590348',
    'mitemAddrId': '12_904_3376_57873',
    'mitemAddrName': '%u6C5F%u82CF%u5357%u4EAC%u5E02%u5EFA%u90BA%u533A%u6C99%u6D32%u8857%u9053%u5EB7%u5E84%u99A8%u82D11%u680B2%u5355%u51432604%u5BA4',
    'wq_addr': '6751590348%7C12_904_3376_57873%7C%u6C5F%u82CF_%u5357%u4EAC%u5E02_%u5EFA%u90BA%u533A_%u6C99%u6D32%u8857%u9053%7C%u6C5F%u82CF%u5357%u4EAC%u5E02%u5EFA%u90BA%u533A%u6C99%u6D32%u8857%u9053%u5EB7%u5E84%u99A8%u82D11%u680B2%u5355%u51432604%u5BA4%7C118.759291%2C32.012816',
    '__jdv': '76161171%7Ckong%7Ct_1001957294_%7Cjingfen%7Cf07f16c73450448981f8b3aee6e4ea85%7C1715133019188',
    'TARGET_UNIT': 'bjcenter',
    'ceshi3.com': '201',
    'JSESSIONID': '388F37AE2F221DD82B286A26FA27D66A.s1',
    '__jdc': '76161171',
    'appCode': 'ms0ca95114',
    'share_cpin': '',
    'share_open_id': '',
    'share_gpin': '',
    'shareChannel': '',
    'source_module': '',
    'erp': '',
    'language': 'zh_CN',
    'p-request-id': '15951003078_p2024040911KMhgmqdyuH',
    '__jdb': '76161171.2.1668069089029464342293|301.1715132963',
    'mba_sid': '1715132943969113358154796431.3',
    'joyytokem': 'babel_2NvVHKHusKCYwcavjT9Fe1zwvQ8JMDFJc05BYjk5MQ==.eER/dFN6QH5zU39Efz8nehUXJ1IGRwAqHHhfeG1TZUIwcxx4DQwAEhEQF3YuOiU7MSN/CRYkOAMiJxAhZBo8KSYRI2MkNSgaPBkoIQkZeBoDQgMpETsBIQ5QNw0=.57ae032c',
    '_gia_d': '1',
    '__jd_ref_cls': 'Babel_H5FirstClick',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://prodev.m.jd.com/mall/active/2NvVHKHusKCYwcavjT9Fe1zwvQ8J/index.html?babelChannel=ttt49&utm_user=plusmember&_ts=1715045454702&ad_od=share&gxd=RnAoxjJQbT3en8kWq4xxWu1_WJ1lKfKWy1i6pD1CNEQYISE5rf7Rbx6fNCAWV8E&gx=RnAomTM2Dm-sqvx98MUPCWg6ONXPvA&rid=22513&cu=true&utm_source=kong&utm_medium=jingfen&utm_campaign=t_1001957294_&utm_term=f07f16c73450448981f8b3aee6e4ea85',
    'Content-Type': 'application/x-www-form-urlencoded',
    'x-referer-page': 'https://prodev.m.jd.com/mall/active/2NvVHKHusKCYwcavjT9Fe1zwvQ8J/index.html',
    'x-rp-client': 'h5_1.0.0',
    'X-Babel-ActId': '2NvVHKHusKCYwcavjT9Fe1zwvQ8J',
    'Origin': 'https://prodev.m.jd.com',
    'Connection': 'keep-alive',
    # 'Cookie': '__jda=76161171.1668069089029464342293.1668069089.1715132943.1715132963.301; b_dw=412; b_dh=915; b_dpr=2.625; b_webp=1; b_avif=1; shshshfpb=BApXc_mjsVupA5kVcheQqbPiQ8NWkO6NcBypHl75V9xJ1P40OJNOHwkq43HyiDJa0A2Zd1g; shshshfp=b6ec8c37a67e0e37fd7f25ffacb1dc2b; shshshfpa=3910eb4c-77a3-c4d8-4a59-99a21ffd1286-1668069091; jcap_dvzw_fp=MStjxvc74o8PNBQNWwvkqMy4UUC2oFU3mziJBO7xwNEc-qWJfCkVnJtoSp00zaKo8Gu2BA==; __jdu=1668069089029464342293; shshshfpx=3910eb4c-77a3-c4d8-4a59-99a21ffd1286-1668069091; 3AB9D23F7A4B3CSS=jdd037XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4AAAAMPKXR667YAAAAACIH7F2JQCUCKIMX; unpl=JF8EAJ9nNSttD0pSUhsFSRQSTllVW1gBQx4DOG5WVg0MH1NRHlZLGxR7XlVdWBRKEx9ubhRVVVNOXA4YBisSEHtdVV9dAE8RAGdiNWRdWUpXBhMHGhMYe15Ublw4SxAEZmYCXFxRQ1UGEwccFxJOXldWXzhKJwNnYDVkbVl7VwYfAhkiEXsWOl8QCEwQCm5gDVVUUEpXDR4FHhAVSF5cXG0JexQ; pinId=9zvM1MUZPR30TcKyARJfCQ; whwswswws=; TrackID=1jiZOhg8eurkv1ZfS2coHN-kgbsGLglVL63gP6uI5x8vzPFIzekf4YZ36vZFpiMSBx9rvgDw0iXeIeWR87PODWgOxq7IeJi5AFyt5HpDZJTDpe28GE76nRUSW4rjayoZX; warehistory="10084577619755,100048859487,100048859487,100061645402,100064695864,100064695864,100044495682,10084544825151,100066921033,100088587403,100066930469,100066921033,10024782385098,100088849495,10085827003737,100064695864,100064695864,10081479480401,10081479480401,100066206148,"; autoOpenApp_downCloseDate_auto=1712541503863_1800000; 3AB9D23F7A4B3C9B=7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4; mba_muid=1668069089029464342293; retina=1; cid=9; webp=1; visitkey=5995296362681319179; equipmentId=7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4; fingerprint=256920febebae7ae67c82b23818eedd7; deviceVersion=124.0; deviceOS=; deviceOSVersion=; deviceName=Firefox; __wga=1712806089494.1712806089494.1712627781655.1711591359138.1.6; joyya=1715133019.1715133025.58.0ckqgms; TrackerID=vhHD2FRnAUCw-h_-3eQcUmbPdhFBvwstHZg2J-GMBtPDYovSVBh2PWZb1y2JZx1KbPJgKFxYORpkZ_BFqj76PTQBI75lol8xWiU2X57_4Sqfpn1sVgQeO4gA2a4yKiV41r-GhE47WV9a5jO-LYAQKg; pt_key=AAJmE08pADDtCQcCnf4_dE3MSDYq_mKyiC5vY7ejYvv1Jl4J__J8K14MlaHkyRQtpvSrh_SHuM4; pt_pin=15951003078_p; pt_token=ku4yj5qz; pwdt_id=15951003078_p; addrId_1=6751590348; mitemAddrId=12_904_3376_57873; mitemAddrName=%u6C5F%u82CF%u5357%u4EAC%u5E02%u5EFA%u90BA%u533A%u6C99%u6D32%u8857%u9053%u5EB7%u5E84%u99A8%u82D11%u680B2%u5355%u51432604%u5BA4; wq_addr=6751590348%7C12_904_3376_57873%7C%u6C5F%u82CF_%u5357%u4EAC%u5E02_%u5EFA%u90BA%u533A_%u6C99%u6D32%u8857%u9053%7C%u6C5F%u82CF%u5357%u4EAC%u5E02%u5EFA%u90BA%u533A%u6C99%u6D32%u8857%u9053%u5EB7%u5E84%u99A8%u82D11%u680B2%u5355%u51432604%u5BA4%7C118.759291%2C32.012816; __jdv=76161171%7Ckong%7Ct_1001957294_%7Cjingfen%7Cf07f16c73450448981f8b3aee6e4ea85%7C1715133019188; TARGET_UNIT=bjcenter; ceshi3.com=201; JSESSIONID=388F37AE2F221DD82B286A26FA27D66A.s1; __jdc=76161171; appCode=ms0ca95114; share_cpin=; share_open_id=; share_gpin=; shareChannel=; source_module=; erp=; language=zh_CN; p-request-id=15951003078_p2024040911KMhgmqdyuH; __jdb=76161171.2.1668069089029464342293|301.1715132963; mba_sid=1715132943969113358154796431.3; joyytokem=babel_2NvVHKHusKCYwcavjT9Fe1zwvQ8JMDFJc05BYjk5MQ==.eER/dFN6QH5zU39Efz8nehUXJ1IGRwAqHHhfeG1TZUIwcxx4DQwAEhEQF3YuOiU7MSN/CRYkOAMiJxAhZBo8KSYRI2MkNSgaPBkoIQkZeBoDQgMpETsBIQ5QNw0=.57ae032c; _gia_d=1; __jd_ref_cls=Babel_H5FirstClick',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'functionId': 'newBabelAwardCollection',
}

data = 'body=%7B%22activityId%22%3A%222NvVHKHusKCYwcavjT9Fe1zwvQ8J%22%2C%22gridInfo%22%3A%22%22%2C%22transParam%22%3A%22%7B%5C%22bsessionId%5C%22%3A%5C%22ae235df3-6263-49e0-b1a1-448b9c7bd945%5C%22%2C%5C%22babelChannel%5C%22%3A%5C%22ttt12%5C%22%2C%5C%22actId%5C%22%3A%5C%2201515392%5C%22%2C%5C%22enActId%5C%22%3A%5C%222NvVHKHusKCYwcavjT9Fe1zwvQ8J%5C%22%2C%5C%22pageId%5C%22%3A%5C%224884063%5C%22%2C%5C%22encryptCouponFlag%5C%22%3A%5C%221%5C%22%2C%5C%22sc%5C%22%3A%5C%22apple%5C%22%2C%5C%22scv%5C%22%3A%5C%2211.4.4%5C%22%2C%5C%22requestChannel%5C%22%3A%5C%22h5%5C%22%2C%5C%22jdAtHomePage%5C%22%3A%5C%220%5C%22%2C%5C%22utmFlag%5C%22%3A%5C%220%5C%22%2C%5C%22locType%5C%22%3A%5C%221%5C%22%7D%22%2C%22scene%22%3A%221%22%2C%22args%22%3A%22key%3D103EA2635E1CFA47B0441D3AC0809834DA13670B78A8260359D54E80B20544C6B8B4B222EC50490DA00D97AECB25B3A3_bingo%2CroleId%3DAA493A65460C2006129F385E73F03E140AB8CC889C71B3E7236A303CEECC3102723E50B79290A8C014C135E8B326DFAEDBF29C796EFD174F3B1F414B4050C428AD1DD15A680FA1BA666E991A043009402D3FA1190310D0C442A2405C5DB4B33B4D0DBB9CA5384958B86FE60D46182C3782F420A57397A25B7E7D91B1D3DE4D0312A0124EA86637A4A3200CABE9F2D944B5FC29DC6B2A85E599E22CFE6BD37136_bingo%2CstrengthenKey%3D7740E17E7A71CA84498E613D9A17A913080F298AFFB6DEF6D8161A4D30AA93D819001B7C658E209AEB4DD6D075AEA4C1_bingo%22%2C%22platform%22%3A%221%22%2C%22orgType%22%3A%222%22%2C%22openId%22%3A%22-1%22%2C%22pageClickKey%22%3A%22-1%22%2C%22eid%22%3A%22FRRVZMPWQDLW6LATJPMV7GHWHTLMRYST6R4U3CCFGQBRQPZ3KPJND6J42YY7O3PVAXHN2Y37TXFUTUPMVCI7WOJHDQ%22%2C%22fp%22%3A%22e28f8e88fb9244b86271b1b48736f894%22%2C%22shshshfp%22%3A%22a23f6274500c49832e22a18f4aa7cbb0%22%2C%22shshshfpa%22%3A%22ff60138c-b977-e3e6-4566-fe632457f80e-1685031503%22%2C%22shshshfpb%22%3A%22BApXcfHvlVupA62ZsMStzMPMCYp6vQaHRNiCahUDX9xJ1MpnBvYO2%22%2C%22childActivityUrl%22%3A%22https%253A%252F%252Fpro.m.jd.com%252Fmall%252Factive%252F2NvVHKHusKCYwcavjT9Fe1zwvQ8J%252Findex.html%253Ftttparams%253DQ9fw4eyJnTGF0IjoiMzEuOTg1MDMiLCJ1bl9hcmVhIjoiMTJfOTA0XzMzNzZfNTc4NzMiLCJkTGF0IjoiIiwicHJzdGF0ZSI6IjAiLCJhZGRyZXNzSWQiOiIxMTc4Mzg1MjY3MCIsImxhdCI6IjMxLjk3MDA3NiIsInBvc0xhdCI6IjMxLjk4NTAzIiwicG9zTG5nIjoiMTE4LjcyMjAzIiwiZ3BzX2FyZWEiOiIxMl85MDRfMzM3OV82MjE4MyIsImxuZyI6IjExOC43NjQ0NTIiLCJnTG5nIjoiMTE4LjcyMjAzIiwibW9kZWwiOiJpUGhvbmUxMCwxIiwiZExuZyI6Ii5J9%2526babelChannel%253Dttt12%2526jumpFrom%253D1%22%2C%22userArea%22%3A%22-1%22%2C%22client%22%3A%22%22%2C%22clientVersion%22%3A%22%22%2C%22uuid%22%3A%22%22%2C%22osVersion%22%3A%22%22%2C%22brand%22%3A%22%22%2C%22model%22%3A%22%22%2C%22networkType%22%3A%22%22%2C%22jda%22%3A%22-1%22%2C%22pageClick%22%3A%22Babel_Coupon%22%2C%22couponSource%22%3A%22manual%22%2C%22couponSourceDetail%22%3A%22-100%22%2C%22channel%22%3A%22%E9%80%9A%E5%A4%A9%E5%A1%94%E4%BC%9A%E5%9C%BA%22%2C%22batchId%22%3A%221128709233%22%2C%22headArea%22%3A%2212_904_3379_62183%22%2C%22couponTemplateFrom%22%3A%22%22%2C%22siteClient%22%3A%22apple%22%2C%22mitemAddrId%22%3A%22%22%2C%22geo%22%3A%7B%22lng%22%3A%22118.764452%22%2C%22lat%22%3A%2231.970076%22%7D%2C%22addressId%22%3A%22%22%2C%22posLng%22%3A%22118.72203%22%2C%22posLat%22%3A%2231.98503%22%2C%22un_area%22%3A%2212_904_3376_57873%22%2C%22gps_area%22%3A%2212_904_3379_62183%22%2C%22homeLng%22%3A%22118.72203%22%2C%22homeLat%22%3A%2231.98503%22%2C%22homeCityLng%22%3A%22%22%2C%22homeCityLat%22%3A%22%22%2C%22focus%22%3A%22%22%2C%22innerAnchor%22%3A%22%22%2C%22cv%22%3A%222.0%22%2C%22gLng1%22%3A%22%22%2C%22gLat1%22%3A%22%22%2C%22head_area%22%3A%22%22%2C%22fullUrl%22%3A%22https%3A%2F%2Fpro.m.jd.com%2Fmall%2Factive%2F2NvVHKHusKCYwcavjT9Fe1zwvQ8J%2Findex.html%3Ftttparams%3DQ9fw4eyJnTGF0IjoiMzEuOTg1MDMiLCJ1bl9hcmVhIjoiMTJfOTA0XzMzNzZfNTc4NzMiLCJkTGF0IjoiIiwicHJzdGF0ZSI6IjAiLCJhZGRyZXNzSWQiOiIxMTc4Mzg1MjY3MCIsImxhdCI6IjMxLjk3MDA3NiIsInBvc0xhdCI6IjMxLjk4NTAzIiwicG9zTG5nIjoiMTE4LjcyMjAzIiwiZ3BzX2FyZWEiOiIxMl85MDRfMzM3OV82MjE4MyIsImxuZyI6IjExOC43NjQ0NTIiLCJnTG5nIjoiMTE4LjcyMjAzIiwibW9kZWwiOiJpUGhvbmUxMCwxIiwiZExuZyI6Ii5J9%26babelChannel%3Dttt12%26jumpFrom%3D1%22%2C%22log%22%3A%221715133690530~1pEu8RUn9N7MDFNbXRmaDk5MQ%3D%3D.fFpFU1l%2BXkJWX3VfRRgsLDdBU1sUACEuFnxBQkpZYVwKVBZ8EzYnGBUOOl8SJDsBFiwuDhtfBR1cEC4%2BJ1oTHF0hOSMAKXw%2BGjEYGAksXxAHXDkWBg8bLSlaMxM%3D.4304bed8~1%2C1~22605748C93E2EDC7C2251062E5C6B29CAFBE221~0grc2s0~C~TBdGWhIMbGgeFURYWhcIbBJSBhgKBBxzZRkDdBxDG0EQGxJSAhgFbhxzZxkEfwkaVhlGFRwUUwIfAGkacmUeAXoOG1QeQxJrGxdVRV4UDQEeFUNFFQ8QBgcHAgQBBAYOBgwLAQEABw0QGxJBUlEQDRJCQ0FGQ0RQURceFUdTVhcIFVZQQ0FGQ0VXFRkQR1RYFQ9pBAgaBgEKGwICGw0eBhwDahkQXVoUDQYeFVNFFQ8QU1EHBgQEUwcAUgUEDlJUAQADAgUPBwMAUgUPVQULDwEUGxdcRxIMFVxiX19YUhceFUQUDQQFBgUHBAYEDgADBAUeFVpdFQ8QDwcAAwdWAVFUVlcBVglTVgYAUlECDlFXD1JSAQRTVAQAVQwFVgIADxceFVZGVRcIFXJ3R21RZXVAWmNHR3RVVFoLWmAHU31kXQdRTQBeY2dQdgRhWWdGYlFqDkh8BnhCWXJAbnoAFRwUWUMQDRJ3R0VeUhB1WFhCQkRTRRkSfl5VGRceFV5XQRcIFQEADwACBxIaFUZRRRIMbAMEABwFAABvGxJEWBcIbBJfZ11dWVUHBxkDFRwUXnphFRwUBgMcAh4HFRkQBgEYAxsGFRwUBgMKAgAGFRkQDwcAAwdWAVFUVlcBVglTVgYAUlECDlFXD1JSAQRTVAQAVQwFVgIADxceFVEUahkQXl9XFQ8QUVZQUVNUQ0QUGxdTXRIMFUAQGxJVXhcIFUcFGQAcBRIaFVZUaEYUDRcLDhIaFVdWFQoURVRcU19bCkRmQURSX0NfFRwUWl8QDWsHGwUeB20aFVdeWFcUDRcDAAEDBgYBAQAAAQUCSQFye1EDQ2h3dFJ5enR8B1FkbVlsY3RLeXELChtgYnpYYQRgf2JbYWBnB0h4bWdKYnlOVAxxQFh7ZVh%2FAXdBfW9%2BcgVmYHBjWGZ0Q3NxT2FccWZFYH9fQHF6ZH1cclx3b3ZcW1dxdGJzelxdTXhdfk11cXFvfmR3cnpzYlh9c2Vgfmd3eGdOBx5gdUNldE9rc3RPBm1xUEMLGQRQUVIFBQJRSUYaBktMSXJIY3dkYmdeYnt0YWFzcGRnYXdOVHN0QAhudE13VXZnQ3JjZgRgcWdBZWFOYnt0ZnV0dUJRYXdjZWJnBV9jcmQCYWZRZXd1dWZwcWRZYXZkRGNqXGVgc2dncWNRYnNwYXlkcE1nf3ZwXGJ0Yl8LSQVAAkdUR0UQGxJbRFIQDRIUSg%3D%3D~03xi35z%22%2C%22random%22%3A%22qTvtdhvm%22%2C%22floor_id%22%3A%22104787633%22%7D&screen=750*1334&client=wh5&clientVersion=1.0.0&sid=c0722e99c5e5a4ee0037c9097f0a0aew&uuid=&area=12_904_3376_57873&uemps=&appid=wh5&ext=%7B%22prstate%22%3A%220%22%7D&functionId=newBabelAwardCollection&h5st=20240508100130548%3Bmtgt6m6tmn5iy9m1%3B35fa0%3Btk03wb9881bc618nyv0Iphu2OCwKfB_X7feiUsWY_DUCzjqLeY0SXKi5l0lQ_FVONcALaXPlN-v2vHAG7PWEb93jPVYA%3B573dec9bb67f9ec296c6b2c0283ab717f2f7e4abdf2d227b89b53e4504b0ffae%3B4.7%3B1715133690548%3BTKmWeupG4BD8DnMKSNsOOB63RYNwdJ2VH5Q1Y1-ExMZbprWcungkyTH0uBdgOkA2qcXX_PU5HEyaeVhU4yxpkJekhqUWqMdzG-nHW3utdh3qgd9PmeXX-L3-mR4QNn6TE0woIJqIs7R9juenDvEKeOT7z3UNsCGNwNRIzutTyilQmIPlkJKvgDFZi4R__zXFc4IaUN1WGO2Ve6x879LqPaWT2GejpvV2aY990dYlVLeyLkoX2Ec9q5HLszStIIoSMbL-b5kgRuKRc9oLDUB0cGiA-OSateQd5_e_x7fRKB62pVTvHSBsY1PYdiSW5MNP8p6LMPJPDJlpkOusfgjTdNOagImb8v8Tco6rpu-05WZJAFng_r0HCtkz5_zdvwRphETIpnKCJOrXYZ7lNb2vAvZXiuqe3KzB7K89QdjAvxWa1hwGxzRNDtBwYXJoTMRJ0YDA&eid=FRRVZMPWQDLW6LATJPMV7GHWHTLMRYST6R4U3CCFGQBRQPZ3KPJND6J42YY7O3PVAXHN2Y37TXFUTUPMVCI7WOJHDQ&x-api-eid-token=jdd03FRRVZMPWQDLW6LATJPMV7GHWHTLMRYST6R4U3CCFGQBRQPZ3KPJND6J42YY7O3PVAXHN2Y37TXFUTUPMVCI7WOJHDQAAAAMONEISIQQAAAAACRVU3XSWEMLFLUX'
def send_request():
    res = requests.post('https://api.m.jd.com/client.action', params=params, headers=headers, cookies=cookies, data=data)
    print(res.text)
    return res



target_time = datetime.datetime(2024, 5, 8, 10, 0, 0, 0)
time_diff = (target_time - datetime.datetime.now()).total_seconds()
if time_diff > 0:
    time.sleep(time_diff)

result = True

while result:
    response = send_request()
    if response.status_code != 200:
        print('请求失败')
        time.sleep(0.2)
        continue
    if response.text.find('本时段优惠券已抢完'):
        print("本场已抢光，下场再来吧")
        exit()
    else:
        print('领取失败, 重新领取')
        time.sleep(0.3)
