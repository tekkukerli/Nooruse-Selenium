from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.set_window_size(1400,1000)

driver.get('https://ristmik.nooruse.ee/otsing-aasta/')

import time
time.sleep(1)


box = driver.find_element_by_id('search-box')
box.send_keys('cars') 

time.sleep(0.5)

button = driver.find_element_by_id('search-btn')
button.click()

count = len(driver.find_elements_by_class_name('posts'))


expectedText = 'Otsingu tulemused: cars' 

time.sleep(0.5)

success = driver.find_element_by_class_name('page-title.search-title')

assert success.text == expectedText

if success.text == expectedText:
    print("Results on page %r of 5" % count)
    print("Success: %r"  % success.text)
    

driver.quit()

