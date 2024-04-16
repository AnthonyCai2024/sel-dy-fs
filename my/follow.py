from driver.web_driver import WebDriver
from models.config import Config


class Follow:

    def get_followers(self, web_driver: WebDriver):
        pass

    @staticmethod
    def get_live_followers(web_driver: WebDriver):
        # goto  https://www.douyin.com/follow
        my_follow = web_driver.get_url(Config.My.MY_FOLLOWER_URL)

        # wait uDQ4oF5W
        visible = web_driver.web_driver_wait(Config.My.MY_LIVE_VISIBLE, timeout=6)
        if visible:
            elements = web_driver.find_elements(Config.My.MY_LIVE_SELECTOR)
            if elements:
                print(f'elements:', elements)

    def get_all_followers(self, web_driver: WebDriver):
        pass
