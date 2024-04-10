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

sleep(100)
# 登录,打开网页后操作

# find the link list
elements = driver.find_elements(By.CSS_SELECTOR, '.B3AsdZT9')
print(f'elements:', elements)

# 获取第一个元素
first_element = elements[0] if elements else None

# 对第一个元素执行操作，比如点击
sleep(1.1)
# save current window
main_window = driver.current_window_handle

first_element.click()

# 必须要先切换到新的窗口，才能对新的页面进行操作
for window_handle in driver.window_handles:
    if window_handle != main_window:
        driver.switch_to.window(window_handle)
        break

# 等待新页面的某个元素出现
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-e2e="user-info-follow-btn"][type="button"]'))
)

# 现在可以对新页面进行操作
# search = driver.find_element(By.CSS_SELECTOR, '.st2xnJtZ.YIde9aUh')
# print(f'search2:', search)
button = driver.find_element(By.CSS_SELECTOR, 'button[data-e2e="user-info-follow-btn"][type="button"]')
print(f'button:', button)
sleep(1.3)
button.click()
sleep(0.9)
