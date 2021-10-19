from appium import webdriver
import time

url = '127.0.0.1:4723/wd/hub'
param = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.ss.android.ugc.aweme",
    "appActivity": "splash.SplashActivity"
}

driver = webdriver.Remote(url, param)
time.sleep(5)
driver.tap([(440,974)])
time.sleep(3)
for i in range(10):
  driver.swipe(450,1100,450,300,500)
  time.sleep(5)
driver.quit()
