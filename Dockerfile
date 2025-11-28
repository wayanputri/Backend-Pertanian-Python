# Gunakan Python versi ringan
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy semua file project
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Default command (docker-compose akan override)
CMD ["python", "app_http.py"]
