from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9515")
# chrome_driver_path = "D:/data/chrome/chrome-win64/chrome-win64/chrome.exe"
chrome_driver_path = "D:/data/chrome/chromedriver_win32/chromedriver.exe"

# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
