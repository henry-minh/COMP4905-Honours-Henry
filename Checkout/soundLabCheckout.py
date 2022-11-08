import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, 
    proxy={
    "server": "81.200.148.5:3190",
    "username": "hp7u1otc",
    "password": "0k6h0cga"
    }
    )
    
    page = browser.new_page()
    page.goto('https://ml-sound-lab.com/products/amped-stevie-t-free')

    # Interact with login form
    #page.click('text=login')
    
    page.click('button[name="add"]')
    #page.click('button[aria-label="View cart"]')
    #page.click('button[name="checkout"]')
    time.sleep(1)
    page.goto('https://ml-sound-lab.com/checkout')
    time.sleep(1)
    
    #######################
    ##  Checkout Page 1  ##
    #######################

    # Email Address
    page.click('input[id="checkout_email"]')
    time.sleep(.1)
    page.fill('input[id="checkout_email"]', 'olhhxwgfgbaynruscf@nthrw.com') 
    
    
    # Billing address
    time.sleep(.1)
    page.click('input[id="checkout_billing_address_first_name"]')
    time.sleep(.1)
    page.fill('input[id="checkout_billing_address_first_name"]', 'Joe')
    time.sleep(1)

    page.select_option('select#checkout_billing_address_country', label='Canada')
    time.sleep(.1)
    page.select_option('select#checkout_billing_address_province', label='Ontario')
    time.sleep(.1)

    page.click('input[id="checkout_billing_address_last_name"]')
    time.sleep(.1)
    page.fill('input[id="checkout_billing_address_last_name"]', 'Biden')

    time.sleep(.1)
    page.click('input[id="checkout_billing_address_address1"]')
    time.sleep(.1)
    page.fill('input[id="checkout_billing_address_address1"]', '6593 Morningview St')

    time.sleep(.1)
    page.click('input[id="checkout_billing_address_city"]')
    time.sleep(.1)
    page.fill('input[id="checkout_billing_address_city"]', 'Ottawa')

    time.sleep(.1)
    page.click('input[id="checkout_billing_address_zip"]')
    time.sleep(.1)
    page.fill('input[id="checkout_billing_address_zip"]', 'K1C6P1')

    time.sleep(.1)
    page.click('button[id="continue_button"]')
    time.sleep(20)

    #######################
    ##  Checkout Page 2  ##
    #######################

    # What would be credit card information


    #checkout

    #page.click('button[id="continue_button"]')
    time.sleep(20)

