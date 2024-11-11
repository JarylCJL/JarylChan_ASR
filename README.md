# Project Name

This project consists of an ASR (Automatic Speech Recognition) API implemented with Flask, utilizing an Elasticsearch backend and a React-based search UI.

## Project Structure
- **Backend**: ASR API with Flask, Elasticsearch for data indexing and search.
- **Frontend**: Search UI built with React.
- **Deployment**: Hosted on AWS EC2 engine

## Deployment URL & Architecture Design

The service is deployed on AWS and can be accessed at:
http://13.236.183.252

The architecture diagram for the system can be found in deployment-design under design.pdf.

## Installation

1. Install dependencies from the requirements file:
    ```bash
    pip install -r requirements.txt
    ```

## ASR API (Flask in Docker)

This API allows for ASR functionality with Flask, packaged in a Docker container.

### To Run ASR API:

1. **Build and Run Docker Image**
    ```bash
    docker build -t asr-api .
    docker run -p 8001:8001 asr-api
    ```

2. **Run ASR Text Prediction Script**
    ```bash
    python cv-decode.py
    ```
    This will generate the predicted text and store it in the `generated_text` column in `cv-valid-dev.csv`.

## Elasticsearch Backend

1. Start the Elasticsearch container by navigating to the `elastic-backend` directory and running:
    ```bash
    cd elastic-backend
    sudo docker-compose up -d
    ```

## Search UI (React in Docker)

1. Start the Search UI container by navigating to the `search-ui` directory and running:
    ```bash
    cd search-ui
    sudo docker-compose up -d
    ```

---
