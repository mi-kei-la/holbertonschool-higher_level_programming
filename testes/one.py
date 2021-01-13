import selenium
from selenium import webdriver

#Access with Chrome to first website
driver = webdriver.Chrome()
driver.get('http://158.69.76.135/level0.php')

#Input user id
id_box = driver.find_element_by_name('id')
id_box.send_keys('2101')

#Find button
submit_button = driver.find_element_by_name('holdthedoor')

#Click 3 times
for i in range(0, 3):
    submit_button.click()