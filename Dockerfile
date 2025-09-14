FROM python:3.11-slim as build

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Install curl + fix line endings for test.sh
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
RUN sed -i 's/\r$//' test.sh && chmod +x test.sh

# Default run command
CMD ["python", "app.py"]
