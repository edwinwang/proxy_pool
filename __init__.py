# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__.py  
   Description :  
   Author :       JHao
   date：          2016/12/3
-------------------------------------------------
   Change Activity:
                   2016/12/3: 
-------------------------------------------------
"""
__author__ = 'JHao'

import sys
from multiprocessing import Process


sys.path.append('./')

from Api.ProxyApi import run as ProxyApiRun
from Schedule.ProxyValidSchedule import run as ValidRun
from Schedule.ProxyRefreshSchedule import run as RefreshRun


def run():
    p_list = list()
    p1 = Process(target=ProxyApiRun, name='ProxyApiRun')
    p_list.append(p1)
    p2 = Process(target=ValidRun, name='ValidRun')
    p_list.append(p2)
    p3 = Process(target=RefreshRun, name='RefreshRun')
    p_list.append(p3)

    for p in p_list:
        p.start()
    for p in p_list:
        p.join()