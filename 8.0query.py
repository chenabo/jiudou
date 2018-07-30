# -*- coding:utf-8 -*-

import time
from selenium import webdriver
import re
import pandas as pd
import xlrd
import datetime
import sys
import random
import math

chromedriver = 'D:/anconda/Scripts/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

def qqb():
    driver.get('http://xr01.18qqb.com/')
    driver.get('http://xr01.18qqb.com/#/auth/sys/xun')
    driver.refresh()
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/span[1]/input').send_keys('zhongshen')
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/span[2]/input').send_keys('123')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/button').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/ul/li[1]/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="32$Menu"]/li[2]').click()
    time.sleep(1)
qqb()
def jj(i):
    print("拒绝")
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/table/tbody/tr[' + str(
            i) + ']/td[2]/span/span[2]/span/a').click()

    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="ZhouqiName"]').send_keys(
        u'以下几种情况无报价：ST股、流通市值过小的股票、次新股、停牌股票、涨停板股票、或者其他券商无报价的股票')  # ：1.询价的名义本金超过该股票市值的5%。2.流通市值小于30亿。3.上市不到370个工作日。4.ST股票，次新股，停牌等不属于可询价的范畴。
    time.sleep(1)
    driver.find_element_by_css_selector(
        'html body div div div.ant-modal-wrap div.ant-modal div.ant-modal-content div.ant-modal-footer button.ant-btn.ant-btn-primary.ant-btn-lg').click()
    time.sleep(1)

def jj2(i):
    print("拒绝")
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/table/tbody/tr[' + str(
            i) + ']/td[2]/span/span[2]/span/a').click()

    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="ZhouqiName"]').send_keys(
        u'请选择正确的期权周期：看涨1个月，看涨3个月，看涨6个月')  # ：1.询价的名义本金超过该股票市值的5%。2.流通市值小于30亿。3.上市不到370个工作日。4.ST股票，次新股，停牌等不属于可询价的范畴。
    time.sleep(1)
    driver.find_element_by_css_selector(
        'html body div div div.ant-modal-wrap div.ant-modal div.ant-modal-content div.ant-modal-footer button.ant-btn.ant-btn-primary.ant-btn-lg').click()
    time.sleep(1)

def jj1(i):
    print("拒绝")
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/table/tbody/tr[' + str(
            i) + ']/td[2]/span/span[2]/span/a').click()

    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="ZhouqiName"]').send_keys(
        u'名义本金需大于等于50万')  # ：1.询价的名义本金超过该股票市值的5%。2.流通市值小于30亿。3.上市不到370个工作日。4.ST股票，次新股，停牌等不属于可询价的范畴。
    time.sleep(1)
    driver.find_element_by_css_selector(
        'html body div div div.ant-modal-wrap div.ant-modal div.ant-modal-content div.ant-modal-footer button.ant-btn.ant-btn-primary.ant-btn-lg').click()
    time.sleep(1)

def jj7(i):
    print("拒绝")
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/table/tbody/tr[' + str(
            i) + ']/td[2]/span/span[2]/span/a').click()

    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="ZhouqiName"]').send_keys(
        u'名义本金需小于等于1000万')  # ：1.询价的名义本金超过该股票市值的5%。2.流通市值小于30亿。3.上市不到370个工作日。4.ST股票，次新股，停牌等不属于可询价的范畴。
    time.sleep(1)
    driver.find_element_by_css_selector(
        'html body div div div.ant-modal-wrap div.ant-modal div.ant-modal-content div.ant-modal-footer button.ant-btn.ant-btn-primary.ant-btn-lg').click()
    time.sleep(1)

def qr(args,i):
    print("确认")
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/table/tbody/tr[' + str(
            i) + ']/td[2]/span/span[1]/span/a'
    ).click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="QuanBili"]').clear()

    print('*' * 100)
    print(args)
    print('*' * 100)

    driver.find_element_by_xpath('//*[@id="QuanBili"]').send_keys(str(args))
    driver.find_element_by_xpath('//*[@id="Zhouqi"]').clear()
    # time.sleep(10)
    driver.find_element_by_xpath('//*[@id="Zhouqi"]').send_keys("1")
    time.sleep(1)
    driver.find_element_by_xpath(
        '/html/body/div[3]/div/div[2]/div/div[1]/div[3]/button[2]').click()
    print("点击确认成功")
    time.sleep(1)

