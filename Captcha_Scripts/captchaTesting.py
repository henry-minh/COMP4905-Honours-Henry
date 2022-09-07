import time
import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    # create a chromium browser instance
    chromium = playwright.chromium
    browser = await  chromium.launch(headless=False)
    context = await browser.new_context()
    page1 = await context.new_page()
    page2 = await context.new_page()
    await page1.goto("https://example.com")
    await page2.goto("https://patrickhlauke.github.io/recaptcha/")
    # create two isolated browser contexts
    #user_context = browser.new_context()
    #admin_context = browser.new_context()
    time.sleep(100)
    # create pages and interact with contexts independently

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())