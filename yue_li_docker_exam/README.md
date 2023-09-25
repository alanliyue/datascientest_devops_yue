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


## Tests

### Authentication

In this first set of tests, we will verify the correctness of the authentication logic. To do this, we need to make GET requests to the `/permissions` endpoint. We know that two users, Alice and Bob, exist with passwords "wonderland" and "builder," respectively. We will also attempt a third test with a password that does not work: "clementine" and "mandarine."

- The first two requests should return a 200 status code, indicating successful authentication.
- The third request should return a 403 status code, indicating authentication failure.

### Authorization

In this second set of tests, we will validate the correctness of user access rights management. We know that Bob has access only to the `/v1` endpoint, while Alice has access to both versions. For each user, we will make requests to the `/v1/sentiment` and `/v2/sentiment` endpoints. For each request, we need to provide the following arguments: `username`, `password`, and `sentence` containing the phrase to analyze.

- Bob's requests should return the expected results based on his limited access.
- Alice's requests should return the expected results for both versions.

### Content

In this final set of tests, we will ensure that the API functions as expected. We will test the following phrases using Alice's account:

1. "life is beautiful"
2. "that sucks"

For each version of the model, we should receive a positive score for the first phrase and a negative score for the second phrase. The test will involve verifying the positivity or negativity of the score.

You can run these tests to verify the correctness and functionality of the Sentiment Analysis API.

For details on how to perform these tests manually, please refer to the "Getting Started" section in the README.

This addition to your README.md will provide information about the tests for authentication, authorization, and content, guiding users on how to perform them and what results to expect.


## Test pipeline
- Create images for 3 testing scenarios using 3 different Dockerfile
- Use docker-compose.yml for launching one by one these containers
- Run setup.sh to build images and launch the whole test pipeline

## Test Results
The test results are merged in the single file api_test.log
