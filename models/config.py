class Config:
    class Watch:
        WATCH_LIST_SELECTOR = '.hY8lWHgA'
        USER_LINK_PATTERN = 'https://www.zhihu.com/people/.*'

    class JsScript:
        SCROLL_DOWN = "window.scrollBy(0, 100);"
        Click = "arguments[0].click();"

    class My:
        MY_FOLLOWER_URL = 'https://www.douyin.com/follow'
        MY_LIVE_VISIBLE = '.uDQ4oF5W'
        MY_LIVE_SELECTOR = '.O3nblU7_.Y_XxfAMJ'
        # //div[@class='my-class']//ul
        MY_FOLLOWER_VISIBLE = "//div[@class='II6cheXp']"
        MY_FOLLOWER_LIST = "//div[@class='II6cheXp']//ul//li"
