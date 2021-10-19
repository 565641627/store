'''操作类'''
import time

from appium.webdriver.common.touch_action import TouchAction
class loginOpera:
    def __init__(self,driver):
        self.driver=driver

    def login(self,username,password):
        TouchAction(self.driver).tap(x=613, y=1016).perform()
        time.sleep(5)
        self.driver.tap([(55,90)])
        time.sleep(5)
        TouchAction(self.driver).tap(x=396, y=1404).perform()
        time.sleep(8)
        el1 = self.driver.find_element_by_id("com.sina.weibo:id/et_login_view_uname")
        el1.send_keys(username)
        el2 = self.driver.find_element_by_id("com.sina.weibo:id/et_login_view_psw")
        el2.send_keys(password)
        TouchAction(self.driver).tap(x=91, y=1464).perform()
        time.sleep(2)
        TouchAction(self.driver).tap(x=770, y=669).perform()
        time.sleep(2)

    def get_succes_data(self):
        try:
            data = self.driver.find_element_by_id("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.TabHost/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView").text
        except Exception:
            data = self.driver.find_element_by_id("com.sina.weibo:id/tv_login_view_tips").text
        return data

    def get_error_data(self):
        try:
            data = self.driver.find_element_by_id("com.sina.weibo:id/tv_login_view_tips").text
        except Exception:
            data = self.driver.find_element_by_id("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.TabHost/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView").text
        return data











