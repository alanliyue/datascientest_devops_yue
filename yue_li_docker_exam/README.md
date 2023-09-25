# API Testing using CI/CD pipeline
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
This project is to use a CI/CD pipeline to automate testing APIfor which predicts sentiment in English phrases.

## Overview

This project showcases a Sentiment Analysis API that predicts whether an English sentence has a positive or negative sentiment. The API is deployed within a Docker container using the image `datascientest/fastapi:1.0.0`.

### API Endpoints

The API exposes the following endpoints:

1. **/status**:
   - Returns `1` if the API is functioning correctly.
   
2. **/permissions**:
   - Returns the user's permissions based on their provided username and password.
   
3. **/v1/sentiment**:
   - Returns sentiment analysis using an older model.
   
4. **/v2/sentiment**:
   - Returns sentiment analysis using a newer model.
   
### API Availability

The API is accessible on port 8000 of the host machine.

### API Documentation

For detailed descriptions of the API endpoints, visit the `/docs` endpoint. This interactive documentation provides information on how to use each API endpoint, including request parameters and expected responses.

To access the API documentation, open a web browser and navigate to the following URL:

```http
http://your-host-machine:8000/docs
```
## API Usage

### /status Endpoint

- Use this endpoint to verify the API's functionality.

```http
GET /status
```

## Getting Started

To get started with the Sentiment Analysis API, follow these steps:

### Step 1: Download the Docker Image

To download the Docker image, run the following command:

```bash
docker image pull datascientest/fastapi:1.0.0

docker container run -p 8000:8000 datascientest/fastapi:1.0.0
```
