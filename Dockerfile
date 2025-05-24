# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Set PYTHONPATH environment variable to help Python find modules
ENV PYTHONPATH=/app/src

# Copy requirements files first (for better caching)
COPY requirements.txt requirements-dev.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements-dev.txt

# Copy the entire src folder into /app/src in the container
COPY src ./src

# Default command to run your CLI app
CMD ["python", "-m", "src.main"]
