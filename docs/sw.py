#! /usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipreacher'


import itchat
import datetime
import time as t
import tushare as ts


stock_symbol = str()
price_low = float()
price_high = float()


# 登陆微信
def login():
    itchat.auto_login()


# 每 3 秒推送一次
def push(stock_symbol, price_low, price_high):
    while True:   
        try:   
            time = datetime.datetime.now()    # 获取当前时间
            now = time.strftime('%H:%M:%S') 
            data = ts.get_realtime_quotes(stock_symbol)    # 获取股票信息
            r1 = float(data['price'])
            r2 = str(stock_symbol) + ' 的当前价格为 ' + str(r1)
            content = now + '\n' + r2
            itchat.send(content, toUserName='filehelper')
            print(content)
            # 判断并发送预警信息
            if r1 <= float(price_low):
                itchat.send('低于最低预警价格', toUserName='filehelper')
                print('低于最低预警价格')
            elif r1 >= float(price_high):
                itchat.send('高于最高预警价格', toUserName='filehelper')
                print('高于最高预警价格')
            else:
                itchat.send('价格正常', toUserName='filehelper')
                print('价格正常')
            t.sleep(2.9)
        except KeyboardInterrupt:
            itchat.send('Stock_WeChat 已执行完毕！\n'
                '更多有意思的小玩意，请戳---->\n'
                '[https://github.com/ipreacher/tricks]', 
                toUserName='filehelper')
            print('\n'
                'Stock_WeChat 已执行完毕！\n'
                '更多有意思的小玩意，请戳---->\n'
                '[https://github.com/ipreacher/tricks]')
            break


# 超过预警价格发送提示
def remind(stock_symbol, price_low, price_high):
    while True:   
        try:   
            time = datetime.datetime.now()    # 获取当前时间
            now = time.strftime('%H:%M:%S') 
            data = ts.get_realtime_quotes(stock_symbol)    # 获取股票信息
            r1 = float(data['price'])
            r2 = str(stock_symbol) + ' 的当前价格为 ' + str(r1)
            content = now + '\n' + r2
            print(content)
            # 判断并发送预警信息
            if r1 <= float(price_low):
                itchat.send('低于最低预警价格', toUserName='filehelper')
                print('低于最低预警价格')
            elif r1 >= float(price_high):
                itchat.send('高于最高预警价格', toUserName='filehelper')
                print('高于最高预警价格')
            else:
                print('价格正常')
            t.sleep(2.9)
        except KeyboardInterrupt:
            itchat.send('Stock_WeChat 已执行完毕！\n'
                '更多有意思的小玩意，请戳---->\n'
                '[https://github.com/ipreacher/tricks]', 
                toUserName='filehelper')
            print('\n'
                'Stock_WeChat 已执行完毕！\n'
                '更多有意思的小玩意，请戳---->\n'
                '[https://github.com/ipreacher/tricks]')
            break




