# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     utils
   Description :
   Author :       201440307129
   date：          2018/4/1
-------------------------------------------------
   Change Activity: 2018/4/1
-------------------------------------------------
"""
import uuid
from datetime import datetime

from pytz import timezone

__author__ = '201440307129'

# 获取当前时间
def getTime():
    ZH = timezone('Asia/Shanghai')
    return datetime.now(ZH)

def getUUID(self):
    s_uuid = str(uuid.uuid5(uuid.uuid4(),''))
    l_uuid = s_uuid.split('-')
    return ''.join(l_uuid)