from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.common.keys import Keys

chromePath = 'Queue_Bypass_Scripts\chromedriver.exe'
optionsDebug = webdriver.ChromeOptions()
optionsDebug.add_experimental_option('excludeSwitches', ['enable-logging'])

chrome_options = webdriver.ChromeOptions()
#prefs = {"profile.managed_default_content_settings.images": 2}
#chrome_options.add_experimental_option("prefs", prefs)
sessionUrl=None

browser = webdriver.Chrome(chromePath,options=optionsDebug) # Add option for Proxy



browser.get('https://deadstock.ca/cart/clear')


##############################################################
#            (Cart Random Product To Enter Queue)            #
##############################################################
browser.get('https://deadstock.ca/cart/39881710010453:1')   #This will be a random product

# If a Queue is presented Wait until we get to checkout page (Try Catch) & Store Session Url
# To Do

#If No Queue is presented, goes to checkout page right away & Store session URL then clear cart
WebDriverWait(browser, 600).until(EC.visibility_of_element_located(("id", "checkout_email")))
sessionUrl = browser.current_url
browser.get('https://deadstock.ca/cart/clear')



# Product Monitor Loop

###############################################
#            (Cart Actual Product)            # Need to test if it redirects you to the same session URL saved earlier
###############################################

browser.get('https://deadstock.ca/cart/39881710010453:1')

#If Captcha Exists, Manially Solve. If We aren't redirected loop
# To Do
checkoutPageStatus=False
while checkoutPageStatus==False:
    try:
        browser.find_element(By.ID, "checkout_email")
        checkoutPageStatus=True
    except:
        print("Solve Captcha or Checkout Page Loading")
    

#Might need to use the session url below but i don't think it's needed

#If Captcha DNE or is solved, proceed to page 1 for form filling
start= time.time()


##############################
#           Page 1           #
##############################
select = Select(browser.find_element("id", 'checkout_shipping_address_country'))
time.sleep(.0009)
select.select_by_visible_text('Canada')
time.sleep(.0009)
browser.find_element("id", "checkout_email").send_keys("joe.apple.marsh@gmail.com")
time.sleep(.0009)
browser.find_element("id", "checkout_shipping_address_first_name").send_keys("Joe")
time.sleep(.0009)
browser.find_element("id", "checkout_shipping_address_last_name").send_keys("Marsh")
time.sleep(.0009)
browser.find_element("id", "checkout_shipping_address_address1").send_keys("1750 windflower way")
time.sleep(.0009)
browser.find_element("id", "checkout_shipping_address_city").send_keys("Ottawa")
select = Select(browser.find_element("id", 'checkout_shipping_address_province'))
time.sleep(.0009)
select.select_by_visible_text('Ontario')
time.sleep(.0009)
browser.find_element("id", "checkout_shipping_address_zip").send_keys("K1C5Y5")
time.sleep(.0009)
browser.find_element("id", "checkout_shipping_address_phone").send_keys("6134248989")
time.sleep(.0009)
browser.find_element("id", "checkout_shipping_address_address2").send_keys("apt A")
time.sleep(.0009)
browser.find_element("id", "continue_button").click()

##############################
#           Page 2           #
##############################
WebDriverWait(browser, 5).until(EC.visibility_of_element_located(("id", "continue_button")))
browser.find_element("id", "continue_button").click()

##############################
#           Page 3           #
##############################
WebDriverWait(browser, 5).until(EC.visibility_of_element_located(("xpath", "//*[@title='Field container for: Card number']")))
test=browser.find_element("xpath","//*[@title='Field container for: Card number']")
iframe = browser.find_element("xpath","//*[@title='Field container for: Card number']")

browser.switch_to.frame(iframe)
time.sleep(.00009)
browser.find_element("id", "number").send_keys("378282246310005")
'''
time.sleep(.00009)
browser.find_element("id", "number").send_keys("822463")
time.sleep(.00009)
browser.find_element("id", "number").send_keys("10005")
'''
browser.switch_to.default_content()
iframe = browser.find_element("xpath","//*[@title='Field container for: Name on card']")
browser.switch_to.frame(iframe)
time.sleep(.00009)
browser.find_element("id", "name").send_keys("Joe Marsh")

browser.switch_to.default_content()
iframe = browser.find_element("xpath","//*[@title='Field container for: Expiration date (MM / YY)']")
browser.switch_to.frame(iframe)
time.sleep(.00009)
browser.find_element("id", "expiry").send_keys("02")
time.sleep(.00009)
browser.find_element("id", "expiry").send_keys("28")

browser.switch_to.default_content()
iframe = browser.find_element("xpath","//*[@title='Field container for: Security code']")
browser.switch_to.frame(iframe)
time.sleep(.00009)
browser.find_element("id", "verification_value").send_keys("9872")

time.sleep(.00009)
browser.switch_to.default_content()

#browser.find_element("id", "continue_button").click()
#Temporary Checkout Page From One of My Previous Purchases
end= time.time()
executionTime=end-start
print("Checkout Button Clikec, Checkout Execution time:")
print(executionTime)
browser.get('https://nrml.ca/13343831/orders/086a03063ea7fbebca66276c1a8b353f')
##############################
#           Page 4           #
##############################
# If we were redirected to the checkout page which will be identified with the unique class "step__footer__continue-btn btn" then we were successful
# Normally I would use the element that containing the confirmation # but it isn't shown sometimes. the continue shopping button does always occur though
#Other wise, end the process notifying the user that there was an error or the item was sold out

try:
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".step__footer__continue-btn")))
    
    confirmationUrl = browser.current_url
    print("Checkout Success, Sending Checkout Link to Discord Webhook")
    #Discord Webhook the Confirmation Page
except:
    print("Checkout Unsuccessful or Sold out")


time.sleep(10)
browser.quit()



