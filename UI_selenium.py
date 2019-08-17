#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# Created on 2019/8/17/017
# @author: lucklong

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

driver.close()
