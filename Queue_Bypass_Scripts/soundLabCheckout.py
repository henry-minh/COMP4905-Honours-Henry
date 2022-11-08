from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from solveRecaptcha import solveRecaptcha
PATH = "C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)


browser.get('https://www.google.com/recaptcha/api2/demo')

start= time.time()
result=solveRecaptcha(
    "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-",
    "https://www.google.com/recaptcha/api2/demo"
)
#print(result)

code=result['code']
print(code)



WebDriverWait(browser,10).until(
    EC.presence_of_element_located((By.ID, 'g-recaptcha-response'))
)
browser.execute_script(
    "document.getElementById('g-recaptcha-response').innerHTML = " + "'" + code + "'"
    )
browser.find_element(By.ID, "recaptcha-demo-submit").click()
end= time.time()
executionTime=end-start
print("Google ReCaptcha Solved in: "+str(executionTime)+" seconds")
time.sleep(120)
"""
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)

# to maximize the browser window
driver.maximize_window()
#get method to launch the URL

driver.get("https://www.google.com/recaptcha/api2/demo")
time.sleep(20)

#to close the browser
driver.close()
"""