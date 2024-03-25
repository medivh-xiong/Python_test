import requests

import requests


headers = {
    'Host': 'ghjf-api.g-town.com.cn',
    'content-type': 'application/json;charset=utf-8',
    'accept': 'application/json, text/plain, */*',
    'authorization': 'ICBC nv8An%20b2QZ66rbmIwG7Fg1xmaUfLbAcSgWVSbk%2F29SZt9zRFdWGnqPBOdYh8aaYfbYv%2FE53TfZ6n5yEcmGXEp8BKTJPkyTm8KbIvTvESZ4wdiDkyr%20jANGmMBSth%2FJMShQBlyUU8G%20Rj%2FXyyDp%2FJOJ3POn913lZrlbsF3yCUKwQMngffGUFWA27c0BwWkqUsetw4nm1ugG23r0H3zQ7IAVLkOtIyuvhnGH4H1IMx%2FeAK1Dfx0mUtydCFCevDb0VbyLzpCgGyGl1XIDLQ2uVfIOk7RL90iRhIHigcm1CoRGnpO6756fxW9DkzTT%2FJpRkI8LzqYx1KHEO4bdLW0nxHaS7Xud62tFjDBifz5%20B83DUHaIymI6zxtW4bhA%2F4cwPenPho2LdSJsHk2zJ6i9V4Dlh%2FspMGgMIXj1x9wYFgZ6P6cG1XJsv7%2FlMDbdCBWB2T1cv7Uk%20jMkwxrC68OH1Y6vSjLcVeah3j5tkWhavKfk55uoK085VcdTHxk59iQoRg5Limj%20tf286S2JEjTjQMV1iMGzZRhC4ojK%20EQJqR1ZppFLwmDwfOB6v90qd1Ud%2Fl47fUKZgwi%2FjI1yHPyTWkL%20%2FGntZfSXOzDmfZehdjAt4%3D',
    'sec-fetch-site': 'same-site',
    'accept-language': 'zh-CN,zh-Hans;q=0.9',
    'sec-fetch-mode': 'cors',
    'origin': 'https://ghjf.g-town.com.cn',
    'user-agent': 'ICBCiPhone ICBCiPhoneBSNew F-ePass 24.01 ICBCiPhone epassComponentVersion:24.01 iPhone10,1 16.5.1 7A561108-3680-413B-8DA2-110736B60BA6 4G BSComponentVersion:24.01 ADDRs:%E5%8D%97%E4%BA%AC%E5%B8%82:ADDReMozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 F-OFST  elife_moblie_ios  fullversion:6.0.2  BSComponentVersion:5.4 WorkStationChannel:0 isBreak:0  fontsizescale:1 wkwebview:true ICBCiPhoneBSNew 6.0.2 iphone os wkwebview:true',
    'referer': 'https://ghjf.g-town.com.cn/',
    'sec-fetch-dest': 'empty',
}

params = {
    'productId': '7295',
    'path': '54f465abaf33917b2643e5a506c214c3',
}

json_data = {
    'address': 'fb6BVvXNASGGg9+byhOCxumYXwbujnbx73itLEpZ9QwTBoXfVrPKiV9HtgCb/9sX8W71rJ/ySCH8EETLIeXY8ZP6/MY8mmoUuiBz9yND7k5jfQgpq/Ev1Zyu0hj+UThzOcSepj2cB36rxmSSCLbguSUF/IQRLh0kgnlx//K0pFfFcQcAiSqT9HBuyKGjKGHC8V5Dsh+aA+sNrB2DVcxpOKxOqQVESJW1cW/B0SYy8DhRjSktK4eizlOmNQLNH4ksZfF7mTGzRBGluJj33oqrJaDXOvz848Q4KDrt11Lpddw7a1gd+ZkaCG1NUOAPjPy5cfxi5LUf7i5EZTAgKfss972ju4G7R6g+xppxve3JCULMP7HBmXtO2zpGMvHpybNBlkD/lbzeUO8u6tn77eGB5Trp8LgV9dNrvPlqHodVGNPm44bCzTfd71ZJLmNmo3k91tj4yC1aiwaY2pXszTtxWKdUFXBlx6UMFmNfBsfRHTcpQCk6yI+XWWXrqMOFIL6oxoIKlS7XXDm70PK9CHk4z15jDLitmpWa62jm8aRsKFZKSsfqDHI7jYKd+4o/U5Gd',
    'skuCode': 'PB0148870001',
    'skuName': '好想你 大吉大利干果礼盒 1170g 标准:标准',
    'quantity': 1,
    'seckillPoints': 5000,
    'activityId': 1897,
    'productId': 7295,
    'comments': '',
    'goldBeans': 0,
    'elifeVersion': 602,
    'gpsCity': '南京市',
}

