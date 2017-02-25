#! /usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipreacher'


import itchat
import datetime
import time 
import tushare as ts

# 自动登陆微信
def login():
    itchat.auto_login()


def handle(all_list = []):
    stock_symbol_list = []
    price_low_list = []
    price_high_list = []
    for i in range(int(len(all_list) / 3)):
        stock_symbol_list.append(all_list[3 * i])
        price_low_list.append(all_list[3 * i + 1])
        price_high_list.append(all_list[3 * i + 2])
    return stock_symbol_list, price_low_list, price_high_list


def get_push(all_list = []):
    stock_symbol_list, price_low_list, price_high_list = handle(all_list)
    localtime = datetime.datetime.now()    # 获取当前时间
    now = localtime.strftime('%H:%M:%S')
    data = ts.get_realtime_quotes(stock_symbol_list)    # 获取股票信息
    price_list = data['price']
    itchat.send(now, toUserName='filehelper')
    print(now)

    for i in range(int(len(all_list) / 3)):
        content = stock_symbol_list[i] + ' 当前价格为 ' + price_list[i] + '\n'
        if float(price_list[i]) <=  float(price_low_list[i]):
            itchat.send(content + '低于最低预警价格', toUserName='filehelper')
            print(content + '低于最低预警价格')
        elif float(price_list[i]) >=  float(price_high_list[i]):
            itchat.send(content + '高于最高预警价格', toUserName='filehelper')
            print(content + '高于最高预警价格')
        else:
            itchat.send(content + '价格正常', toUserName='filehelper')
            print(content + '价格正常')
    itchat.send('***** end *****', toUserName='filehelper')
    print('***** end *****\n')


def get_remind(all_list = []):
    stock_symbol_list, price_low_list, price_high_list = handle(all_list)
    localtime = datetime.datetime.now()    # 获取当前时间
    now = localtime.strftime('%H:%M:%S')
    data = ts.get_realtime_quotes(stock_symbol_list)    # 获取股票信息
    price_list = data['price']
    itchat.send(now, toUserName='filehelper')
    print(now)

    for i in range(int(len(all_list) / 3)):
        content = stock_symbol_list[i] + ' 当前价格为 ' + price_list[i] + '\n'
        if float(price_list[i]) <=  float(price_low_list[i]):
            itchat.send(content + '低于最低预警价格', toUserName='filehelper')
            print(content + '低于最低预警价格')
        elif float(price_list[i]) >=  float(price_high_list[i]):
            itchat.send(content + '高于最高预警价格', toUserName='filehelper')
            print(content + '高于最高预警价格')
        else:
            print(content + '价格正常')
    itchat.send('***** end *****', toUserName='filehelper')
    print('***** end *****\n')


def push(all_list = []):
    itchat.send('Stock_WeChat 已开始执行！', toUserName='filehelper')
    print('Stock_WeChat 已开始执行！')
    while True:
        try:
            get_push(all_list)
            time.sleep(2.9)
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


def remind(all_list = []):
    itchat.send('Stock_WeChat 已开始执行！', toUserName='filehelper')
    print('Stock_WeChat 已开始执行！')
    while True:
        try:
            get_remind(all_list)
            time.sleep(2.9)
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


