from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
load_dotenv()

import os

pwd = os.getenv("pythonpwd")

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)

driver.set_window_size(1400,1200)

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

driver.get('https://ristmik.nooruse.ee/eesti-odede-tervisekaitumine-2009-2010/')

time.sleep(0.5)

muuda = driver.find_element_by_id('main-modal-btn')
muuda.click()

time.sleep(0.5)

modal = driver.find_element_by_id('main-edit')
modal.send_keys(Keys.PAGE_DOWN)

autor = driver.find_element_by_id('autor')
autor.click()

