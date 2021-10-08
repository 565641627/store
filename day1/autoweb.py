from selenium import webdriver
import time
#连接谷歌浏览器
driver = webdriver.Chrome()
#获取京东网址
driver.get(r'https:/www.jd.com/')
#最大化窗口
driver.maximize_window()
#搜索框输入vivo
driver.find_element_by_xpath("//*[@clstag='h|keycount|head|search_c']").send_keys('vivox70')
#点击搜索
driver.find_element_by_xpath("//*[@clstag='h|keycount|head|search_a']").click()
time.sleep(5)
#打开商品详情页
driver.find_element_by_xpath("//*[@width='220' and @src='//img12.360buyimg.com/n7/jfs/t1/6913/12/16473/79286/615f0ce4E2047080f/3503697a8a681c9c.jpg']").click()
time.sleep(15)
#关闭页面
driver.quit()
time.sleep(5)

'''百度搜索'''
driver.get(r'https:/www.baidu.com/')
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='kw' and @name='wd']").send_keys('深圳')
driver.find_element_by_xpath("//*[@type='submit' and @id='su']").click()
time.sleep(20)
driver.quit()










