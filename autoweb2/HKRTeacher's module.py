import time
from selenium import  webdriver

driver = webdriver.Chrome()
#打开网址
driver.get('http://localhost:8080/HKR/')
#页面最大化
driver.maximize_window()
#点击教室登录
driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/a[2]').click()
#输入用户名
driver.find_element_by_id('loginname').send_keys('tonghe')
#输入密码
driver.find_element_by_id('password').send_keys('root')
#点击登录
driver.find_element_by_id('submit').click()
#点击今日评价
driver.find_element_by_id('_easyui_tree_15').click()
time.sleep(2)
#点击日期
driver.find_element_by_id('J-xl').click()
time.sleep(1)
#选择日期
driver.find_element_by_xpath('//*[@id="laydate_table"]/tbody/tr[2]/td[7]').click()
time.sleep(1)
#点击查询
driver.find_element_by_xpath('//*[@id="eva"]/div/div/div[1]/table/tbody/tr/td[2]/a/span/span[1]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[8]/div[3]/a/span/span').click()
time.sleep(2)
#点击导出评价
driver.find_element_by_xpath('//*[@id="eva"]/div/div/div[1]/table/tbody/tr/td[4]/a/span/span[1]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[8]/div[3]/a/span/span').click()
time.sleep(2)
#点击评价报表
driver.find_element_by_xpath('//*[@id="_easyui_tree_16"]/span[4]/a').click()
time.sleep(2)
#点击历史操作日志
driver.find_element_by_id('_easyui_tree_18').click()
time.sleep(2)
driver.refresh()
driver.find_element_by_id('_easyui_tree_18').click()
#点击日期
driver.find_element_by_id('J-history').click()
time.sleep(2)
#选择年份
driver.find_element_by_id('laydate_y').click()
time.sleep(1)
#2020
driver.find_element_by_xpath('//*[@id="laydate_ys"]/li[7]').click()
time.sleep(2)
#选择月份
driver.find_element_by_id('laydate_m').click()
time.sleep(1)
#5月
driver.find_element_by_xpath('//*[@id="laydate_ms"]/span[5]').click()
time.sleep(1)
#选择日期
driver.find_element_by_xpath('//*[@id="laydate_table"]/tbody/tr[5]/td[5]').click()
time.sleep(2)
#点击查询
driver.find_element_by_xpath('//*[@id="history"]/div/div/div[1]/table/tbody/tr/td[2]/a/span/span[1]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[8]/div[3]/a/span/span').click()
driver.find_element_by_xpath('//*[@id="history"]/div/div/div[3]/table/tbody/tr/td[13]/a/span/span[2]').click()
time.sleep(1)
#选择页面数据显示数量
driver.find_element_by_xpath('//*[@id="history"]/div/div/div[3]/table/tbody/tr/td[1]/select').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="history"]/div/div/div[3]/table/tbody/tr/td[1]/select/option[2]').click()
#选择第88页
driver.find_element_by_xpath('//*[@id="history"]/div/div/div[3]/table/tbody/tr/td[7]/input').send_keys('88')
#导出当前日志
driver.find_element_by_xpath('//*[@id="history"]/div/div/div[1]/table/tbody/tr/td[4]/a/span/span[1]').click()
time.sleep(5)
driver.quit()








