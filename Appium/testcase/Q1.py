
import time
import os
import logging
import logging.config
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from appium.webdriver import Remote
from appium.webdriver.webelement import WebElement as MobileWebElement
from selenium.webdriver.common.keys import Keys
from appium.webdriver.extensions.android.nativekey import AndroidKey
 
CON_LOG='log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

class AppiumClient:
    def __init__(self, os_name: str, os_version: str, device_name: str):
        self.caps = dict()
        self.caps['platformName'] = os_name
        self.caps['platformVersion'] = os_version
        self.caps['deviceName'] = device_name
        self.caps['resetKeyboard'] = True
        self.caps['unicodeKeyboard'] = False # 使用自带输入法，输入中文时填True
        #self.driver: Remote = None
        
    def __del__(self):
        if self.driver:
            self.driver.quit()
 
    def launch_app(self, package: tuple = None, app_path=''):
        """
        :param package: tuple (appPackage, appActivity)
        :param app_path: apk path in PC
        :return:
        """
        try:
            if app_path:
                self.caps['app'] = app_path
            if package:
                self.caps['appPackage'] = package[0]
                self.caps['appActivity'] = package[1]
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.caps)
            self.driver.implicitly_wait(10)
            time.sleep(9) 
            return True
        except Exception as e:
            print(str(e))
            return False
 
    def find_element(self, who: str, by: str):
        logging.info('***** look for %s by %s *****' % (who, by))
        time.sleep(3) 
        element: MobileWebElement = self.driver.find_element(by, who)
        return element

    def find_all_element(self, who: str, by: str):
        logging.info('***** look for %s by %s *****' % (who, by))
        time.sleep(3)
        new = who + "*[not(*)]"
        print (new)
        elements = self.driver.find_element(by, new) ##"//*[not(*)]"
        #element: MobileWebElement = self.driver.find_element(by, who)
        return elements

    def get_element_list(self):
        element_list = []
        logging.info('***** look for elements *****')
        time.sleep(3)
        who = "//android.view.View[@resource-id='lnk_Link']"
        list = self.driver.find_elements(By.XPATH,who)
        if list:
            for value in list:
                ele_name = value.get_attribute("content-desc")
                element_list.append(ele_name)
            return (element_list)
        else:
            return False

    def click(self, who: str, by=AppiumBy.ID):
        logging.info('***** look for %s by %s then click *****' % (who, by))
        time.sleep(8)
        element = self.find_element(who, by)
        if element:
            logging.info('***** click %s *****' % element)
            element.click()
            time.sleep(8)
            return True
        else:
            return False
 
    def input(self, text: str, who: str, by=AppiumBy.ID):
        element = self.find_element(who, by)
        if element:
            logging.debug("所有可用的输入法：",self.driver.available_ime_engines)
            logging.debug("当前正在使用的输入法：",self.driver.active_ime_engine)
            logging.debug("切换输入法到 io.appium.settings/.UnicodeIME")
            self.driver.activate_ime_engine('io.appium.settings/.UnicodeIME')
            logging.debug("当前正在使用的输入法：",self.driver.active_ime_engine)
            logging.info("***** Click search box *****")
            element.click()
            logging.info("***** Send text %s *****" % text)
            element.send_keys(text)
            logging.info("***** Press Enter *****")
            self.driver.press_keycode(AndroidKey.ENTER)
            time.sleep(20)
            return True
        else:
            return False
 
    def back(self):
        logging.info('***** back *****')
        self.driver.back()
 
    def wait_element(self, who: str, by=AppiumBy.ID, time_out=30):
        for i in range(time_out):
            element = self.find_element(who, by)
            if element:
                return True
            else:
                logging.info('***** sleep 1s wait for %s *****' % who)
                time.sleep(1)
        logging.info('***** wait %s more than %ds*****' % (who, time_out))
        return False
 
    def get_attributes(self, who: str, by=AppiumBy.ID):
        element = self.find_element(who, by)
        if element:
            attributes = dict()
            attributes['checkable'] = element.get_attribute('checkable')
            attributes['long-clickable'] = element.get_attribute('long-clickable')
            attributes['clickable'] = element.get_attribute('clickable')
            attributes['checked'] = element.get_attribute('checked')
            attributes['selected'] = element.get_attribute('selected')
            attributes['text'] = element.get_attribute('text')
            attributes['focused'] = element.get_attribute('focused')
            return attributes
        else:
            return None
 
    def print_all_element(self):
        logging.info(self.driver.page_source)

    def screenshot(self,name):
        logging.info('***** Capture Screen *****')
        self.driver.get_screenshot_as_file(os.getcwd() + '/'+ name +'.png')
 
 
if __name__ == "__main__":
    function_btn= "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]" ##//img[2]' 
    product_btn = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View" ## xpath=(.//*[normalize-space(text()) and normalize-space(.)='海外據點'])[1]/following::div[6]
    card = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[1]"
    card_link = '//android.view.View[@content-desc="卡片介紹"]/android.widget.TextView'
    card1 = "(.//*[normalize-space(text()) and normalize-space(.)='EN'])[1]/following::p[10]"  ##xpath=(.//*[normalize-space(text()) and normalize-space(.)='EN'])[1]/following::p[10]
    '''function4 = "(.//*[normalize-space(text()) and normalize-space(.)='EN'])[1]/following::p[10]"  ##xpath=(.//*[normalize-space(text()) and normalize-space(.)='EN'])[1]/following::p[10]
    function5 = "(.//*[normalize-space(text()) and normalize-space(.)='EN'])[1]/following::p[9]"##xpath=(.//*[normalize-space(text()) and normalize-space(.)='EN'])[1]/following::p[9]"
    function6 = "(.//*[normalize-space(text()) and normalize-space(.)='EN'])[1]/following::p[9]"  ##xpath=(.//*[normalize-space(text()) and normalize-space(.)='EN'])[1]/following::p[9]'''
    client = AppiumClient('Android', '7.1.2', '127.0.0.1:62001')
    #client.launch_app(('com.android.chrome', 'com.google.android.apps.chrome.Main'))
    client.launch_app(('com.android.browser', 'com.android.browser.BrowserActivity'))
    #client.click('com.android.chrome:id/terms_accept')
    #client.input('https://www.cathaybk.com.tw/cathaybk/','com.android.chrome:id/search_box_text')
    client.input('https://www.cathaybk.com.tw/cathaybk/','com.android.browser:id/url')
    client.screenshot("homepage")
    client.click(function_btn,AppiumBy.XPATH)
    client.click(product_btn,AppiumBy.XPATH)
    client.click(card,AppiumBy.XPATH)
    client.screenshot("card_list")
    print(client.get_element_list())
    #print(client.get_attributes(card,AppiumBy.XPATH))
    #client.click(card_link,AppiumBy.XPATH)
    #client.click(card1,AppiumBy.XPATH)
    #client.screenshot("card_1")
    '''client.click(link)
    client.click(function3,AppiumBy.XPATH)
    client.click(function4,AppiumBy.XPATH)
    client.click(function5,AppiumBy.XPATH)
    client.click(function6,AppiumBy.XPATH)'''
    #client.screenshot()