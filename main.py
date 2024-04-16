from driver.watcher import Watcher
from driver.web_driver import WebDriver
from utils import redis_util
from utils.argument_parser import parse_arguments
from utils.reg_filter import RegFilter

if __name__ == '__main__':
    link, count = parse_arguments()

    url = RegFilter.url_search(link)

    web_driver = WebDriver()
    watcher = Watcher()

    # get from redis
    urls = redis_util.get_set('douyin_user')
    if urls and len(urls) > 0:
        print(f'urls count:', len(urls))
        # follow user
        watcher.follow_user_by_url(web_driver, urls, count)
    else:
        print(f'No user found in redis!')
