# -*- coding: utf-8 -*-
import json
import codecs
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanSpiderTop250Pipeline(object):
    def __init__(self):
        self.file = codecs.open('douban_movie_top250.json', mode='wb',
                                encoding='utf-8')

    def process_item(self, item, spider):

        line = 'the list:' + '\n'

        for i in range(len(item['quote'])):

            movie_name = {"movie_name": item['movie_name'][i]}
            star = {"star": item['star'][i]}
            quote = {"quote": item['quote'][i]}
            line = line + json.dumps(movie_name, ensure_ascii=False)
            line = line + json.dumps(star, ensure_ascii=False)
            line = line + json.dumps(quote, ensure_ascii=False)
            line += '\n'

        self.file.write(line)

    def close_spider(self, spider):
        self.file.close()
