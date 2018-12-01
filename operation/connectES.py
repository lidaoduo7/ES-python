# -*- coding: utf-8 -*-

'''
参考：https://pypi.org/project/elasticsearch/
'''

from datetime import datetime
from elasticsearch import Elasticsearch

# 连接ES集群
# by default we connect to localhost:9200
es = Elasticsearch()

# 创建索引
# create an index in elasticsearch, ignore status code 400 (index already exists)
# res = es.indices.create(index='my-index2', ignore=400)
# print(res)

# 创建索引、类型、文档
# datetimes will be serialized
# res2 = es.index(index="my-index3", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})
# print(res2)

# 获取文档
# but not deserialized
res3 = es.get(index="my-index3", doc_type="test-type", id=42)['_source']
print(res3)

