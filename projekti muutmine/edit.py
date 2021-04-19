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

pealkiri = driver.find_element_by_name('post_title')
pealkiri.send_keys(' test')

eng_pealkiri = driver.find_element_by_name('postitus_pealkiri_ing')
eng_pealkiri.send_keys(' test')

eesmark = driver.find_element_by_name('postitus_eesmark')
eesmark.send_keys(' test')

time.sleep(0.5)

summary = driver.find_element_by_name('postitus_ing_kokkuvote')
summary.send_keys(' test')

time.sleep(0.5)

modal = driver.find_element_by_id('main-edit')
modal.send_keys(Keys.PAGE_DOWN)


sisu = driver.find_element_by_name('post_content')
sisu.send_keys(' test')

time.sleep(0.5)

aasta = driver.find_element_by_name('postitus_kaitsmise_aasta')
aasta.clear()
aasta.send_keys('2008')

algus = driver.find_element_by_name('postitus_kestus_algus')
algus.clear()
algus.send_keys('2008')

staatus = driver.find_element_by_name('staatus_nimi')
Select(staatus).select_by_index(1)

time.sleep(0.5)

modal = driver.find_element_by_id('main-edit')
modal.send_keys(Keys.PAGE_DOWN)

box = driver.find_element_by_id('save')
box.click()

submit = driver.find_element_by_name('submitMainModal')
submit.click()

message = driver.find_element_by_class_name('entry-title') 

pealkirjaSisu = 'Eesti õdede tervisekäitumine. 2009-2010 test'

assert message.text == pealkirjaSisu

if message.text == pealkirjaSisu:
    print("Created post title: %r"  % message.text)

time.sleep(0.5)

def clear_text(element, length):
    #length = len(element.get_attribute('value'))
    element.send_keys(length * Keys.BACKSPACE)

time.sleep(0.5)

muuda = driver.find_element_by_id('main-modal-btn')
muuda.click()

time.sleep(0.5)
 
pealkiri = driver.find_element_by_name('post_title')
clear_text(pealkiri, 5)

eng_pealkiri = driver.find_element_by_name('postitus_pealkiri_ing')
clear_text(eng_pealkiri, 5)

eesmark = driver.find_element_by_name('postitus_eesmark')
clear_text(eesmark, 5)

time.sleep(0.5)

summary = driver.find_element_by_name('postitus_ing_kokkuvote')
clear_text(summary, 5)

modal = driver.find_element_by_id('main-edit')
modal.send_keys(Keys.PAGE_DOWN)

sisu = driver.find_element_by_name('post_content')
clear_text(sisu, 5)

aasta = driver.find_element_by_name('postitus_kaitsmise_aasta')
aasta.clear()
aasta.send_keys('2007')

algus = driver.find_element_by_name('postitus_kestus_algus')
algus.clear()
algus.send_keys('2007')

staatus = driver.find_element_by_name('staatus_nimi')
Select(staatus).select_by_index(3)

time.sleep(0.5)

modal = driver.find_element_by_id('main-edit')
modal.send_keys(Keys.PAGE_DOWN)

box = driver.find_element_by_id('save')
box.click()

submit = driver.find_element_by_name('submitMainModal')
submit.click()

message2 = driver.find_element_by_class_name('entry-title') 

pealkirjaSisu2 = 'Eesti õdede tervisekäitumine. 2009-2010'

assert message2.text == pealkirjaSisu2

if message2.text == pealkirjaSisu2:
    print("Removed test: %r"  % message2.text)