#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

url = "https://api.weixin.qq.com/cgi-bin/component/api_component_token"
data = '''
<xml>
<AppId>%s</AppId>
<CreateTime>1413192605 </CreateTime>
<InfoType> </InfoType>
<ComponentVerifyTicket> </ComponentVerifyTicket>
</xml>
'''

result = requests.post(url, data).json()
print result
