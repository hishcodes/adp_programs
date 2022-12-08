from selenium import webdriver

while True:
    browser = webdriver.Chrome()
    browser.get("https://amazon.in")

    search_box = browser.find_element_by_id('twotabsearchtextbox')
    search_box.send_keys("iphone 14")

    search_button = browser.find_element_by_id('nav-search-submit-button')
    search_button.click()

    price = browser.find_element_by_class_name('a-price-whole')

    print("Price of iphone 14 is: " + price.text)