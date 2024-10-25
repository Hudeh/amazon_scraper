import logging
from django.core.cache import cache
from celery import shared_task
from .models import Brand, Product
from .scraper import scrape_amazon_products

# Set up logging
logger = logging.getLogger(__name__)

CACHE_TIMEOUT = 60 * 60  # 1 hour


@shared_task(name="update_brand_products", bind=True, max_retries=3)
def update_brand_products(self):
    all_brands = Brand.objects.all()
    total_updated = 0

    for brand in all_brands:
        try:
            # Generate cache key using brand ID to avoid naming conflicts
            cache_key = f"brand_products_{brand.id}"
            products_data = cache.get(cache_key)

            if not products_data:
                # Scrape products and store in cache
                products_data = scrape_amazon_products(brand.name)
                cache.set(cache_key, products_data, CACHE_TIMEOUT)

            updated_count = 0
            for data in products_data:
                _, created = Product.objects.update_or_create(
                    asin=data["asin"],
                    defaults={
                        "name": data["name"],
                        "image": data["image"],
                        "sku": data.get("sku", ""),
                        "brand": brand,
                    },
                )
                if not created:
                    updated_count += 1

            total_updated += updated_count
            logger.info(f"Updated {updated_count} products for brand '{brand.name}'.")

        except Exception as exc:
            logger.error(f"Error updating products for brand '{brand.name}': {exc}")

    logger.info(f"Total updated products across all brands: {total_updated}")
