from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os
from seleniumwire import webdriver
import json
import requests
from requests.auth import HTTPProxyAuth
#https://hp7u1otc:0k6h0cga@81.200.148.5:3190
url = 'https://www.google.com/recaptcha/api2/demo'
proxy  = {'http': 'hp7u1otc@0k6h0cga:81.200.148.5:3190/'}




# https://nrml.ca/cart/32318741217346:1
# https://accounts.hcaptcha.com/demo
# https://www.google.com/recaptcha/api2/demo

chromePath = 'chromedriver.exe'
optionsDebug = webdriver.ChromeOptions()
optionsDebug.add_experimental_option('excludeSwitches', ['enable-logging'])
sessionUrl=None

browser = webdriver.Chrome(chromePath,options=optionsDebug) # Add option for Proxy
browser.get(url)

start= time.time()
captchaOrCheckoutFlag=False

captchaType=None
while captchaType==None:
    try:
        browser.find_element(By.CSS_SELECTOR, ".g-recaptcha")
        captchaType="recaptcha"
        break
    except:
        try:
            browser.find_element(By.ID, "checkout_email")
            captchaType="nocaptcha"
            break
        except:
            try:
                browser.find_element(By.CSS_SELECTOR, ".h-captcha")
                captchaType="hcaptcha"
                break
            except:
                print("iterating through loop again")


if captchaType=="hcaptcha":
    print("HCaptcha Detected")
    captchaSolved=False
    while captchaSolved==False:
        try:
            WebDriverWait(browser, .05).until(EC.presence_of_element_located(("id", "checkout_email")))
            captchaSolved=True
        except:
            print("loop hcaptcha")
        

if captchaType=="recaptcha":
    print("RECaptcha Detected")
    captchaSolved=False
    while captchaSolved==False:
        try:
            WebDriverWait(browser, .05).until(EC.presence_of_element_located(("id", "checkout_email")))
            captchaSolved=True
        except:
            print("loop recaptcha")

if captchaType=="nocaptcha":
    print("No Captcha Detected")


end= time.time()
executionTime=end-start

print(executionTime)
browser.quit()