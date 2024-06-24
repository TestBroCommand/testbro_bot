# Use an official Python image as the base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot code
COPY . .

ENV db_path="."
ENV TOKEN="7472757134:AAHH3neHCGlOIcPtUgJg_X3Lc2StfnFCIKw"

# Run the bot when the container starts
CMD ["python", "main.py"]
