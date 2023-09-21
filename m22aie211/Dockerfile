# Use a base image with Linux (e.g., Ubuntu)
FROM ubuntu:20.04

# Install system dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Set the working directory in the container
WORKDIR /app

# Copy application code and dependencies to the container
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Expose the port your application will run on
EXPOSE 5050

# Command to run your application
CMD ["python3", "app.py"]
