class Config:
    class Watch:
        WATCH_LIST_SELECTOR = '.hY8lWHgA'
        USER_LINK_PATTERN = 'https://www.zhihu.com/people/.*'

    class JsScript:
        SCROLL_DOWN = "window.scrollBy(0, 100);"
        Click = "arguments[0].click();"
