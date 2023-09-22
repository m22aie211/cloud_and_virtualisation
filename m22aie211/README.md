# Clone the Source Code 
git clone https://github.com/m22aie211/cloud_and_virtualisation.git
cd m22aie211

# Project Structure
m22aie211/
├── app.py            # Web application code
├── requirements.txt  # Python dependencies
├── Dockerfile        # Dockerfile for building the image
├── README.md         # README file

# Dockerization
We have used a custom Docker image built from a Linux OS base image (Ubuntu 20.04). The Dockerfile performs below steps
1. installs system dependencies
2. sets up a working directory
3. copies the application code and dependencies
4. exposes the necessary port.

# pushing source codes to git repo
git add .gitignore app.py Dockerfile requirements.txt README.md
git commit -m "Added the source code for Dcokerisation assignment"
git push origin main

# Building Docker Image
docker build -t docker_assignment .
# Deploying Docker Image
docker run -d -p 5050:5050 docker_assignment
# Accessing API end points 
curl -X GET http://localhost:5050/health
curl -X GET http://localhost:5050/get_cata
curl -X POST -H "Content-Type: application/json" -d '{
	"transaction_id": "1234567890",
	"amount": 100.00,
	"currency": "USD",
	"payment_method": "credit_card",
	"card_number": "1234-5678-9876-5432",
	"expiry_date": "12/24",
	"cvv": "123"
}' http://localhost:5050//insert

# App Functionality 
This app is having below 3 end points

1. Health Check - Checks if the web app is up and running. 
   1.1 response code 200 
2. Insert record - This is a POST method which can be invoked with a JSON payload which will insert the json data to Mongo DB collection.
	Response codes
	2.1 201 - If data gets inserted successfully
	2.2 400 - If no data is provided as payload
   	2.3 500 - If any internal server error
3. Get Data - This is a GET method which can be invoked to get the data from Mongo collection.
	Response codes
	3.1 200 - If Data gets fetched successfully
    3.2 404 - If there is no data in the mongo collection 
    3.3 500 - If any internal server error
# Check logs of deployed application
docker logs -f <CONTAINER ID>
# List Down docker processes running
docker ps
# Stopping the Docker process
docker stop <CONTAINER ID>

# Author
Author Name: Krupamay ghosal
GitHub: https://github.com/m22aie211/cloud_and_virtualisation.git
Email: m22aie211@iitj.ac.in

