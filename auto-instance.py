import random
from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# 定义关注次数,随机6-10
count_gz = random.randint(6, 11)

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

# 等待新页面的 综合 选项出现
element = WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".qwx22yjn"))
)

# 现在可以对新页面进行操作
zh = driver.find_element(By.CSS_SELECTOR, '.qwx22yjn')
print(f'zh:', zh)
sleep(1.3)
zh.click()

sleep(1.2)

verify_text = driver.find_element(By.CSS_SELECTOR, '.tzVl3l7w')
print('verify_text:', verify_text)

sleep(1.9)
# find comment area
comment = driver.find_element(By.CSS_SELECTOR, '.tzVl3l7w')
print(f'comment:', comment)

# save current window
search_window = driver.current_window_handle
sleep(4.2)
# click comment area
comment.click()

sleep(1.2)

# find the link list
elements = driver.find_elements(By.CSS_SELECTOR, '.B3AsdZT9')
print(f'elements count:', len(elements))

# 遍历元素列表，检查元素的HTML中是否包含特定字符串
specific_string = 'MS4'
filtered_elements = [element for element in elements if specific_string in element.get_attribute('outerHTML')]

# 使用字典来存储已经添加的name，确保唯一性
# 字典的键是name，值是相应的字典（第一次出现的）
unique_hrefs = {}

# 对筛选后的元素列表进行操作
for element in filtered_elements:
    # print(element.get_attribute('outerHTML'))  # 或者任何你需要对元素进行的操作
    try:
        href = element.get_attribute('href')
        # print('href:', href)

        if href not in unique_hrefs:
            unique_hrefs[href] = element

    except NoSuchElementException:
        print('No href found inside this ')

# 打印字典的值
for value in unique_hrefs.values():
    print(value.get_attribute('outerHTML'))

# 获取字典的值集合，这些是唯一的元素
filtered_unique_items = list(unique_hrefs.values())

# 定义起始索引
index = 1

# 遍历唯一元素列表
for item in filtered_unique_items:
    index += 1
    print(f'index:', index)

    if index > count_gz:
        print(f'已经关注了{count_gz}个用户,程序退出!')
        break
    if index > 1:
        print(f'程序开始关注:', item.get_attribute('outerHTML'))
    else:
        print(f'程序跳过第一个关注:')
        continue

    # 获取第二个元素,第一个固定是同一个人,不能使用
    # first_element = filtered_unique_items[1] if elements else None
    first_element = item if elements else None
    print(f'first_element:', first_element.get_attribute('outerHTML'))

    # sec = elements[10] if elements else None
    # print(f'sec:', sec.get_attribute('outerHTML'))

    # 对第一个元素执行操作，比如点击
    sleep(1.1)
    # save current window
    target_window = driver.current_window_handle

    first_element.click()

    sleep(3.1)
    # 遍历所有窗口句柄，切换到最新的窗口
    for window_handle in driver.window_handles:
        driver.switch_to.window(window_handle)

    sleep(1.1)

    button = driver.find_element(By.CSS_SELECTOR, 'button[data-e2e="user-info-follow-btn"][type="button"]')
    button_html = button.get_attribute('outerHTML')
    print(f'button:', button.get_attribute('outerHTML'))

    sleep(1.3)

    if '已关注' in button_html:
        print('已关注,不需再次点击')
    else:
        driver.execute_script("arguments[0].click();", button)

    sleep(0.9)
    # 关闭当前标签页
    driver.close()

    # 关闭当前窗口
    # 获取当前所有打开的标签页的句柄
    handles = driver.window_handles

    handle_count = len(handles)

    # 切换到新打开的标签页
    driver.switch_to.window(handles[handle_count - 1])
