from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# 指定ChromeDriver路径
chrome_driver_path = 'D:/data/chrome/chromedriver-win64/chromedriver-win64/chromedriver.exe'

# 设置Service
service = Service(executable_path=chrome_driver_path)

# 创建WebDriver对象
driver = webdriver.Chrome(service=service, options=chrome_options)

# 现在你可以控制已打开的浏览器实例了
# driver.get("https://www.baidu.com")
driver.get("https://www.douyin.com/")

print(driver.title)
print(driver.current_url)

sleep(3.6)

# find search box
search = driver.find_element(By.CSS_SELECTOR, '.st2xnJtZ.YIde9aUh')
print(f'search:', search)
sleep(1.1)

# send text
search.send_keys('计划粉丝一千万')

sleep(0.2)

# save current window
main_window = driver.current_window_handle

# find search button
search_button = driver.find_element(By.CSS_SELECTOR, '.JMEzcqbO')
print(f'search_button:', search_button)
search_button.click()

# sleep(3)

# WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

# 必须要先切换到新的窗口，才能对新的页面进行操作
for window_handle in driver.window_handles:
    if window_handle != main_window:
        driver.switch_to.window(window_handle)
        break

sleep(5)
