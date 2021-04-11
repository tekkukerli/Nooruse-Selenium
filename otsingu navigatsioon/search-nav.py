from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.set_window_size(1400,1000)

driver.get('https://ristmik.nooruse.ee/')

import time
time.sleep(1)

search = driver.find_element_by_id('menu-item-10')
search.click()

year = driver.find_element_by_id('menu-item-69')
year.click()

time.sleep(0.5)

pageTwo = driver.find_element_by_xpath('//*[@id="main-text"]/div[3]/div/ul/li[3]')
pageTwo.click()

time.sleep(0.5)

dropdown = driver.find_element_by_class_name('select2-selection.select2-selection--single')
dropdown.click()

time.sleep(0.5)

yearselect = driver.find_element_by_xpath('//*[@class="select2-results__options"]/li[3]')   
yearselect.click()

time.sleep(0.5)

author = driver.find_element_by_id('menu-item-72')
author.click()

time.sleep(0.5)

pageThree = driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div[1]/div/div/div[2]/div/ul/li[4]')
pageThree.click()

time.sleep(0.5)

tag = driver.find_element_by_id('menu-item-71')
tag.click()

time.sleep(0.5)

nextButton = driver.find_element_by_class_name('active.fa.fa-arrow-right')
nextButton.click()

time.sleep(0.5)

title = driver.find_element_by_id('menu-item-70')
title.click()

time.sleep(0.5)

nextButton2 = driver.find_element_by_class_name('active.fa.fa-arrow-right')
nextButton2.click()

time.sleep(0.5)

prevButton = driver.find_element_by_class_name('active.fa.fa-arrow-left')
prevButton.click()

time.sleep(0.5)

expectedText = 'Sirvi pealkirja järgi' 

time.sleep(0.5)

success = driver.find_element_by_class_name('entry-title.search-title')

assert success.text == expectedText

if success.text == expectedText:
    print("Success: %r"  % success.text)

driver.quit()