response = requests.post(
    'https://ghjf-api.g-town.com.cn/seckill/54f465abaf33917b2643e5a506c214c3',
    params=params,
    headers=headers,
    json=json_data,
)
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"skuCode":"PB0150250001","quantity":1,"goldBeans":0,"address":"fb6BVvXNASGGg9+byhOCxumYXwbujnbx73itLEpZ9QwTBoXfVrPKiV9HtgCb/9sX8W71rJ/ySCH8EETLIeXY8ZP6/MY8mmoUuiBz9yND7k5jfQgpq/Ev1Zyu0hj+UThzOcSepj2cB36rxmSSCLbguSUF/IQRLh0kgnlx//K0pFfFcQcAiSqT9HBuyKGjKGHC8V5Dsh+aA+sNrB2DVcxpOKxOqQVESJW1cW/B0SYy8DhRjSktK4eizlOmNQLNH4ksZfF7mTGzRBGluJj33oqrJaDXOvz848Q4KDrt11Lpddw7a1gd+ZkaCG1NUOAPjPy5cfxi5LUf7i5EZTAgKfss972ju4G7R6g+xppxve3JCULMP7HBmXtO2zpGMvHpybNBlkD/lbzeUO8u6tn77eGB5Trp8LgV9dNrvPlqHodVGNPm44bCzTfd71ZJLmNmo3k91tj4yC1aiwaY2pXszTtxWKdUFXBlx6UMFmNfBsfRHTcpQCk6yI+XWWXrqMOFIL6oxoIKlS7XXDm70PK9CHk4z15jDLitmpWa62jm8aRsKFZKSsfqDHI7jYKd+4o/U5Gd","comments":"","staff":"","coupons":[{"coupon":"GTCD8140030754812023804","useCouponSku":"PB0150250001"}],"elifeVersion":602,"gpsCity":"南京市"}'.encode()
#response = requests.post('https://ghjf-api.g-town.com.cn/order/submission', headers=headers, data=data)response = requests.post('https://ghjf-api.g-town.com.cn/order/submission', headers=headers, json=json_data)
print(response.text)
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"skuCode":"PB0150250001","quantity":1,"goldBeans":0,"address":"fb6BVvXNASGGg9+byhOCxumYXwbujnbx73itLEpZ9QwTBoXfVrPKiV9HtgCb/9sX8W71rJ/ySCH8EETLIeXY8ZP6/MY8mmoUuiBz9yND7k5jfQgpq/Ev1Zyu0hj+UThzOcSepj2cB36rxmSSCLbguSUF/IQRLh0kgnlx//K0pFfFcQcAiSqT9HBuyKGjKGHC8V5Dsh+aA+sNrB2DVcxpOKxOqQVESJW1cW/B0SYy8DhRjSktK4eizlOmNQLNH4ksZfF7mTGzRBGluJj33oqrJaDXOvz848Q4KDrt11Lpddw7a1gd+ZkaCG1NUOAPjPy5cfxi5LUf7i5EZTAgKfss972ju4G7R6g+xppxve3JCULMP7HBmXtO2zpGMvHpybNBlkD/lbzeUO8u6tn77eGB5Trp8LgV9dNrvPlqHodVGNPm44bCzTfd71ZJLmNmo3k91tj4yC1aiwaY2pXszTtxWKdUFXBlx6UMFmNfBsfRHTcpQCk6yI+XWWXrqMOFIL6oxoIKlS7XXDm70PK9CHk4z15jDLitmpWa62jm8aRsKFZKSsfqDHI7jYKd+4o/U5Gd","comments":"","staff":"","coupons":[{"coupon":"GTCD8140030754812023804","useCouponSku":"PB0150250001"}],"elifeVersion":602,"gpsCity":"南京市"}'.encode()
#response = requests.post('https://ghjf-api.g-town.com.cn/order/submission', headers=headers, data=data)