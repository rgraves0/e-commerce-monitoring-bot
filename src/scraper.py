import random
import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)"
]

async def get_price(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent=random.choice(USER_AGENTS)
        )
        page = await context.new_page()
        await stealth_async(page)

        await page.goto(url, timeout=60000)
        await asyncio.sleep(random.uniform(3, 6))

        price = None

        try:
            if "shopee" in url:
                price = await page.locator("div[class*=product-price]").inner_text()
            elif "lazada" in url:
                price = await page.locator("span[class*=pdp-price]").inner_text()
            elif "tiktok" in url:
                price = await page.locator("span[class*=price]").inner_text()
        except:
            pass

        await browser.close()
        return price
