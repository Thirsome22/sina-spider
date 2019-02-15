# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     launch
   Description :
   Author :       201440307129
   date：          2018/4/1
-------------------------------------------------
   Change Activity: 2018/4/1
-------------------------------------------------
"""
__author__ = '201440307129'

from scrapy import cmdline
if __name__ == '__main__':
    cmdline.execute("scrapy crawl weibo_keyword".split())