while True:
    try:
        now = datetime.datetime.now()
        print(now.hour)
        if now.hour == 7:
            time.sleep(9900)
        # if now.hour == 1 and now.minute == 1:
        if now.hour == 13:

            driver.refresh()
            time.sleep(2)
            time.sleep(5)
            driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/button[2]').click()
            time.sleep(5)
            driver.get('http://xr01.18qqb.com/')
            driver.get('http://xr01.18qqb.com/')
            driver.refresh()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/span[1]/input').clear()
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/span[1]/input').send_keys('zhongshen')
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/span[2]/input').clear()
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/span[2]/input').send_keys('123')
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/button').click()
            time.sleep(5)
            driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/ul/li[1]/div').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="32$Menu"]/li[2]').click()
            time.sleep(1)
    except Exception as e:
        print(e)
    time.sleep(1)
    driver.refresh()
    time.sleep(1)
    for i in range(1, 5):
        print(i)
        time.sleep(1)
        # 提取询价状态
        status = driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div[2]/table/tbody/tr[' + str(
                i) + ']/td[7]').text
        if status == "询价中":
            # 提取类型
            gplx = driver.find_element_by_xpath(
                '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div[2]/table/tbody/tr[' + str(
                    i) + ']/td[6]').text
            s_id = driver.find_element_by_xpath(
                '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div[2]/table/tbody/tr[' + str(
                    i) + ']/td[4]').text
            s_id = s_id.upper()
            splb = ['CU1810', 'AL1810', 'ZN1810', 'PB1810', 'AU1812', 'AG1812', 'RB1810', 'RU1901', 'SC1809', 'BU1812', 'HC1810','NI1901', 'A1901', 'M1901', 'Y1901', 'P1901', 'C1901', 'I1901', 'JM1901', 'J1901', 'L1901', 'V1901', 'JD1901','PP1901', 'CS1901', 'AP901', 'OI901', 'CF901', 'SR901', 'ZC901', 'TA901', 'FG901', 'MA901', 'RM901', 'SM809','SF809']
            if s_id in splb:
                args = 'D:\\Work\\Option\\sp.xlsx'
                # 实现查询 data_r1 Excel中提取报价
                data = xlrd.open_workbook(args)
                table = data.sheet_by_name(u'Sheet1')
                row = table.nrows
                stkarr = []
                for m in range(row - 1):
                    x = table.row_values(m + 1)
                    stkarr.append(x[0:13])
                stkinfo1 = pd.DataFrame(stkarr,
                                        columns=['id','c1','c2','c4','c12','c26','c52','p1','p2','p4','p12','p26','p52'])
                c1 = stkinfo1[stkinfo1.id == str(s_id)]['c1'].values[0]
                c2 = stkinfo1[stkinfo1.id == str(s_id)]['c2'].values[0]
                c4 = stkinfo1[stkinfo1.id == str(s_id)]['c4'].values[0]
                c12 = stkinfo1[stkinfo1.id == str(s_id)]['c12'].values[0]
                c26 = stkinfo1[stkinfo1.id == str(s_id)]['c26'].values[0]
                c52 = stkinfo1[stkinfo1.id == str(s_id)]['c52'].values[0]
                p1 = stkinfo1[stkinfo1.id == str(s_id)]['p1'].values[0]
                p2 = stkinfo1[stkinfo1.id == str(s_id)]['p2'].values[0]
                p4 = stkinfo1[stkinfo1.id == str(s_id)]['p4'].values[0]
                p12 = stkinfo1[stkinfo1.id == str(s_id)]['p12'].values[0]
                p26 = stkinfo1[stkinfo1.id == str(s_id)]['p26'].values[0]
                p52 = stkinfo1[stkinfo1.id == str(s_id)]['p52'].values[0]
                print(c1,c2,c4,c12,c26,c52,p1,p2,p4,p12,p26,p52)
                # 期权类型
                typex = driver.find_element_by_xpath(
                    '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div[2]/table/tbody/tr[' + str(
                        i) + ']/td[9]').text
                if typex == '看涨2周':
                    qr(c2, i)
                elif typex == '看涨1个月':
                    qr(c4, i)
                elif typex == '看涨3个月':
                    qr(c12, i)
                elif typex == '看涨6个月':
                    qr(c26, i)
                elif typex == '看跌2周':
                    qr(p2, i)
                elif typex == '看跌1个月':
                    qr(p4, i)
                elif typex == '看跌3个月':
                    qr(p12, i)
                elif typex == '看跌6个月':
                    qr(p26, i)
                else:
                    jj(i)





            if gplx == 'A股':
                # 获取平台名字//*[@id="root"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div[2]/table/tbody/tr[4]/td[23]
                platform = driver.find_element_by_xpath(
                    '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div[2]/table/tbody/tr[' + str(
                        i) + ']/td[23]').text
                # 获取股票代码
                s_id = driver.find_element_by_xpath(
                    '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div[2]/table/tbody/tr[' + str(
                        i) + ']/td[4]').text
                s_id = s_id.upper()
                # 期权类型
                typex = driver.find_element_by_xpath(
                    '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div[2]/table/tbody/tr[' + str(
                        i) + ']/td[9]').text
                # 名义本金
                mybj = driver.find_element_by_xpath(
                    '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div[2]/table/tbody/tr[' + str(
                        i) + ']/td[11]').text
                mybj = re.findall(r'\d*', mybj)[0]
                mybj = float(mybj)
                # print(platform,s_id,typex,mybj)
                if typex == '看涨1个月':
                    args = 'D:\\Work\\Option\\data_r1.xlsx'
                    # 实现查询 data_r1 Excel中提取报价
                    data = xlrd.open_workbook(args)
                    table = data.sheet_by_name(u'Sheet1')
                    row = table.nrows
                    stkarr = []
                    for m in range(row - 1):
                        x = table.row_values(m + 1)
                        stkarr.append(x[0:17])
                    stkinfo1 = pd.DataFrame(stkarr,
                                            columns=['id', 'name', 'amt_a', 'rate_a', 'qs_a', 'amt_b', 'rate_b', 'qs_b',
                                                     'amt_c', 'rate_c', 'qs_c', 'amt_d', 'rate_d', 'qs_d', 'amt_e',
                                                     'rate_e', 'qs_e'])

                    # print(type(stkinfo1[stkinfo1.id == str(id)]['amt_a']))

                    amt_a = float(stkinfo1[stkinfo1.id == str(s_id)]['amt_a'])


                    rate_a = float(stkinfo1[stkinfo1.id == str(s_id)]['rate_a'])
                    amt_b = float(stkinfo1[stkinfo1.id == str(s_id)]['amt_b'])
                    rate_b = float(stkinfo1[stkinfo1.id == str(s_id)]['rate_b'])
                    amt_c = float(stkinfo1[stkinfo1.id == str(s_id)]['amt_c'])
                    rate_c = float(stkinfo1[stkinfo1.id == str(s_id)]['rate_c'])
                    amt_d = float(stkinfo1[stkinfo1.id == str(s_id)]['amt_d'])
                    rate_d = float(stkinfo1[stkinfo1.id == str(s_id)]['rate_d'])
                    amt_e = float(stkinfo1[stkinfo1.id == str(s_id)]['amt_e'])
                    rate_e = float(stkinfo1[stkinfo1.id == str(s_id)]['rate_e'])

                    qs_a = str(stkinfo1[stkinfo1.id == str(s_id)]['qs_a'].values[0])
                    qs_b = str(stkinfo1[stkinfo1.id == str(s_id)]['qs_b'].values[0])
                    qs_c = str(stkinfo1[stkinfo1.id == str(s_id)]['qs_c'].values[0])
                    qs_d = str(stkinfo1[stkinfo1.id == str(s_id)]['qs_d'].values[0])
                    qs_e = str(stkinfo1[stkinfo1.id == str(s_id)]['qs_e'].values[0])
                    rate_a1 = rate_a
                    rate_b1 = rate_b
                    rate_c1 = rate_c
                    rate_d1 = rate_d
                    rate_e1 = rate_e
                elif typex == '看涨3个月':
                    args = 'D:\\Work\\Option\\data_r3.xlsx'
                    # 实现查询 data_r1 Excel中提取报价
                    data = xlrd.open_workbook(args)
                    table = data.sheet_by_name(u'Sheet1')
                    row = table.nrows
                    stkarr = []
                    for m in range(row - 1):
                        x = table.row_values(m + 1)
                        stkarr.append(x[0:17])
                    stkinfo1 = pd.DataFrame(stkarr,
                                            columns=['id', 'name', 'amt_a', 'rate_a', 'qs_a', 'amt_b', 'rate_b', 'qs_b',
                                                     'amt_c', 'rate_c', 'qs_c', 'amt_d', 'rate_d', 'qs_d', 'amt_e',
                                                     'rate_e', 'qs_e'])
                    amt_a = float(stkinfo1[stkinfo1.id == str(s_id)]['amt_a'])
                    rate_a = float(stkinfo1[stkinfo1.id == str(s_id)]['rate_a'])
                    amt_b = float(stkinfo1[stkinfo1.id == str(s_id)]['amt_b'])
                    rate_b = float(stkinfo1[stkinfo1.id == str(s_id)]['rate_b'])
                    amt_c = float(stkinfo1[stkinfo1.id == str(s_id)]['amt_c'])
                    rate_c = float(stkinfo1[stkinfo1.id == str(s_id)]['rate_c'])
                    amt_d = float(stkinfo1[stkinfo1.id == str(s_id)]['amt_d'])
                    rate_d = float(stkinfo1[stkinfo1.id == str(s_id)]['rate_d'])
                    amt_e = float(stkinfo1[stkinfo1.id == str(s_id)]['amt_e'])
                    rate_e = float(stkinfo1[stkinfo1.id == str(s_id)]['rate_e'])
                    qs_a = str(stkinfo1[stkinfo1.id == str(s_id)]['qs_a'].values[0])
                    qs_b = str(stkinfo1[stkinfo1.id == str(s_id)]['qs_b'].values[0])
                    qs_c = str(stkinfo1[stkinfo1.id == str(s_id)]['qs_c'].values[0])
                    qs_d = str(stkinfo1[stkinfo1.id == str(s_id)]['qs_d'].values[0])
                    qs_e = str(stkinfo1[stkinfo1.id == str(s_id)]['qs_e'].values[0])
                    rate_a1 = rate_a
                    rate_b1 = rate_b
                    rate_c1 = rate_c
                    rate_d1 = rate_d
                    rate_e1 = rate_e
                elif typex == '看涨6个月':
                    args = 'D:\\Work\\Option\\data_r6.xlsx'
                    # 实现查询 data_r1 Excel中提取报价
                    data = xlrd.open_workbook(args)
                    table = data.sheet_by_name(u'Sheet1')
                    row = table.nrows
                    stkarr = []
                    for m in range(row - 1):
                        x = table.row_values(m + 1)
                        stkarr.append(x[0:17])
                    stkinfo1 = pd.DataFrame(stkarr,
                                            columns=['id', 'name', 'amt_a', 'rate_a', 'qs_a', 'amt_b', 'rate_b', 'qs_b',
                                                     'amt_c', 'rate_c', 'qs_c', 'amt_d', 'rate_d', 'qs_d', 'amt_e',
                                                     'rate_e', 'qs_e'])
                    amt_a = float(stkinfo1[stkinfo1.id == str(s_id)]['amt_a'])
                    rate_a = float(stkinfo1[stkinfo1.id == str(s_id)]['rate_a'])
                    amt_b = float(stkinfo1[stkinfo1.id == str(s_id)]['amt_b'])
                    rate_b = float(stkinfo1[stkinfo1.id == str(s_id)]['rate_b'])
                    amt_c = float(stkinfo1[stkinfo1.id == str(s_id)]['amt_c'])
                    rate_c = float(stkinfo1[stkinfo1.id == str(s_id)]['rate_c'])
                    amt_d = float(stkinfo1[stkinfo1.id == str(s_id)]['amt_d'])
                    rate_d = float(stkinfo1[stkinfo1.id == str(s_id)]['rate_d'])
                    amt_e = float(stkinfo1[stkinfo1.id == str(s_id)]['amt_e'])
                    rate_e = float(stkinfo1[stkinfo1.id == str(s_id)]['rate_e'])
                    qs_a = str(stkinfo1[stkinfo1.id == str(s_id)]['qs_a'].values[0])
                    qs_b = str(stkinfo1[stkinfo1.id == str(s_id)]['qs_b'].values[0])
                    qs_c = str(stkinfo1[stkinfo1.id == str(s_id)]['qs_c'].values[0])
                    qs_d = str(stkinfo1[stkinfo1.id == str(s_id)]['qs_d'].values[0])
                    qs_e = str(stkinfo1[stkinfo1.id == str(s_id)]['qs_e'].values[0])
                    rate_a1 = rate_a
                    rate_b1 = rate_b
                    rate_c1 = rate_c
                    rate_d1 = rate_d
                    rate_e1 = rate_e
                elif typex == '看涨2周':
                    args = 'D:\\Work\\Option\\data_r0.xlsx'
                    # 实现查询 data_r1 Excel中提取报价
                    data = xlrd.open_workbook(args)
                    table = data.sheet_by_name(u'Sheet1')
                    row = table.nrows
                    stkarr = []
                    for m in range(row - 1):
                        x = table.row_values(m + 1)
                        stkarr.append(x[0:17])
                    stkinfo1 = pd.DataFrame(stkarr,
                                            columns=['id', 'name', 'amt_a', 'rate_a', 'qs_a', 'amt_b', 'rate_b', 'qs_b',
                                                     'amt_c', 'rate_c', 'qs_c', 'amt_d', 'rate_d', 'qs_d', 'amt_e',
                                                     'rate_e', 'qs_e'])
                    amt_a = float(stkinfo1[stkinfo1.id == str(s_id)]['amt_a'])
                    rate_a = float(stkinfo1[stkinfo1.id == str(s_id)]['rate_a'])
                    amt_b = float(stkinfo1[stkinfo1.id == str(s_id)]['amt_b'])
                    rate_b = float(stkinfo1[stkinfo1.id == str(s_id)]['rate_b'])
                    amt_c = float(stkinfo1[stkinfo1.id == str(s_id)]['amt_c'])
                    rate_c = float(stkinfo1[stkinfo1.id == str(s_id)]['rate_c'])
                    amt_d = float(stkinfo1[stkinfo1.id == str(s_id)]['amt_d'])
                    rate_d = float(stkinfo1[stkinfo1.id == str(s_id)]['rate_d'])
                    amt_e = float(stkinfo1[stkinfo1.id == str(s_id)]['amt_e'])
                    rate_e = float(stkinfo1[stkinfo1.id == str(s_id)]['rate_e'])
                    qs_a = str(stkinfo1[stkinfo1.id == str(s_id)]['qs_a'].values[0])
                    qs_b = str(stkinfo1[stkinfo1.id == str(s_id)]['qs_b'].values[0])
                    qs_c = str(stkinfo1[stkinfo1.id == str(s_id)]['qs_c'].values[0])
                    qs_d = str(stkinfo1[stkinfo1.id == str(s_id)]['qs_d'].values[0])
                    qs_e = str(stkinfo1[stkinfo1.id == str(s_id)]['qs_e'].values[0])
                    rate_a1 = rate_a
                    rate_b1 = rate_b
                    rate_c1 = rate_c
                    rate_d1 = rate_d
                    rate_e1 = rate_e
                s = r'1.xls'
                data1 = xlrd.open_workbook(s, formatting_info=True)
                table1 = data1.sheet_by_name(u'info')
                row1 = table1.nrows
                stkarr1 = []
                for mm in range(row1 - 1):
                    x = table1.row_values(mm + 1)
                    stkarr1.append(x[0:6])
                stkinfo2 = pd.DataFrame(stkarr1, columns=['id', 'zz', 'sw', 'sw2', 'sw22', 'sw23'])
                if platform == "vip001":
                    print('18中投宝')
                    if mybj >= 100:
                        rate_a = rate_a* 2.1
                    if mybj < 100:
                        rate_a = rate_a* 2.2
                    if mybj >= 100:
                        rate_b = rate_b* 2.1
                    if mybj < 100:
                        rate_b = rate_b* 2.2
                    if mybj >= 100:
                        rate_c = rate_c* 2.1
                    if mybj < 100:
                        rate_c = rate_c* 2.2
                    if mybj >= 100:
                        rate_d = rate_d* 2.1
                    if mybj < 100:
                        rate_d = rate_d* 2.2
                    if mybj >= 100:
                        rate_e = rate_e* 2.1
                    if mybj < 100:
                        rate_e = rate_e* 2.2
                    if rate_a < 10:
                        rate_a = round(random.uniform(10.01,10.05), 2)
                    elif rate_b < 10:
                        rate_b = round(random.uniform(10.01,10.05), 2)
                    elif rate_c < 10:
                        rate_c = round(random.uniform(10.01,10.05), 2)
                    elif rate_d < 10:
                        rate_d = round(random.uniform(10.01,10.05), 2)
                    elif rate_e < 10:
                        rate_e = round(random.uniform(10.01,10.05), 2)
                    asd = ['SZ002154','SZ000810','SH601006','SH600565','SZ000413','SZ000040','SH600563','SH601901','SZ300398','SZ002027',
                           'SZ000516','SZ002465','SZ002185','SH600984','SZ000656','SH600495','SH600572','SZ002422','SZ000513','SZ002601',
                           'SZ002671','SH600600','SZ300214','SZ300408','SH600409','SZ002563','SH601229','SZ000681','SZ000025','SZ002709',
                           'SH600330','SH600867','SZ000785','SH600803','SZ002727','SZ000539','SZ000519','SH600329','SH600020','SH601618',
                           'SZ002807','SZ002839','SH601186','SZ002434','SZ002242']
                    if typex == '看涨2周':
                        print(id)
                        jj2(i)
                    else:
                        if mybj < 50:
                            print(id)
                            jj1(i)
                        elif str(s_id) in asd:
                            print('50支票的报价')
                            if mybj > 1000:
                                jj7(i)
                            if mybj <= 1000:
                                if typex == '看涨1个月':
                                    args = 'D:\\Work\\Option\\Rate_QS\\50zp.xlsx'
                                    data = xlrd.open_workbook(args)
                                    table = data.sheet_by_name(u'Sheet1')
                                    row = table.nrows
                                    stkarr = []
                                    for m in range(row - 1):
                                        x = table.row_values(m + 1)
                                        stkarr.append(x[0:4])
                                    stkinfo1 = pd.DataFrame(stkarr,
                                                            columns=['id', 'name', '100W', '50W'])
                                    amt = float(stkinfo1[stkinfo1.id == str(s_id)]['100W'].values[0])

                                    if mybj >= 100:
                                        rate_a1 = amt
                                    if mybj < 100:
                                        rate_a1 = amt+0.5
                                    rate_a1 = math.ceil(rate_a1 * 100) / 100
                                    qr(rate_a1,i)
                                elif typex != '看涨1个月':
                                    if amt_a >= (float(stkinfo2[stkinfo2.id == str(s_id)][qs_a]) + mybj):
                                        if rate_a < 10000:
                                            rate_a = math.ceil(rate_a * 100) / 100
                                            qr(rate_a,i)
                                        else:
                                            jj(i)
                                    elif amt_b >= (float(stkinfo2[stkinfo2.id == str(s_id)][qs_b]) + mybj):
                                        if rate_b < 10000:
                                            rate_b = math.ceil(rate_b * 100) / 100
                                            qr(rate_b,i)
                                        else:
                                            jj(i)
                                    elif amt_c >= (float(stkinfo2[stkinfo2.id == str(s_id)][qs_c]) + mybj):
                                        if rate_c < 10000:
                                            rate_c = math.ceil(rate_c * 100) / 100
                                            qr(rate_c,i)
                                        else:
                                            jj(i)
                                    elif amt_d >= (float(stkinfo2[stkinfo2.id == str(s_id)][qs_d]) + mybj):
                                        if rate_d < 10000:
                                            rate_d = math.ceil(rate_d * 100) / 100
                                            qr(rate_d,i)
                                        else:
                                            jj(i)
                                    elif amt_e >= (float(stkinfo2[stkinfo2.id == str(s_id)][qs_e]) + mybj):
                                        if rate_e < 10000:
                                            rate_e = math.ceil(rate_e * 100) / 100
                                            qr(rate_e,i)
                                        else:
                                            jj(i)
                        elif mybj >= 50 and str(s_id) not in asd:
                            if amt_a >= (float(stkinfo2[stkinfo2.id == str(s_id)][qs_a])+mybj):
                                if rate_a < 10000:
                                    if typex == '看涨1个月':
                                        if 18 > rate_a >= 10.01:
                                            print('/'*100)
                                            rate_a = math.ceil(rate_a*100)/100
                                            qr(rate_a,i)
                                        else:
                                            jj(i)
                                    else:
                                        rate_a = math.ceil(rate_a * 100) / 100
                                        qr(rate_a,i)
                                else:
                                    jj(i)
                            elif amt_b >= (float(stkinfo2[stkinfo2.id == str(s_id)][qs_b])+mybj):
                                if rate_b < 10000:
                                    if typex == '看涨1个月':
                                        if 18 > rate_b >= 10.01:
                                            print('/'*100)
                                            rate_b = math.ceil(rate_b*100)/100
                                            qr(rate_b,i)
                                        else:
                                            jj(i)
                                    else:
                                        rate_b = math.ceil(rate_b * 100) / 100
                                        qr(rate_b,i)
                                else:
                                    jj(i)
                            elif amt_c >= (float(stkinfo2[stkinfo2.id == str(s_id)][qs_c]) + mybj):
                                if rate_c < 10000:
                                    if typex == '看涨1个月':
                                        if 18 > rate_c >= 10.01:
                                            print('/'*100)
                                            rate_c = math.ceil(rate_c*100)/100
                                            qr(rate_c,i)
                                        else:
                                            jj(i)
                                    else:
                                        rate_c = math.ceil(rate_c * 100) / 100
                                        qr(rate_c,i)
                                else:
                                    jj(i)
                            elif amt_d >= (float(stkinfo2[stkinfo2.id == str(s_id)][qs_d]) + mybj):
                                if rate_d < 10000:
                                    if typex == '看涨1个月':
                                        if 18 > rate_d >= 10.01:
                                            print('/'*100)
                                            rate_d = math.ceil(rate_d*100)/100
                                            qr(rate_d,i)
                                        else:
                                            jj(i)
                                    else:
                                        rate_d = math.ceil(rate_d * 100) / 100
                                        qr(rate_d,i)
                                else:
                                    jj(i)
                            elif amt_e >= (float(stkinfo2[stkinfo2.id == str(s_id)][qs_e]) + mybj):
                                if rate_e < 10000:
                                    if typex == '看涨1个月':
                                        if 18 > rate_e >= 10.01:
                                            print('/'*100)
                                            rate_e = math.ceil(rate_e*100)/100
                                            qr(rate_e,i)
                                        else:
                                            jj(i)
                                    else:
                                        rate_e = math.ceil(rate_e * 100) / 100
                                        qr(rate_e,i)
                                else:
                                    jj(i)
                            else:
                                jj(i)


