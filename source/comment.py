from time import sleep

from driver.web_driver import WebDriver
from models.config import Config
from utils import redis_util

if __name__ == '__main__':
    # open the url
    url = 'https://www.douyin.com/note/7290718479680834876'
    web_driver = WebDriver()
    web_driver.get_url(url)
    sleep(9)

    user_list = []

    # find all comment list
    elements = web_driver.find_elements_xpath(Config.Watch.WATCH_LIST_XPATH)
    if elements:
        print(f'elements count:', len(elements))
        for element in elements:
            href = element.get_attribute('href')
            if href:
                user_list.append(href)

    if user_list:
        print(f'user_list count:', len(user_list))
        unique_user_list = set(user_list)
        redis_util.add_set('douyin_user', unique_user_list)
