from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = 'https://www.douyin.com/user/MS4wLjABAAAADYK2_uBpwAV95OZRAnjeGRP0iu7PCW1PdaJTcKQrgOBwJWdExP9fJkIr8a56Aeg7'

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
driver.get(url)

print(driver.title)
print(driver.current_url)

sleep(3.6)
button = driver.find_element(By.CSS_SELECTOR, 'button[data-e2e="user-info-follow-btn"][type="button"]')
print(f'button:', button.get_attribute('outerHTML'))
sleep(1.3)
# button.click()
driver.execute_script("arguments[0].click();", button)
