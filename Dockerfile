# Use official Python image
FROM python:3.11.2-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory inside the container
WORKDIR /code


# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip && \ 
pip install --no-cache-dir -r requirements.txt

# Copy entrypoint.sh
COPY ./entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r$//g' /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Copy application code
COPY . /code


# Set entrypoint
ENTRYPOINT ["/entrypoint.sh"]
