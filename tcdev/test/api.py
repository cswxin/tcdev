#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

url = "https://api.weixin.qq.com/cgi-bin/component/api_component_token"
data = {
"component_appid": "wxa53b6068be0068ac",
"component_appsecret": "bc7f8fc805a43db69b1a520794425b02",
"component_verify_ticket": "9bf839bc092ea304ec3b808b109f65e5ae4db009" 
}

# AppID: 
# wxa53b6068be0068ac
# AppSecret: 
# bc7f8fc805a43db69b1a520794425b02

# signature=9bf839bc092ea304ec3b808b109f65e5ae4db009
# timestamp=1494341721&
# nonce=1385208597
# encrypt_type=aes
# msg_signature=b1f2e24ace9ce8d2fe9cd6f64527d771dfb96bfe


result = requests.post(url, data)
print result.text
