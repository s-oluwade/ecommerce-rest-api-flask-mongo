# Ecommerce REST API with Flask and MongoDB

## Features

Cart Management: Create, retrieve, update, and delete carts.
Product Management: Create, and retrieve products.
CI/CD Deployment: Automated deployment to Azure App Service as a docker container using Azure Pipelines.
Testing: Automated Testing with pytest.

## API Endpoints

### Carts:
`GET /carts: Retrieve all carts.
POST /carts: Create a new cart.
DELETE /carts/<product_id>: Delete a cart.`

### Products:
`GET /products: Retrieve all products.`

`GET /products/<product_id>: Retrieve a specific product by ID.`
`POST /products: Create a new product.`

## Local Installation

## Clone 
git clone https://github.com/s-oluwade/ecommerce-rest-api-flask-mongo.git
cd ecommerce-rest-api-flask-mongo

## Set Up a Virtual Environment
python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`

## Install Dependencies
pip install -r requirements.txt

## Configure Environment Variables
MONGODB_URI=mongodb://localhost:27017/ecommerce_db
FLASK_ENV=development
SECRET_KEY=your_secret_key_here

## Test
pytest tests/

## Build (if deploying in docker)
docker-compose build

## Deployment
python server.py or docker-compose up (if deploying in docker)
