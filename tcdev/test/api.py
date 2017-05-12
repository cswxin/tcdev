#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

appid = "wxa53b6068be0068ac"

# url = "https://api.weixin.qq.com/cgi-bin/component/api_component_token"
# data = {
# "component_appid": appid,
# "component_appsecret": "f116e87b7951a11942d1e841e36ef16b",
# "component_verify_ticket": "ticket@@@3q3eQyWEjZehQ13sfMFCsexZ408aSDF2PLQ1bLLfwVMJLv7M0bpPGkyBQPwM8DI0Hf3IQd8R4pS5wjWmF14pAg" 
# }
# 
# 
# result = requests.post(url, json=data).json()
# print result

component_access_token = 'vWvb5cjfNcso9Xt0U3UG30O4GsA_zHccbQ8VauKU1N9modrUof3rpsEU0hPIioeWywmdLgmDe37ZWG-DyZYKfway6ak0dj3ZwB_a1vG12ynIZQZjkieZCcYAFaTnJJgIZEJjADAMRW'
url = "https://api.weixin.qq.com/cgi-bin/component/api_create_preauthcode?component_access_token=%s"%component_access_token
data = {
"component_appid": appid
}
result = requests.post(url, json=data).json()
print result

'pre_auth_code' = 'preauthcode@@@E6AvQW83CQwgV_vEFY6XF5FZP3OdmacABBUktsbP9t_yTtPdyRiAByGcJRBnzzGG'

https://mp.weixin.qq.com/cgi-bin/componentloginpage?component_appid=wxa53b6068be0068ac&pre_auth_code=E6AvQW83CQwgV_vEFY6XF5FZP3OdmacABBUktsbP9t_yTtPdyRiAByGcJRBnzzGG&redirect_uri=preauthcode@@@E6AvQW83CQwgV_vEFY6XF5FZP3OdmacABBUktsbP9t_yTtPdyRiAByGcJRBnzzGG&redirect_uri=http%3A%2F%2F119.23.53.19
