from queueBypassLinkGrabber import getBypassLink
import time
from discord_webhook import DiscordWebhook
import asyncio
from playwright.async_api import async_playwright
shopURL="https://www.capsuletoronto.com/"
bypassURL=""
async def run(playwright):
    # create a chromium browser instance
    chromium = playwright.chromium
    browser = await  chromium.launch(headless=False, 
    proxy={
    "server": "81.200.148.5:3190",
    "username": "hp7u1otc",
    "password": "0k6h0cga"
    }
    )
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto(getBypassLink())

    time.sleep(0.5)
    bypassURL=page.url
    await page.goto(shopURL+"/cart")
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/985673989181567008/R9MJjtrJ7fwBibWU1fwk7hdx5NiiMC2mx6NmEBY6s_uP9uM2B9fAdyIG6MWOjw0dagLi', content="Bypass Link: "+bypassURL)
    response = webhook.execute()
    await page.goto("https://www.capsuletoronto.com/cart/change?line=1&quantity=0")
    time.sleep(0.5)
    await page.goto(shopURL+"/cart")
    time.sleep(360)
    # create pages and interact with contexts independently

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())