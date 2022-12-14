# Henry Nguyen Honours Project

### Shopify Checkout Automation Tool

<p>The purpose of this project is to highlight the prevalence and prevention of scalping attacks in the
E-Commerce ecosystem. During project develpment, I will be showcasing the importance of balancing web traffic protection and how bots depleting limited product negatively impact real customers while negatively effecting the web application's performance.</p>

### Features ✨

- Product Monitoring (Webscraping)
- Profile Creation
- Proxy Creation
- Shopify Queue Bypass Implementation
- Discord Checkout Notification Integration

### Additional Notes

- The captchas tab in the UI was not implemented
- The one profile checkout option was not implemented (Originally meant to prevent multiple orders on the same credit card)
- Payment information must be input in a valid format (AMEX, Mastercard,Visa). Dummy cards can be used here: https://www.paypalobjects.com/en_GB/vhelp/paypalmanager_help/credit_card_numbers.htm
- If the email used in a profile has been used with the ShopPay services in the past it must be unbinded for the software to work. Opt out here: https://shop.app/opt-out

### Guide To Shopify 📁

- <p><a href="https://docs.google.com/presentation/d/1sz8ChZtQNIseWiH6DCc-wJ791BlAlRy8oH1arS1TfHI/edit?usp=sharing">Shopify Guide</a></p>

### Technical Guide to Bandit AIO 🛠

- <p><a href="https://docs.google.com/document/d/1TjBO5ME-s_Xvvzj3_z5gz0XJhiPSwRK_Nzy4KqFQHkM/edit?usp=sharing">Bandit AIO Guide</a></p>

### PROGRAMMED IN

<p align="left">
<a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" width="36" height="36" alt="Python" /></a>
</p>

- Python 3.9

### Software FRAMEWORKS & LIBRARIES

<p align="left"> <a href="https://playwright.dev/python/docs/intro" target="_blank" rel="noreferrer"><img src="https://yt3.ggpht.com/9y13pxP3xxovml6W83D4Kbq4joCA-WaKy01i1BAihK6315sPq7z_oTIa3YdGa7ws4k4aaRbf=s900-c-k-c0x00ffffff-no-rj" width="32" height="32" /></a><a href="https://requests.readthedocs.io/en/latest/" target="_blank" rel="noreferrer"><img src="https://upload.wikimedia.org/wikipedia/commons/a/aa/Requests_Python_Logo.png" width="32" height="32" /></a><a href="https://pypi.org/project/discord-webhook/" target="_blank" rel="noreferrer"><img src="https://pypi.org/static/images/logo-small.95de8436.svg" width="32" height="32" /></a><a href="https://pypi.org/project/PyQt6/" target="_blank" rel="noreferrer"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Python_and_Qt.svg/1200px-Python_and_Qt.svg.png" width="32" height="32" /></a></p>

- Selenium 4.5 (web browser automation)
- Selenium-wire 5.10 (Selenium proxy support for user password authenticated IP’s)
- PyQt6 6.3.1 (GUI library)
- Requests 2.28.1 (web scraping the product ID)
- PyQt6-tools 6.1.0.1.2
- Discord-webhook 0.17.0 (Discord notifications for checkouts)

### Other Tools Used Throughout the Project
- Windows 10
- Visual Studio Code 1.73.1 (IDE)
- qt6-applications (GUI creation environment for PyQt6 UI files)
- qt-6tools (qt designer environment for PyQt6 UI files)
- 2captcha-python 1.1.2 (testing auto image recognition captcha solving)
