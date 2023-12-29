# Farenow Remote Access API

## Description
This API is a Flask application that serves as an API service for connecting to an AWS EC2 instance. It provides functionality for interacting with the instance through HTTP requests.

## Prerequisites
Before using this API, make sure you have the following:
- An AWS account with access to EC2 instances
- An EC2 instance running on AWS

## Configuration
1. Open and edit the .env file.
2. Save the changes

## Usage
1. Start the API server: `python app.py`
2. Send HTTP requests to the API endpoints to interact with the EC2 instance.

## API Endpoints
1. Get all the services and their corresponding images
2. Get all subservices and their corresponding tables under a service 
3. Get all questions for a subservice if they have that
4. Get all available providers for the subservice in the area
5. Push the order to the database
