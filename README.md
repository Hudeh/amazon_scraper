# Amazon Scraper API

This project provides a an api to scrape amazon base on specific brand.

## Getting Started

### Prerequisites

- Python 3.x
- Docker
- Docker Compose
- Redis
- PostgreSQL

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Hudeh/amazon_scraper.git
   cd amazon_scraper
   ```

2. **Configure environment variables:**

   Rename env_sample to .env and update the values as needed:

   ```bash
   mv env_sample .env
   ```

### Running the Project

Using Docker Compose
The easiest way to run the project is by using Docker Compose, which will set up all services automatically

1. **Build and start services:**

   ```bash
   docker-compose build
   ```

2. **Run container:**

    ```bash
    docker-compose up
    ```

3. **Add the Task to Django Admin**

    Create a PeriodicTask in the Django Admin:
    Navigate to Periodic Tasks (under django-celery-beat).

    Create a new periodic task:

    Name: Update Brand Products
    Task: products.tasks.update_brand_products
    Set a Crontab Schedule:

    In the Django Admin, go to Crontab Schedule under django-celery-beat.
    Add a new schedule with:
    Minute: 0
    Hour: 0,6,12,18 (this will run the task 4 times a day at midnight, 6 AM, noon, and 6 PM).
    Day of Month: *
    Month:*
    Day of Week: *
    Go back to your Periodic Task and associate it with the newly created crontab schedule.
