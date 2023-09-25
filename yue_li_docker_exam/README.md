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

## API Usage

### /status Endpoint

- Use this endpoint to verify the API's functionality.

```http
GET /status
