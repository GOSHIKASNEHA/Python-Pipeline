# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files into container
COPY . .

# Install dependencies
RUN pip install requests

# Run script
CMD ["python", "api_script.py"]