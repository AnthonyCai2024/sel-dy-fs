from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


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
