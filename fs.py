# 导入 selenium 库
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建 Chrome 浏览器驱动程序实例
driver = webdriver.Chrome()

driver.get('https://www.douyin.com/')
# driver.get('https://www.baidu.com/')
# assert 'Yahoo' in browser.title

print(driver.title)
print(driver.current_url)

# elem = browser.find_element(By.NAME, 'p')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)

# sleep(5)  # Let the page load, will be added to the API
sleep(3)

# <li class="web-login-tab-list__item web-login-tab-list__item__active" tabindex="0"
# aria-label="扫码登录" role="tab" aria-selected="true">扫码登录</li>

# classname
# search = driver.find_element(By.ID, 'kw')
# search = driver.find_element(By.CLASS_NAME, 'web-login-tab-list__item')
# print(f'search:', search)

# class
element = driver.find_element(By.CSS_SELECTOR, '.web-login-tab-list__item__active')
print(f'element:', element)

# li
li = driver.find_element(By.CSS_SELECTOR, 'li[aria-label="扫码登录"]')
print(f'li:', li)

# xpath
# search = driver.find_element(By.XPATH, '//input[@name="wd"]')

# close
# driver.close()

# find the close button
close = driver.find_element(By.CLASS_NAME, 'dy-account-close')
print(f'close:', close)
close.click()

# find search box
search = driver.find_element(By.CSS_SELECTOR, '.st2xnJtZ.YIde9aUh')
print(f'search:', search)

# send text
search.send_keys('计划粉丝一千万')
search.click()

sleep(5)

sleep(1)
