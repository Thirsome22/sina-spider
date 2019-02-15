# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     cookies
   Description :
   Author :       201440307129
   date：          2017/12/2
-------------------------------------------------
   Change Activity: 2017/12/2
-------------------------------------------------
"""
__author__ = '201440307129'

from selenium import webdriver
import time

# chromedriver
chromepath = 'chromedriver.exe'

myWeiBo = [
    {'account':'13216294244','password':'asd21111'},
]

'''
登陆账号获取cookies
使用selenium，先调用chrome浏览器
最后改成PhantomJS
'''
def getCookies(weibo):
    url = 'https://passport.weibo.cn/signin/login'
    print("Start crawl cookies!!!!")
    cookies = []
    # cookies = ['_T_WM=89d51dbb9802c590cafef269c94b44ca; SCF=As865Xxdyv4sT4AO5L3ydl1A-se4Rks0zKfvH5yexLNFtVoZiYHqVqvyVGeurLLT82b3Ciz6O7uFll9kUg4l7zI.; H5_INDEX_TITLE=%E5%B1%80%E9%95%BF%E5%88%AB%E5%BC%80%E6%9E%AA%E6%98%AF%E6%88%91; H5_INDEX=3; SUB=_2A253tIN_DeRhGeNL41MV-C7NyTuIHXVVVi03rDV6PUJbkdANLUb6kW1NSMqDkp4eriOfoOpHkRHNBIVcTjxLs4pU; SUHB=05i6yxP7A6_5PX; SSOLoginState=1521546031']
    for ele in weibo:
        account = ele['account']
        password = ele['password']
        # print(account,password)
        try:
            options = webdriver.ChromeOptions()
            #options.add_experimental_option("excludeSwitches", ["--ignore-certificate-errors"])
            driver = webdriver.Chrome(executable_path=chromepath,chrome_options=options)
            driver.get(url=url)
            time.sleep(2)

            failure = 0
            while "登录 - 新浪微博" in driver.title and failure < 5:
                failure+=1
                # loginName
                username = driver.find_element_by_id("loginName")
                username.send_keys(account)

                # loginPassword
                psd = driver.find_element_by_id("loginPassword")
                psd.clear()
                psd.send_keys(password)

                commit = driver.find_element_by_id('loginAction')
                commit.click()


                time.sleep(40)
                # print(driver.get_cookie())
                cookie = {}
                if "微博 - 随时随地发现新鲜事" in driver.title:
                    # driver.get_cookies（） 获得cookie信息
                    for elem in driver.get_cookies():
                        cookie[elem['name']] = elem['value']
                        if len(cookie)>0:
                            cookies.append(cookie)
                            print("Get Cookie Successful: %s!!!!!!"%account)
        except Exception as e:
            print("%s Failure!!!!!" % account)
            print(e)
            pass
        finally:
            try:
                driver.quit()
            except Exception as e:
                pass
    return cookies

cookies = getCookies(myWeiBo)

