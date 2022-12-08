from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://hishcodes.com")

full_page = browser.find_element_by_tag_name('html')
full_page.send_keys(Keys.END)


