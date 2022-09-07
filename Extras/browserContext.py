import time
import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    # create a chromium browser instance
    chromium = playwright.chromium
    browser = await  chromium.launch_persistent_context(headless=False, proxy={
    "server": "81.200.148.5:3190",
    "username": "hp7u1otc",
    "password": "0k6h0cga"
    })
    context = await browser.new_context()
    page1 = await context.new_page()
    page2 = await context.new_page()
    await page1.goto("https://youtube.com")
    await page2.goto("https://www.deadstock.ca/6163517/checkouts/b40aff6e3973a040db39afaf0c369e5e")
    # create two isolated browser contexts
    #user_context = browser.new_context()
    #admin_context = browser.new_context()
    time.sleep(5)
    browser.close()
    # create pages and interact with contexts independently

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())