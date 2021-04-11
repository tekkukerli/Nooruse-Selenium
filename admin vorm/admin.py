from selenium import webdriver
import random
from dotenv import load_dotenv
load_dotenv()

import os

pwd = os.getenv("pythonpwd")

first_names=('John','Andy','Joe', 'Liam','Noah','Oliver','William','Elijah','James','Benjamin','Lucas','Mason','Ethan','Alexander','Henry','Jacob','Michael','Daniel','Logan','Jackson','Sebastian','Jack','Aiden')
last_names=('Johnson','Smith','Williams', 'Smith', 'Jones',	'Taylor','Brown','Williams','Wilson','Johnson','Davies','Robinson',	'Wright','Thompson','Evans','Walker','White','Roberts',	'Green','Hall',	'Wood',	'Jackson','Clark')

randomName =" ".join(random.choice(last_names)+", "+random.choice(first_names) for _ in range(1))


print(randomName)

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.set_window_size(1400,1000)

driver.get('https://ristmik.nooruse.ee/')

element = driver.find_element_by_class_name('apsl-icon-block.icon-google')
element.click()

email = driver.find_element_by_id('identifierId')
email.send_keys('noorusetestA@gmail.com')

nextButton = driver.find_element_by_class_name('VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.qIypjc.TrZEUc.lw1w4b')
nextButton.click()

import time
time.sleep(1)

password = driver.find_element_by_name('password')
password.send_keys(pwd)

time.sleep(1)

nextButton2 = driver.find_element_by_class_name('VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.qIypjc.TrZEUc.lw1w4b')
nextButton2.click()

time.sleep(1)

menu = driver.find_element_by_id('menu-item-102')
menu.click()

pealkiri = driver.find_element_by_name('post_title')
randomNr = random.randint(1,100)
pealkirjaSisu = 'selenium2' + str(randomNr) 
pealkiri.send_keys(pealkirjaSisu)

time.sleep(1)

autor = driver.find_element_by_name('autorid_value')
autor.send_keys(randomName)

time.sleep(1)

õigused = driver.find_element_by_xpath("//*[@id='page']/div[2]/div/div[1]/div/div/form/div[3]/select/option[3]").click() 

time.sleep(1)

submit = driver.find_element_by_class_name('project-submit')
submit.click()

time.sleep(1)

message = driver.find_element_by_class_name('entry-title') 

assert message.text == pealkirjaSisu

if message.text == pealkirjaSisu:
    print("Created post title: %r"  % message.text)

driver.quit()      