from time import sleep

from driver.web_driver import WebDriver
from models.config import Config

if __name__ == '__main__':
    # open the url
    url = 'https://www.douyin.com/note/7290718479680834876'
    web_driver = WebDriver()
    web_driver.get_url(url)
    sleep(9)

    user_dict = {}

    # find all comment list
    elements = web_driver.find_elements_xpath(Config.Watch.WATCH_LIST_XPATH)
    if elements:
        print(f'elements count:', len(elements))
        for element in elements:
            href = element.get_attribute('href')
            user_id = href.split("/user/")[1]

            # save to dict
            user_dict[user_id] = href

    if user_dict:
        print(f'user_dict count:', len(user_dict))
        for key, value in user_dict.items():
            print(f'user_id:', key)
            print(f'href:', value)
