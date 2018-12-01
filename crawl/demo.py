# -*- coding: utf-8 -*-

'''
参考
https://mp.weixin.qq.com/s/mTxxkwRZPgBiKC3Sv-jo3g
'''

import requests
import json
import time
from datetime import datetime,timedelta
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

def get_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
    }
    html = requests.get(url, headers=headers)
    if html.status_code == 200:
        return html.content
    else:
        return None


'''
解析Json数据，
每个接口有15条评论数据cmts，10条热门评论数据hcmts，
将评论数据中用户名、城市名、评论内容、评分、评论时间依次解析出来，并返回 字典列表
'''
def parse_data(html):
    json_data = json.loads(html)['cmts']
    comments = []
    try:
        for item in json_data:
            comment = {
                'nickName': item['nickName'],
                'cityName': item['cityName'] if 'cityName' in item else '',
                'content': item['content'].strip().replace('\n', ''),
                'score': item['score'],
                'startTime': item['startTime']
            }
            comments.append(comment)
        return comments
    except Exception as e:
        print(e)



'''
将获取到的数据保存到本地。
此过程中，对接口url中时间的处理借鉴了其他博主的爬虫思路，将每次爬取的15条数据取最后一条的评论时间，减去一秒（防止重复），从该时间向前获取直到影片上映时间，获取所有数据
'''
def save():
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    end_time = '2018-11-09 00:00:00'
    while start_time > end_time:
        url = 'http://m.maoyan.com/mmdb/comments/movie/42964.json?_v_=yes&offset=15&startTime=' + start_time.replace(
            ' ', '%20')
        html = None
        try:
            html = get_data(url)
        except Exception as e:
            time.sleep(0.5)
            html = get_data(url)
        else:
            time.sleep(0.1)
        comments =parse_data(html)
        start_time = comments[14]['startTime']
        print(start_time)
        start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S') + timedelta(seconds=-1)
        start_time = datetime.strftime(start_time, '%Y-%m-%d %H:%M:%S')
        for item in comments:
            print(item)
            with open('files/comments.txt', 'a', encoding='utf-8')as f:
                f.write(item['nickName']+','+item['cityName'] +','+item['content']+','+str(item['score'])+ item['startTime'] + '\n')

'''
用户评论，词云图
只看观众分布无法判断大家对电影的喜好，所以我通过jieba把评论分词，最后通过wordcloud制作词云，作为大众对该电影的综合评价
'''
def word_cloud_show():
    comments = []
    with open('files/comments.txt', 'r', encoding='utf-8')as f:
        rows = f.readlines()
        try:
            for row in rows:
                comment = row.split(',')[2]
                if comment != '':
                    comments.append(comment)
                # print(city)
        except Exception as e:
            print(e)
    comment_after_split = jieba.cut(str(comments), cut_all=False)
    words = ' '.join(comment_after_split)
    # 多虑没用的停止词
    stopwords = STOPWORDS.copy()
    stopwords.add('电影')
    stopwords.add('一部')
    stopwords.add('一个')
    stopwords.add('没有')
    stopwords.add('什么')
    stopwords.add('有点')
    stopwords.add('感觉')
    stopwords.add('毒液')
    stopwords.add('就是')
    stopwords.add('觉得')
    bg_image = plt.imread('love.jpg')    #背景图片
    wc = WordCloud(width=1024, height=768, background_color='white', mask=bg_image, font_path='STKAITI.TTF',
                   stopwords=stopwords, max_font_size=400, random_state=50)
    wc.generate_from_text(words)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()



if __name__ == '__main__':
    print("It's in main!")

    # url = 'http://m.maoyan.com/mmdb/comments/movie/42964.json?v=yes&offset=15&startTime=2018-11-20%2019%3A17%3A16'
    # html = get_data(url)
    # print(html)

    # save()

    # word_cloud_show()

