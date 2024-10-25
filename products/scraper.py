import requests
from bs4 import BeautifulSoup
import random
import time
import logging

logger = logging.getLogger(__name__)

HEADERS = [
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"},
    {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"},
    {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"},
]

def scrape_amazon_products(brand_name):
    """
    Scrapes Amazon for products matching a specific brand name.
    Returns a list of product dictionaries with name, ASIN, SKU, and image URL.
    """
    base_url = f"https://www.amazon.com/s?k={brand_name}"
    products = []

    try:
        # Handle pagination
        page = 1
        while True:
            logger.info(f"Scraping page {page} for brand: {brand_name}")
            url = f"{base_url}&page={page}"
            
            headers = random.choice(HEADERS)
            response = requests.get(url, headers=headers)

            if response.status_code != 200:
                logger.error(f"Failed to retrieve page {page}. Status code: {response.status_code}")
                break

            soup = BeautifulSoup(response.content, "html.parser")

            # Parse product data
            product_elements = soup.find_all("div", {"data-component-type": "s-search-result"})

            if not product_elements:
                logger.info(f"No more products found on page {page}. Stopping pagination.")
                break

            for element in product_elements:
                try:
                    # Extract product details
                    name = element.h2.text.strip()
                    asin = element["data-asin"]
                    sku = element.get("data-sku", "")
                    image = element.find("img")["src"]

                    products.append({
                        "name": name,
                        "asin": asin,
                        "sku": sku,
                        "image": image,
                    })
                except Exception as e:
                    logger.error(f"Error parsing product element: {e}")
                    continue

            page += 1
            time.sleep(random.uniform(1, 3))

    except Exception as e:
        logger.error(f"Error scraping Amazon for brand {brand_name}: {e}")

    return products
