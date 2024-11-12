# Use a lightweight Python image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source files
COPY . .

# Command to run the application
CMD ["python", "src/app.py"]
