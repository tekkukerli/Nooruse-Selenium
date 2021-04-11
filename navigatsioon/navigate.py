from selenium import webdriver
from dotenv import load_dotenv
load_dotenv()

import os

pwd = os.getenv("pythonpwd")

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.set_window_size(1400,1000)

driver.get('https://ristmik.nooruse.ee/')

import time

element = driver.find_element_by_class_name('apsl-icon-block.icon-google')
element.click()

email = driver.find_element_by_id('identifierId')
email.send_keys('noorusetestA@gmail.com')

nextButton = driver.find_element_by_class_name('VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.qIypjc.TrZEUc.lw1w4b')
nextButton.click()

time.sleep(1)

password = driver.find_element_by_name('password')
password.send_keys(pwd)

time.sleep(1)

nextButton2 = driver.find_element_by_class_name('VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.qIypjc.TrZEUc.lw1w4b')
nextButton2.click()

time.sleep(1)

contact = driver.find_element_by_id('menu-item-783')
contact.click()

time.sleep(0.5)

rights = driver.find_element_by_id('menu-item-102')
rights.click()

time.sleep(0.5)

search = driver.find_element_by_id('menu-item-10')
search.click()

year = driver.find_element_by_id('menu-item-69')
year.click()

time.sleep(0.5)

logo = driver.find_element_by_id('site-logo')
logo.click()

time.sleep(0.5)

search2 = driver.find_element_by_id('menu-item-10')
search2.click()

author = driver.find_element_by_id('menu-item-68')
author.click()

time.sleep(0.5)

search3 = driver.find_element_by_id('menu-item-10')
search3.click()

tag = driver.find_element_by_id('menu-item-67')
tag.click()

time.sleep(0.5)

search4 = driver.find_element_by_id('menu-item-10')
search4.click()

title = driver.find_element_by_id('menu-item-66')
title.click()

time.sleep(0.5)

frontpage = driver.find_element_by_id('menu-item-8')
frontpage.click()

time.sleep(0.5)

expectedText = 'Tartu Tervishoiu Kõrgkooli arendusprojektide andmebaas' 

success = driver.find_element_by_class_name('home-title.align-items-center')

assert success.text == expectedText

if success.text == expectedText:
    print("Success: %r"  % success.text)

driver.quit()
    