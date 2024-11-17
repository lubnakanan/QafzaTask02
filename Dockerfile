# Use the official Python slim image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY app01.py /app/
COPY IDRequest.py /app/
COPY simple_xgboost.csv /app/

# Expose the application port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app01:app", "--host", "0.0.0.0", "--port", "8000"]
