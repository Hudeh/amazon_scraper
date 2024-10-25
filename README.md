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
