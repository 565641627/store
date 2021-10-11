import time
from selenium import  webdriver

driver = webdriver.Chrome()

driver.get('http://localhost:8080/HKR/')

driver.maximize_window()
#注册
'''
driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/a[1]').click()

driver.find_element_by_xpath('//*[@id="loginname"]').send_keys('Friday')



driver.find_element_by_xpath('//*[@id="msform"]/fieldset[1]/input[2]').send_keys('阿飞')


driver.find_element_by_xpath('//*[@id="pwd"]').send_keys(123456)


driver.find_element_by_xpath('//*[@id="msform"]/fieldset[1]/input[4]').send_keys(123456)

driver.find_element_by_xpath('//*[@id="msform"]/fieldset[1]/input[5]').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="valid_age"]').send_keys(22)



driver.find_element_by_xpath('//*[@id="msform"]/fieldset[2]/input[3]').click()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="reg_mail"]').send_keys('2421045399@qq.com')



driver.find_element_by_xpath('//*[@id="reg_phone"]').send_keys(18034275926)


driver.find_element_by_xpath('//*[@id="msform"]/fieldset[3]/textarea').send_keys('河北省沧州市沧县')



driver.find_element_by_xpath('//*[@id="btn_reg"]').click()
'''
#用户
# driver.find_element_by_xpath("//*[@id='loginname']").send_keys("DW")
# driver.find_element_by_xpath("//*[@id='password']").send_keys("123456")
# driver.find_element_by_xpath("//*[@id='submit']").click()
# time.sleep(2)
# ============修改头像==========================================================================
# driver.find_element_by_xpath("//*[@id='img']").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='ul_pic'][6]/img").click()
# =========================================================================================

# ============提交评价========================================================================
# #driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[2]/td[2]").send_keys("9 (上晚自习)")
# driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[7]/td[3]/div/label[2]/div").click()
# driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[11]/td[2]/div/label[2]/div").click()
# driver.find_element_by_xpath("//*[@id='textarea']").send_keys("waesrdbfsdbvfdasddbfdwddbfds")
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='subtn']").click()


# ============查询同学==========================================================================
# driver.find_element_by_xpath("//*[@id='_easyui_tree_10']").click()

# ============修改信息==========================================================================
# driver.find_element_by_xpath("//*[@id='_easyui_tree_8']").click()
#
# ac = ActionChains(driver)
#
# age = driver.find_element_by_xpath("//*[@id='_easyui_textbox_input1']")
# ac.double_click(age).send_keys("26").perform()
# ac.release()
# driver.find_element_by_xpath("//*[@id='btn_modify']").click()
#
#
# driver.quit()

#教师管理：查询，重置密码
'''
driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/a[2]').click()

driver.find_element_by_xpath('//*[@id="loginname"]').send_keys(13552648187)

driver.find_element_by_xpath('//*[@id="password"]').send_keys('admin')

driver.find_element_by_xpath('//*[@id="submit"]').click()

driver.find_element_by_xpath('//*[@id="_easyui_tree_11"]/span[4]/a').click()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="sear_teaname"]').send_keys('乔越洋')

driver.find_element_by_xpath('//*[@id="search_user"]/span/span[1]').click()

driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[9]/div/a').click()
'''


#学生管理：姓名电话查询，设置毕业
'''
driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/a[2]').click()

driver.find_element_by_xpath('//*[@id="loginname"]').send_keys(13552648187)

driver.find_element_by_xpath('//*[@id="password"]').send_keys('admin')

driver.find_element_by_xpath('//*[@id="submit"]').click()

driver.find_element_by_xpath('//*[@id="_easyui_tree_12"]/span[4]/a').click()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="J-stu"]').send_keys('阿飞')
driver.find_element_by_xpath('//*[@id="J-phone"]').send_keys(18034275926)

driver.find_element_by_xpath('//*[@id="stu_panel"]/div/div/div[1]/table/tbody/tr/td[4]/a/span/span[1]').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[11]/div/a').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[8]/div[3]/a/span/span').click()

'''

#课程管理：添加、取消添加课程
'''
driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/a[2]').click()

driver.find_element_by_xpath('//*[@id="loginname"]').send_keys(13552648187)

driver.find_element_by_xpath('//*[@id="password"]').send_keys('admin')

driver.find_element_by_xpath('//*[@id="submit"]').click()

driver.find_element_by_xpath('//*[@id="_easyui_tree_13"]/span[4]/a').click()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="course_panel"]/div/div/div[1]/table/tbody/tr/td/a/span/span[1]').click()

driver.find_element_by_xpath('//*[@id="course_form_add"]/table/tbody/tr[1]/td[2]/input').send_keys('芜湖')

driver.find_element_by_xpath('//*[@id="course_form_add"]/table/tbody/tr[2]/td[2]/textarea').send_keys('666')

driver.find_element_by_xpath('/html/body/div[7]/div[3]/a[1]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[10]/div[3]/a').click()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="course_form_add"]/table/tbody/tr[1]/td[2]/input').send_keys('航天')

driver.find_element_by_xpath('//*[@id="course_form_add"]/table/tbody/tr[2]/td[2]/textarea').send_keys('起飞')


driver.find_element_by_xpath('/html/body/div[7]/div[3]/a[2]/span').click()
'''


'''
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
'''









