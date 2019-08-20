#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# Created on 2019/8/17/017
# @author: lucklong

from selenium import webdriver
import time
# 加启动配置
option = webdriver.ChromeOptions()

option.add_argument('disable-infobars')
# noption.add_argument('headless')
driver = webdriver.Chrome(chrome_options=option)
driver.maximize_window()
driver.get("https://www.qidian.com/")

driver.find_element_by_id("login-btn").click()

driver.switch_to.frame('loginIfr')
# 使用switch_to.frame 方法切进去frame中

driver.find_element_by_id("username").send_keys("18701685387")
time.sleep(3)
driver.find_element_by_id("password").send_keys("Long19920203")

driver.find_element_by_css_selector('#j-inputMode > div.login-common-wrap > a').click()

driver.switch_to.default_content()
time.sleep(2)
# 切回主文档
driver.find_element_by_id("exit-btn").click()
time.sleep(10)
driver.close()
