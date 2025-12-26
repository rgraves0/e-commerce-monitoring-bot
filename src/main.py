import os
import asyncio
import time
from dotenv import load_dotenv
from scraper import get_price
from telegram_bot import send_message

load_dotenv()

PRODUCT_URLS = os.getenv("PRODUCT_URLS").split(",")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 1800))

last_prices = {}

async def monitor():
    while True:
        for url in PRODUCT_URLS:
            price = await get_price(url)

            if not price:
                continue

            if url not in last_prices:
                last_prices[url] = price
                continue

            if price != last_prices[url] or "0" in price:
                msg = f"🔥 Price Changed!\n{url}\n💰 {price}"
                await send_message(msg)
                last_prices[url] = price

            await asyncio.sleep(5)

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    asyncio.run(monitor())
