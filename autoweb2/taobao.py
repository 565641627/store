from selenium import webdriver
driver=webdriver.Chrome()
driver.get(r'https:/www.taobao.com/')
driver.maximize_window()
driver.find_element_by_id('q').send_keys('卡地亚')
driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
driver.find_element_by_id('fm-login-id').send_keys('18908662106')
driver.find_element_by_id('fm-login-password').send_keys('baozouluoli.')

