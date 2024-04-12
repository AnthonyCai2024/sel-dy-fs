from selenium.webdriver.common.by import By

from driver.watcher import Watcher
from driver.web_driver import WebDriver
from models.config import Config
from utils.argument_parser import parse_arguments
from utils.reg_filter import RegFilter

if __name__ == '__main__':
    link, count = parse_arguments()

    url = RegFilter.url_search(link)

    web_driver = WebDriver()
    watcher = Watcher()
    # get url
    web_driver.get_url(url)

    # find all watch list
    elements = web_driver.find_elements(By.CSS_SELECTOR, Config.Watch.WATCH_LIST_SELECTOR)

    # filter valid user
    valid_user_list = watcher.filter_valid_user(elements)
    # todo compare with already watched list

    print(f'valid_user_list count:', len(valid_user_list))
