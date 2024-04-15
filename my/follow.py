from time import sleep

from driver.web_driver import WebDriver
from models.config import Config


class Follow:

    def get_followers(self, web_driver: WebDriver):
        pass

    def get_live_followers(self, web_driver: WebDriver):
        # goto  https://www.douyin.com/follow
        driver = web_driver.get_url(Config.My.MY_FOLLOWER_URL)

        sleep(2.3)



    def get_all_followers(self, web_driver: WebDriver):
        pass


