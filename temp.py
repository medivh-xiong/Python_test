import requests

cookies = {
    '__jda': '181111935.1668069089029464342293.1668069089.1708505434.1708509820.233',
    'b_dw': '1905',
    'b_dh': '942',
    'b_dpr': '2',
    'b_webp': '1',
    'b_avif': '1',
    'shshshfpb': 'BApXeoJ4qyOhA5kVcheQqbPiQ8NWkO6NcBypHl75X9xJ1MhsrroO2',
    'shshshfp': 'b6ec8c37a67e0e37fd7f25ffacb1dc2b',
    'shshshfpa': '3910eb4c-77a3-c4d8-4a59-99a21ffd1286-1668069091',
    'jcap_dvzw_fp': 'MStjxvc74o8PNBQNWwvkqMy4UUC2oFU3mziJBO7xwNEc-qWJfCkVnJtoSp00zaKo8Gu2BA==',
    '__jdu': '1668069089029464342293',
    'shshshfpx': '3910eb4c-77a3-c4d8-4a59-99a21ffd1286-1668069091',
    '3AB9D23F7A4B3CSS': 'jdd037XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4AAAAMNZMRATNIAAAAAD77VMKQ5DMI3NUX',
    'unpl': 'JF8EAKhnNSttX0NdARoATxQSG10HWwoNSB4CamIGVg1fTQBVElAbFER7XlVdWBRKFB9sZxRUWlNPVQ4ZACsSEHtdVV9dD0MTA2hkNWRdWUpUBBwLGBsSe15Ublw4SxAEZmYCXFxRQ1UGEwccFxJOXldWXzhKJwNnYDVkbVl7VAQbAxMiEktcVV9YDk8TC18sa1UQWExTDBoFExMZQ1xXVlgPThUGbGQNVm1Ze1c',
    'pinId': '9zvM1MUZPR30TcKyARJfCQ',
    'whwswswws': '',
    'TrackID': '1qzgjq5pK4vuM12LfiEvxuS_7rEXiKO8eEeUfPmOPfhtO5lzVWG5e1RIiHFY0R7TA0sKxHcxnn4Fv96zSoaINJgG85dIoc9m5Pdl18ZJkE6Aa8buB0GsYoqlTkCTj-Wbj',
    'ipLoc-djd': '12-904-907-50559',
    'pin': '15951003078_p',
    'unick': '%E5%86%A5%E7%8E%8B%E4%B9%8B%E6%AD%8C',
    '_tp': 'ak3bQDgGku8%2BskP5GCRaiw%3D%3D',
    '_pst': '15951003078_p',
    'warehistory': '"10085827003737,100064695864,100064695864,10081479480401,10081479480401,100066206148,10086397575079,10091517815466,100068431529,100058134266,100035340746,"',
    'mba_muid': '1668069089029464342293',
    'joyya': '1708505237.1708505243.49.1i1937q',
    'retina': '1',
    'cid': '9',
    'webp': '1',
    'visitkey': '737803510179678',
    'equipmentId': '7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4',
    'fingerprint': '808f4ae16c15d708044b42078e6b45d9',
    'deviceVersion': '122.0',
    'deviceOS': '',
    'deviceOSVersion': '',
    'deviceName': 'Firefox',
    '__wga': '1708505444145.1708505444145.1706755024545.1706755024545.1.2',
    'sc_width': '1920',
    'TARGET_UNIT': 'bjcenter',
    'ceshi3.com': '201',
    '__jdc': '181111935',
    'wlfstk_smdl': 'e8i1new46uubar3ioih4ul9532oibmup',
    'appCode': 'ms0ca95114',
    '__jdv': '95931165%7Ckong%7Ct_1001695162_%7Cjingfen%7C698503e73a1b4f42804423a67ea8c17e%7C1708505473618',
    'areaId': '12',
    'joyytokem': 'babel_23iCQkqfSFk5s8ie86ggtJMzVp4WMDFpZUdqdDk5MQ==.WFJ3UkFZUHVZTFBVcxQxEwkqWUMMEnQJClhJcUZFRVQ5WApYGwUrBDEALz8FCxwyAjVcDhEJHAw0NggkADR/JCMCKnEkFyscNyIYXlAfUwwjVAoCBxsXKCVGFxs=.9874fecb',
    'wxa_level': '1',
    'jxsid': '17085054438780613147',
    'PPRD_P': 'EA.17053.1.1-UUID.1668069089029464342293',
    '__jd_ref_cls': 'Babel_staytimeExpo',
    'mba_sid': '17085088717894569530423499346.0',
    '__jdb': '181111935.5.1668069089029464342293|233.1708509820',
    'thor': 'BF80140138890A11F2001240DE13FB3F3C61C0880504BFA8A1E9BDE57F39C654446FCF0B0368B1B87ECB49154D3FA9771981E851793FBC2F1BC369F2284164BDCF5F6F604977DC2AFC32B2AF7BEA92CAC927790641C26AE2D827E958FCDE3A69CAA21D9483485E5BC1B26112362198F0D30BEC08B16BFC3408AA913CB86F8D9968A0F50371768AD1D15A7626F6F588BC',
    'flash': '2_Y-yYDSx4OkxRGgtBchJT9K6hmP8Xl6qQACgpqh9P2dOSZ0dLY1gL9etUsnPSm2S9irep3t6nTE2UlDPWZnS5_F6PFEoDxrt0B4NfQhN0CPN*',
    'jsavif': '1',
    'shshshsID': '3f56aa6eef41630953040e7cdb136dde_3_1708510020871',
    'token': '5ad247847cc9c6d559c882b05e393791,3,949172',
    '__tk': 'a71f722f8e0d1e649892d31121bd1016,3,949172',
    '3AB9D23F7A4B3C9B': '7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4',
    '_gia_d': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:122.0) Gecko/20100101 Firefox/122.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'x-referer-page': 'https://item.jd.com/100065364971.html',
    'x-rp-client': 'h5_1.0.0',
    'Origin': 'https://item.jd.com',
    'Connection': 'keep-alive',
    'Referer': 'https://item.jd.com/',
    # 'Cookie': '__jda=181111935.1668069089029464342293.1668069089.1708505434.1708509820.233; b_dw=1905; b_dh=942; b_dpr=2; b_webp=1; b_avif=1; shshshfpb=BApXeoJ4qyOhA5kVcheQqbPiQ8NWkO6NcBypHl75X9xJ1MhsrroO2; shshshfp=b6ec8c37a67e0e37fd7f25ffacb1dc2b; shshshfpa=3910eb4c-77a3-c4d8-4a59-99a21ffd1286-1668069091; jcap_dvzw_fp=MStjxvc74o8PNBQNWwvkqMy4UUC2oFU3mziJBO7xwNEc-qWJfCkVnJtoSp00zaKo8Gu2BA==; __jdu=1668069089029464342293; shshshfpx=3910eb4c-77a3-c4d8-4a59-99a21ffd1286-1668069091; 3AB9D23F7A4B3CSS=jdd037XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4AAAAMNZMRATNIAAAAAD77VMKQ5DMI3NUX; unpl=JF8EAKhnNSttX0NdARoATxQSG10HWwoNSB4CamIGVg1fTQBVElAbFER7XlVdWBRKFB9sZxRUWlNPVQ4ZACsSEHtdVV9dD0MTA2hkNWRdWUpUBBwLGBsSe15Ublw4SxAEZmYCXFxRQ1UGEwccFxJOXldWXzhKJwNnYDVkbVl7VAQbAxMiEktcVV9YDk8TC18sa1UQWExTDBoFExMZQ1xXVlgPThUGbGQNVm1Ze1c; pinId=9zvM1MUZPR30TcKyARJfCQ; whwswswws=; TrackID=1qzgjq5pK4vuM12LfiEvxuS_7rEXiKO8eEeUfPmOPfhtO5lzVWG5e1RIiHFY0R7TA0sKxHcxnn4Fv96zSoaINJgG85dIoc9m5Pdl18ZJkE6Aa8buB0GsYoqlTkCTj-Wbj; ipLoc-djd=12-904-907-50559; pin=15951003078_p; unick=%E5%86%A5%E7%8E%8B%E4%B9%8B%E6%AD%8C; _tp=ak3bQDgGku8%2BskP5GCRaiw%3D%3D; _pst=15951003078_p; warehistory="10085827003737,100064695864,100064695864,10081479480401,10081479480401,100066206148,10086397575079,10091517815466,100068431529,100058134266,100035340746,"; mba_muid=1668069089029464342293; joyya=1708505237.1708505243.49.1i1937q; retina=1; cid=9; webp=1; visitkey=737803510179678; equipmentId=7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4; fingerprint=808f4ae16c15d708044b42078e6b45d9; deviceVersion=122.0; deviceOS=; deviceOSVersion=; deviceName=Firefox; __wga=1708505444145.1708505444145.1706755024545.1706755024545.1.2; sc_width=1920; TARGET_UNIT=bjcenter; ceshi3.com=201; __jdc=181111935; wlfstk_smdl=e8i1new46uubar3ioih4ul9532oibmup; appCode=ms0ca95114; __jdv=95931165%7Ckong%7Ct_1001695162_%7Cjingfen%7C698503e73a1b4f42804423a67ea8c17e%7C1708505473618; areaId=12; joyytokem=babel_23iCQkqfSFk5s8ie86ggtJMzVp4WMDFpZUdqdDk5MQ==.WFJ3UkFZUHVZTFBVcxQxEwkqWUMMEnQJClhJcUZFRVQ5WApYGwUrBDEALz8FCxwyAjVcDhEJHAw0NggkADR/JCMCKnEkFyscNyIYXlAfUwwjVAoCBxsXKCVGFxs=.9874fecb; wxa_level=1; jxsid=17085054438780613147; PPRD_P=EA.17053.1.1-UUID.1668069089029464342293; __jd_ref_cls=Babel_staytimeExpo; mba_sid=17085088717894569530423499346.0; __jdb=181111935.5.1668069089029464342293|233.1708509820; thor=BF80140138890A11F2001240DE13FB3F3C61C0880504BFA8A1E9BDE57F39C654446FCF0B0368B1B87ECB49154D3FA9771981E851793FBC2F1BC369F2284164BDCF5F6F604977DC2AFC32B2AF7BEA92CAC927790641C26AE2D827E958FCDE3A69CAA21D9483485E5BC1B26112362198F0D30BEC08B16BFC3408AA913CB86F8D9968A0F50371768AD1D15A7626F6F588BC; flash=2_Y-yYDSx4OkxRGgtBchJT9K6hmP8Xl6qQACgpqh9P2dOSZ0dLY1gL9etUsnPSm2S9irep3t6nTE2UlDPWZnS5_F6PFEoDxrt0B4NfQhN0CPN*; jsavif=1; shshshsID=3f56aa6eef41630953040e7cdb136dde_3_1708510020871; token=5ad247847cc9c6d559c882b05e393791,3,949172; __tk=a71f722f8e0d1e649892d31121bd1016,3,949172; 3AB9D23F7A4B3C9B=7XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4; _gia_d=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'appid': 'pc-item-soa',
    'functionId': 'pc_detailpage_wareBusiness',
    'client': 'pc',
    'clientVersion': '1.0.0',
    't': '1708510022290',
    'body': '{"skuId":100065364971,"cat":"1620,1624,1656","area":"12_904_907_50559","shopId":"1000309622","venderId":1000309622,"paramJson":"{\\"platform2\\":\\"1\\",\\"specialAttrStr\\":\\"p0ppppppppppppppppppppppppp\\",\\"skuMarkStr\\":\\"00\\"}","num":1,"bbTraffic":"","canvasType":1}',
    'h5st': '20240221180702324;qmy6yn6fyf6iilu8;fb5df;tk03wb04e1cf118nM04D5CXxUnPECgtr_3emkqiGBJsFliQd86DgeihqD3HwzvmvY7yS0fgfbkCL17Yc6Pqpykh2eGrq;159d0d63e4b8961eb50dda4b6499cdf7aa4480bc5808d7d36844757954f2c50a;4.3;1708510022324;6ab648016f4b18e308deb8189a91955075b82204fe1f5a3e2d017a46737552fa1b5c10b259f21644f0374719ac308aa52382eda65bf97eed4658bbf35cb73194e19a4f8b4d55160ac0292cca6b1e2c90786e5ae2735f7074f9041cf85cf9d97442532c9bde5164bfdd65db72fbe3e5f9641d227b565967aa7d6911c55f0fc7697069bf8f27ded9c09f61ca35b08f1bd819d55ee0a3c7b7886ae91b2676c2c02c25ab4eb79e136265876271fd09dac099a66699c9984ae4c24a127f418525e507ce5c8a72e96e367351ca59e753f6e18aece972956ae5e1c1ea6ecba2d9bff3f12ee7ae6c0f72e8ee3fa38e01e0205d47cfc46e9cb37b01275929805861417b7f47046a00bd7f57b3679a4eda50e77deadef7c122ad3a36e7f5e143cb169f484dfdc6a2f9a77e578e0dd842a5f388daeb62f23f25ec1ad1c5972565068638ecc43d5615d1b77746787d73b828a2a28f1c00f8b03b2f13161645c44d8d352b5e8e',
    'x-api-eid-token': 'jdd037XZ4KFNKG3RR5LLS4T52YX7GCCIVGQ2465FGEM3SYK7OXUT7FDIKO5PDRC3QC2IRK2KKOJV2QZXZUL727RCLFSHNS4AAAAMNZMRATNIAAAAAD77VMKQ5DMI3NUX',
    'loginType': '3',
    'scval': '100065364971',
    'uuid': '181111935.1668069089029464342293.1668069089.1708505434.1708509820.233',
}

response = requests.get('https://api.m.jd.com/', params=params, cookies=cookies, headers=headers)
print(response.text)