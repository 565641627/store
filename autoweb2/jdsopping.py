from selenium import webdriver
from selenium.webdriver import ActionChains
from urllib import request
import numpy as np
import cv2
import time
#连接谷歌浏览器
driver = webdriver.Chrome()
#获取京东网址
driver.get(r'https:/www.jd.com/')
#最大化窗口
driver.maximize_window()
#搜索框输入vivo
driver.find_element_by_xpath("//*[@clstag='h|keycount|head|search_c']").send_keys('华硕天选2')
#点击搜索
driver.find_element_by_xpath("//*[@clstag='h|keycount|head|search_a']").click()
time.sleep(5)
#打开商品详情页
driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[2]/div/div[1]/a/img").click()
time.sleep(5)
#切换到商品页面
data=driver.window_handles
driver.switch_to.window(data[1])
#点击添加购物车
driver.find_element_by_id('InitCartUrl').click()
time.sleep(3)
#点击账号登录
driver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/div/div[3]/a").click()
#定位账号密码输入框
driver.find_element_by_id('loginname').send_keys('18908662106')
driver.find_element_by_id('nloginpwd').send_keys('ezreal..')
#点击登录
driver.find_element_by_xpath("//*[@href='javascript:;' and @class='btn-img btn-entry']").click()
#滑动验证

class JD_Login:
    def get_image(self):
        backimgUrl = self.driver.find_element_by_xpath(r'//div/div[@class="JDJRV-bigimg"]/img').get_attribute(
            "src")  # 背景缺口图链接
        gapUrl = self.driver.find_element_by_xpath(r'//div/div[@class="JDJRV-smallimg"]/img').get_attribute("src")  # 块状缺口链接

        request.urlretrieve(backimgUrl, "backing.png")
        request.urlretrieve(gapUrl, "gap.png")


    def get_diff_location(self):
        # 获取图片并灰度化
        block = cv2.imread("gap.png", 0)
        template = cv2.imread("backing.png", 0)
        # 二值化后的图片名称
        blockName = "block.jpg"
        templateName = "template.jpg"
        # 将二值化后的图片进行保存
        cv2.imwrite(blockName, block)
        cv2.imwrite(templateName, template)
        block = cv2.imread(blockName)
        block = cv2.cvtColor(block, cv2.COLOR_RGB2GRAY)
        block = abs(255 - block)
        cv2.imwrite(blockName, block)
        block = cv2.imread(blockName)
        template = cv2.imread(templateName)
        # 获取偏移量
        result = cv2.matchTemplate(block, template, cv2.TM_CCOEFF_NORMED)  # 查找block在template中的位置，返回result是一个矩阵，是每个点的匹配结果
        x, y = np.unravel_index(result.argmax(), result.shape)
        print("x方向的偏移", int(y * 0.4 + 18), 'x:', x, 'y:', y)
        return y


    def get_move_track(self, gap):
        print("需要移动的距离", gap)
        track = []  # 移动轨迹
        current = 0  # 当前位移
        # 减速阈值
        mid = gap * 4 / 5  # 前4/5段加速 后1/5段减速
        t = 0.2  # 计算间隔
        v = 0  # 初速度
        while current < gap:
            if current < mid:
                a = 3  # 加速度为+3
            else:
                a = -3  # 加速度为-3
            v0 = v  # 初速度v0
            v = v0 + a * t  # 当前速度
            move = v0 * t + 1 / 2 * a * t * t  # 移动距离
            current += move  # 当前位移
            track.append(round(move))  # 加入轨迹
        return track


    def move_slider(self, track):
        slider = self.driver.find_elements_by_xpath(r'//div[@class="JDJRV-slide-inner JDJRV-slide-btn"]')[0]
        ActionChains(self.driver).click_and_hold(slider).perform()
        for x in track:  # 只有水平方向有运动 按轨迹移动
            ActionChains(self.driver).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(1)
        ActionChains(self.driver).release().perform()  # 松开鼠标


    def main(self):
        self.agreement_inputPhone()
        self.get_image()
        gap = self.get_diff_location()
        track = self.get_move_track(gap)
        # print("移动轨迹",track)
        self.move_slider(track)

if __name__ == "__main__":
    jd = JD_Login()
    jd.main()

# 关闭页面
# driver.quit()
