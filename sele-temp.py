# PythonでSeleniumのwebdriverモジュールをインポート
from selenium import webdriver

# 1.操作するブラウザを開く
# /Users/imac2/Desktop/Selenium/chromedriver
driver = webdriver.Chrome('WebDriverを格納しているディレクトリを指定')

# 2.操作するページを開く
driver.get('URL')

# 基本設定はここまで。↑は使い回し可能。ここから下は、やりたい動作によって増える

# 3.操作する要素を指定

# id属性で指定する
driver.find_element_by_id('ID')
# class属性で指定する
driver.find_element_by_class_name('CLASS_NAME')
# name属性で指定する
driver.find_element_by_name('NAME')
# CSSセレクタで指定する
driver.find_elements_by_css_selector('CSSセレクタ')
# XPathで指定する
driver.find_elements_by_xpath('XPath')
# 完全一致のリンクテキスト
driver.find_elements_by_link_text('リンクテキスト')
# 部分一致のリンクテキスト
driver.find_elements_by_partial_link_text('リンクテキスト')

# 4.その要素を操作する

# クリックする１
driver.find_element_by_id('ID').click()
# クリックする２
# 『.click()』で何故かクリックできないときは、JavaScriptで無理やりクリックさせます。
element = driver.find_element_by_id('ID')
driver.execute_script("arguments[0].click();", element)
# テキストを入力する
driver.find_element_by_id('ID').send_keys('文字列')
# テキストを取得する
driver.find_element_by_id('ID').text
# 属性値を取得する
driver.find_element_by_id('ID').get_attribute('属性名')
# テキストをクリアする
driver.find_element_by_id('ID').clear()