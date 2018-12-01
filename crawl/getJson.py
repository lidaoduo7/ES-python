# -*- coding: utf-8 -*-

'''
获取json数据，尝试写入ES中
https://mp.weixin.qq.com/s/mTxxkwRZPgBiKC3Sv-jo3g

从移动端抓包找到评论接口（怎么做的？）


'''

import requests
import json



url = "http://m.maoyan.com/mmdb/comments/movie/42964.json?v=yes&offset=15&startTime=2018-11-20%2019%3A17%3A16"
header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0' }
html=requests.get(url,headers=header)
result = html.content.decode('utf8')
# print(result)
dictinfo = json.loads(result)  # 字符串转换成字典

total = dictinfo['total']
print(total)