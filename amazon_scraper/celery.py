import os
from celery import Celery
from decouple import config
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amazon_scraper.settings')
app = Celery(
    "amazon_scraper",
    broker=config("REDIS_URL"),
    backend=config("REDIS_URL"),
    redbeat_redis_url=config("REDIS_URL"),
    broker_connection_retry_on_startup=True,
)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    "update_brand_products": {
        "task": "update_brand_products",
        "schedule": crontab(minute=0, hour="0,6,12,18"),
    },
}
