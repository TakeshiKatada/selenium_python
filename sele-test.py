"""
サイボウズに片田アカウントでログインするプログラム
2019,5,14
Katada-t
"""
# PythonでSeleniumのwebdriverモジュールをインポート
from selenium import webdriver

# 1.操作するブラウザを開く
# /Users/imac2/Desktop/Selenium/chromedriver
driver = webdriver.Chrome('/Users/imac2/Desktop/Selenium/chromedriver')

# 2.操作するページを開く
driver.get('https://hira-print.cybozu.com/login')

# 基本設定はここまで。↑は使い回し可能。ここから下は、やりたい動作によって増える

# 操作する要素を指定
driver.find_element_by_id('username-:0-text')

# その要素を操作する
driver.find_element_by_id('username-:0-text').click()
driver.find_element_by_id('username-:0-text').send_keys("katada-t@hi-ad.jp")

driver.find_element_by_id('password-:1-text')
driver.find_element_by_id('password-:1-text').click()
driver.find_element_by_id('password-:1-text').send_keys("J2dkCEW6")

driver.find_element_by_class_name('login-button')
driver.find_element_by_class_name('login-button').click()