# Use the official Python image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install curl and other dependencies
RUN apt-get update && apt-get install -y curl
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Run the application
CMD ["python", "app.py"]