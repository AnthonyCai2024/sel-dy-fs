from time import sleep

from driver.web_driver import WebDriver
from models.config import Config

if __name__ == '__main__':
    # open the url
    url = 'https://www.douyin.com/note/7290718479680834876'
    web_driver = WebDriver()
    web_driver.get_url(url)
    sleep(9)
    # find all comment list
    elements = web_driver.find_elements_xpath(Config.Watch.WATCH_LIST_XPATH)
    if elements:
        print(f'elements count:', len(elements))
        for element in elements:
            print(element.get_attribute('href'))
