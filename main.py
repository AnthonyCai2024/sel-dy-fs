from driver.watcher import Watcher
from driver.web_driver import WebDriver
from my.follow import Follow
from utils.argument_parser import parse_arguments
from utils.reg_filter import RegFilter

if __name__ == '__main__':
    link, count = parse_arguments()

    url = RegFilter.url_search(link)

    web_driver = WebDriver()
    watcher = Watcher()
    # get url
    web_driver.get_url(url)

    # get follow
    followers = Follow.get_live_followers(web_driver)

    exit()

    sleep(2)
    # todo scroll down
    web_driver.page_down()

    sleep(0.6)

    web_driver.page_down()

    sleep(0.6)

    web_driver.page_down()

    sleep(0.6)

    web_driver.page_down()

    # find all watch list
    elements = web_driver.find_elements(Config.Watch.WATCH_LIST_SELECTOR)

    # filter valid user
    valid_user_list = watcher.filter_valid_user(elements)
    # todo compare with already watched list

    print(f'valid_user_list count:', len(valid_user_list))

    # follow user
    watcher.follow_user(web_driver, valid_user_list, count)
