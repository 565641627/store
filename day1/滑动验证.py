import time
from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get(r'D:/Python%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%BB%83%E4%B9%A0%E7%9A%84html/%E7%BB%83%E4%B9%A0%E7%9A%84html/%E6%BB%91%E5%8A%A8%E9%AA%8C%E8%AF%81/mousedrag.html')
tip=driver.find_element_by_class_name('slider')
ActionChains(driver).drag_and_drop_by_offset(tip,248,0).perform()
time.sleep(1)
driver.quit()
