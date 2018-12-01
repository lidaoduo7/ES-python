# -*- coding: utf-8 -*-


'''


'''

from elasticsearch import Elasticsearch
from datetime import datetime

obj = Elasticsearch([{"host": "192.168.100.104", "port": 9200}])    #在ES中配置IP地址
# obj = Elasticsearch([{"host": "localhost", "port": 9200}])

res3 = obj.get(index="my-index3", doc_type="test-type", id=42)['_source']
print(res3)