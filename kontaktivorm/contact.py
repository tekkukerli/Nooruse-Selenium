from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.set_window_size(1400,1000)

driver.get('https://ristmik.nooruse.ee/kontakt/')

import time
time.sleep(1)

name = driver.find_element_by_name('nimi')
name.send_keys('John')

lastname = driver.find_element_by_name('perenimi')
lastname.send_keys('Doe')

email = driver.find_element_by_name('epost')
email.send_keys('John@gmail.com')       

company = driver.find_element_by_name('firma')
company.send_keys('Elva Haigla')      

message = driver.find_element_by_name('sonum')
message.send_keys('See on Selenium testing.')      

time.sleep(1)

submit = driver.find_element_by_class_name('wpcf7-form-control.wpcf7-submit')
submit.click()

time.sleep(1)
      
expectedText = 'Sõnum saadetud. Täname sõnumi eest!' 

success = driver.find_element_by_class_name('wpcf7-response-output')

assert success.text == expectedText

if success.text == expectedText:
    print("Success: %r"  % success.text)

driver.quit()


  

       