# 导入 selenium 库
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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
sleep(2)

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

sleep(0.2)

# save current window
main_window = driver.current_window_handle

# find search button
search_button = driver.find_element(By.CSS_SELECTOR, '.JMEzcqbO')
search_button.click()

# sleep(3)

# WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

# 必须要先切换到新的窗口，才能对新的页面进行操作
for window_handle in driver.window_handles:
    if window_handle != main_window:
        driver.switch_to.window(window_handle)
        break

# 等待新页面的某个元素出现
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".dC4GYZQ1"))
)

# 现在可以对新页面进行操作
# search = driver.find_element(By.CSS_SELECTOR, '.st2xnJtZ.YIde9aUh')
# print(f'search2:', search)

sleep(0.9)

verify_text = driver.find_element(By.CSS_SELECTOR, '.dC4GYZQ1')
print('verify_text:', verify_text)

sleep(0.3)
# find comment area
comment = driver.find_element(By.CSS_SELECTOR, '.tzVl3l7w')
print(f'comment:', comment)

# save current window
search_window = driver.current_window_handle
sleep(5)
# click comment area
comment.click()

sleep(1.1)

# # 必须要先切换到新的窗口，才能对新的页面进行操作
# for window_handle in driver.window_handles:
#     if window_handle != main_window:
#         driver.switch_to.window(window_handle)
#         break
