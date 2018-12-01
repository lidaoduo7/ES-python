# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 22:57
# @Author  : liduo
# @Email   : 
# @File    : jiebaDemo.py
# @Software: PyCharm

import jieba

comments = []
comments.append("看观众分布无法判断大家对电影的喜好，所以我把通过jieba把评论分词")
comments.append("最后通过wordcloud制作词云，作为大众对该电影的综合评价")

seg_list = jieba.cut(str(comments), cut_all=False)
print(','.join(seg_list))