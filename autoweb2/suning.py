from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(r'https:/www.suning.com/')
driver.maximize_window()
driver.find_element_by_id('searchKeywords').send_keys('vivox70')
driver.find_element_by_id('searchSubmit').click()
time.sleep(2)
driver.find_element_by_xpath(
    '//*[@id="ssdsn_search_pro_baoguang{invStatus}-0-1_1_01:0071201482_12318196964"]/img').click()
time.sleep(2)
data = driver.window_handles
driver.switch_to.window(data[1])
driver.find_element_by_id('addCart').click()
time.sleep(2)
# driver.quit()
