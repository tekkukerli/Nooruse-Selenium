from selenium import webdriver
from dotenv import load_dotenv
load_dotenv()

import os

pwd = os.getenv("pythonpwd")

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)

driver.set_window_size(1400,1000)

driver.get('https://ristmik.nooruse.ee/')

import time

element = driver.find_element_by_class_name('apsl-icon-block.icon-google')
element.click()

email = driver.find_element_by_id('identifierId')
email.send_keys('kerliarendab')

nextButton = driver.find_element_by_class_name('VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.qIypjc.TrZEUc.lw1w4b')
nextButton.click()

time.sleep(1)

password = driver.find_element_by_name('password')
password.send_keys(pwd)

time.sleep(1)

nextButton2 = driver.find_element_by_class_name('VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.qIypjc.TrZEUc.lw1w4b')
nextButton2.click()

time.sleep(1)

