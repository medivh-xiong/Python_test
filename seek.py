import time

import requests

headers = {
    'Host': 'api.livelab.com.cn',
    'accept': '*/*',
    'content-type': 'application/json',
    'authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9'
                     '.eyJjdCI6MTY3ODA3NDA3Mjg2NiwibWlkIjo1NjQyNSwidHlwZSI6ImFwcGxldCIsImRpZCI6IiJ9'
                     '.h51Jds7gHsUkihDxgh5nHYosm2s2FVqgqD69-MhWBUySoY6kx_2QEojIUXV-dOfJLy1F8m-vxGhxhibZyfgpEA',
    'referer': 'https://servicewechat.com/wx5a8f481d967649eb/53/page-frame.html',
    'accept-language': 'zh-CN,zh-Hans;q=0.9',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                  'Mobile/15E217 MicroMessenger/6.8.0(0x16080000) NetType/WIFI Language/en Branch/Br_trunk '
                  'MiniProgramEnv/Mac',
}

json_data = {
    'contactName': '熊欣',
    'contactPhone': '15951003078',
    'deliveryType': 1,
    'combineTicketVos': [],
    'ordinaryTicketVos': [
        {
            'seatPlanId': 601,
            'seatPlanName': '1280元',
            'seatPlanPrice': 1280,
            'seatPlanQuantity': 1,
            'seatInfoVo': None,
            'frequentContactsId': 61588,
        },
        {
            'seatPlanId': 601,
            'seatPlanName': '1280元',
            'seatPlanPrice': 1280,
            'seatPlanQuantity': 1,
            'seatInfoVo': None,
            'frequentContactsId': 61673,
        },
    ],
    'payment': 2560,
    'totalPrice': 2560,
    'performId': 213,
    'projectId': '124',
    'privilegeCodeList': [],
}


result = True
while result:
    response = requests.post('https://api.livelab.com.cn/order/app/center/v2/create', headers=headers, json=json_data)
    msg = response.text
    print(msg)
    time.sleep(2)
