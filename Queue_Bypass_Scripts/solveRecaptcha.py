from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os
from seleniumwire import webdriver

chromePath = 'Queue_Bypass_Scripts\chromedriver.exe'
optionsDebug = webdriver.ChromeOptions()
optionsDebug.add_experimental_option('excludeSwitches', ['enable-logging'])
sessionUrl=None

browser = webdriver.Chrome(chromePath,options=optionsDebug) # Add option for Proxy
browser.get('https://www.google.com/recaptcha/api2/demo')
captchaOrCheckoutFlag=False


try:
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".g-recaptcha")))
    # There is a Captcha that needs to be solved
    captchaSolved=False
    while captchaSolved==False:
        try:
            #This would be replaced with a checkout page element
            WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".recaptcha-success")))
            print("Captcha Successfully solved")
            captchaSolved=True
        except:
            print("captcha not solved yet")
except:
    print("No Captcha => We should be on checkout page 1")
print("Checkout Page 1")
time.sleep(10)
browser.quit()


#hcaptcha variant: use class: h-captcha
#https://www.plesk.com/test-hcaptcha/

#need to change where it loops and looks for an hcaptcha, g-recaptcha, and id checkout_email to determine