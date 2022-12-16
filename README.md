# Henry Nguyen Honours Project

### Shopify Checkout Automation Tool

<p>The purpose of this project is to highlight the prevalence and prevention of scalping attacks in the
E-Commerce ecosystem. During project develpment, I will be showcasing the importance of balancing web traffic protection and how bots depleting limited product negatively impact real customers and could negatively effect web server performance.</p>

### Video Demo 📺
- https://youtu.be/SrWzTO-cDCE

### Features ✨

- Product Monitoring (Webscraping)
- Profile Creation
- Proxy Creation
- Shopify Queue Bypass Implementation
- Discord Checkout Notification Integration

### Important Notes 📝

- The captchas tab in the UI was not implemented
- The one profile checkout option was not implemented (Originally meant to prevent multiple orders on the same credit card)
- Payment information must be input in a valid format (AMEX, Mastercard,Visa). Dummy cards can be used here: https://www.paypalobjects.com/en_GB/vhelp/paypalmanager_help/credit_card_numbers.htm
- If the email used in a profile has been used with the ShopPay services in the past it must be unbinded for the software to work. Opt out here: https://shop.app/opt-out
- Right before the final checkout submission, the user will be redirected to one the order confirmation page of one of my past Shopify online purchases to simulate the checkout flow without making the user have to purchase something.
- Selenium needs the user to download the latest chrome driver, add it to their enviornment variables, and place it outside the GUI directory (place with this README).
The latest chrome driver can be downloaded here: https://sites.google.com/a/chromium.org/chromedriver/downloads
- A discord webhook must be setup for the software to work. If you want to change the Discord webhook key I provided by default, follow the instructions in the Technical Guide section of this README

### File Details 📚
- main.py - Launch the GUI from here
- onLoadFunctions.py - Loads the information from settings.json in the GUI
- taskFunctions.py - Create, Update, Delete Tasks 
- taskStartStopFunctions.py - Functionality for when tasks are running
- profileFunctions.py - Create, Update, Delete profiles
- proxyFunctions.py - Create, Update, Delete proxy groups
- settingFunctions.py - Create/Edit a discord webhook
- settings.json - json containing information on the saved tasks, profiles, proxies, and discord webhook
- interface.ui  -UI file main uses to load the GUI
- interface.py  -py file for interface.ui, used to load the GUI

### Guide To Shopify 📁

- <p><a href="https://docs.google.com/presentation/d/1sz8ChZtQNIseWiH6DCc-wJ791BlAlRy8oH1arS1TfHI/edit?usp=sharing">Shopify Guide</a></p>

### Technical Guide 🛠

- <p><a href="https://docs.google.com/document/d/1TjBO5ME-s_Xvvzj3_z5gz0XJhiPSwRK_Nzy4KqFQHkM/edit?usp=sharing">Bandit AIO Guide</a></p>

### Programmed Using 💻

<p align="left">
<a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" width="36" height="36" alt="Python" /></a>
</p>

- Python 3.9

### Software Frameworks & Libraries 📀

<p align="left"> <a href="https://playwright.dev/python/docs/intro" target="_blank" rel="noreferrer"><img src="https://yt3.ggpht.com/9y13pxP3xxovml6W83D4Kbq4joCA-WaKy01i1BAihK6315sPq7z_oTIa3YdGa7ws4k4aaRbf=s900-c-k-c0x00ffffff-no-rj" width="32" height="32" /></a><a href="https://requests.readthedocs.io/en/latest/" target="_blank" rel="noreferrer"><img src="https://upload.wikimedia.org/wikipedia/commons/a/aa/Requests_Python_Logo.png" width="32" height="32" /></a><a href="https://pypi.org/project/discord-webhook/" target="_blank" rel="noreferrer"><img src="https://pypi.org/static/images/logo-small.95de8436.svg" width="32" height="32" /></a><a href="https://pypi.org/project/PyQt6/" target="_blank" rel="noreferrer"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Python_and_Qt.svg/1200px-Python_and_Qt.svg.png" width="32" height="32" /></a></p>

- Selenium 4.5 (web browser automation)
- Selenium-wire 5.10 (Selenium proxy support for user password authenticated IP’s)
- PyQt6 6.3.1 (GUI library)
- Requests 2.28.1 (web scraping the product ID)
- PyQt6-tools 6.1.0.1.2
- Discord-webhook 0.17.0 (Discord notifications for checkouts)

### Other Tools Used Throughout the Project 💿
- Windows 10
- Visual Studio Code 1.73.1 (IDE)
- qt6-applications (GUI creation environment for PyQt6 UI files)
- qt-6tools (qt designer environment for PyQt6 UI files)
- 2captcha-python 1.1.2 (testing auto image recognition captcha solving)
