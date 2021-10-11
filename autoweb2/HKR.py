import time
from selenium import  webdriver

driver = webdriver.Chrome()

driver.get('http://localhost:8080/HKR/')

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/a[1]').click()

driver.find_element_by_xpath('//*[@id="loginname"]').send_keys('EZ')



driver.find_element_by_xpath('//*[@id="msform"]/fieldset[1]/input[2]').send_keys('ezreal')


driver.find_element_by_xpath('//*[@id="pwd"]').send_keys(123456)


driver.find_element_by_xpath('//*[@id="msform"]/fieldset[1]/input[4]').send_keys(123456)

driver.find_element_by_xpath('//*[@id="msform"]/fieldset[1]/input[5]').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="valid_age"]').send_keys(18)



driver.find_element_by_xpath('//*[@id="msform"]/fieldset[2]/input[3]').click()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="reg_mail"]').send_keys('2857070729@qq.com')



driver.find_element_by_xpath('//*[@id="reg_phone"]').send_keys(18908888554)


driver.find_element_by_xpath('//*[@id="msform"]/fieldset[3]/textarea').send_keys('日本东京')



driver.find_element_by_xpath('//*[@id="btn_reg"]').click()