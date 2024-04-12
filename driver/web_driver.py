from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from models.config import Config


class WebDriver:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

        # 指定ChromeDriver路径
        chrome_driver_path = 'D:/data/chrome/chromedriver-win64/chromedriver-win64/chromedriver.exe'

        # 设置Service
        service = Service(executable_path=chrome_driver_path)

        # 创建WebDriver对象
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # init driver
        self.driver = driver

    def get_url(self, url):
        self.driver.get(url)

        print(self.driver.title)
        print(self.driver.current_url)

    def find_element(self, value, by=By.CSS_SELECTOR):
        return self.driver.find_element(by, value)

    def find_elements(self, value, by=By.CSS_SELECTOR):
        return self.driver.find_elements(by, value)

    def switch_to_latest_window(self):
        # 遍历所有窗口句柄，切换到最新的窗口
        for window_handle in self.driver.window_handles:
            self.driver.switch_to.window(window_handle)

    # switch to main window
    def close_switch_to_main_window(self):
        self.close_current_tab()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def execute_script(self, script, *args):
        self.driver.execute_script(script, *args)

    def execute_click(self, element):
        self.execute_script(Config.JsScript.Click, element)

    def close_current_tab(self):
        if len(self.driver.window_handles) > 1:
            self.driver.close()
