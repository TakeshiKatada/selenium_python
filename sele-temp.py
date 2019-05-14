# PythonでSeleniumのwebdriverモジュールをインポート
from selenium import webdriver

# 1.操作するブラウザを開く
# /Users/imac2/Desktop/Selenium/chromedriver
driver = webdriver.Chrome('WebDriverを格納しているディレクトリを指定')

# 2.操作するページを開く
driver.get('URL')

# 基本設定はここまで。↑は使い回し可能。ここから下は、やりたい動作によって増える

# 3.操作する要素を指定

# 4.その要素を操作する