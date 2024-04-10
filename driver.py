from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 指定ChromeDriver的路径
chrome_driver_path = 'D:/data/chrome/chromedriver-win64/chromedriver-win64/chromedriver.exe'

# 设置ChromeDriver的路径
service = Service(executable_path=chrome_driver_path)

# 创建Chrome浏览器实例
driver = webdriver.Chrome(service=service)

# 打开一个网页
driver.get('https://www.baidu.com')

sleep(5)
