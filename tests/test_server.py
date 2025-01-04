import json
import requests

# Define the base URL for the Flask app
BASE_URL = 'http://localhost:5000'

# Test GET /api/carts endpoint
def test_get_carts():
    response = requests.get(f'{BASE_URL}/api/carts')
    
    assert response.status_code == 200  # Check if status code is 200
    carts = response.json()  # Convert response to JSON
    
    assert isinstance(carts, list)  # Check if response is a list
    if carts:
        assert 'user_id' in carts[0]  # Check if 'user_id' exists in first cart

# Test POST /api/carts endpoint
def test_create_cart():
    new_cart = {
        'user_id': 1,
        'items': [{'product_id': '6777ab1a9a51b49961e628ec', 'quantity': 2}]
    }

    response = requests.post(f'{BASE_URL}/api/carts', json=new_cart)
    
    assert response.status_code == 201  # Check if status code is 201 (Created)
    message = response.json().get('message')
    assert message == 'Cart created'  # Check if the message is correct
    cart_id = response.json().get('cart_id')
    requests.delete(f'{BASE_URL}/api/carts/{cart_id}')

# Test PUT /api/carts endpoint (update existing cart)
def test_update_cart():
    updated_cart = {
        'user_id': 1,
        'items': [{'product_id': '6777aa9f9a51b49961e628eb', 'quantity': 3}]
    }

    response = requests.post(f'{BASE_URL}/api/carts', json=updated_cart)
    
    assert response.status_code == 200  # Check if status code is 200 (OK)
    message = response.json().get('message')
    assert message == 'Cart updated'  # Check if the message is correct

# Test DELETE /api/carts/{cart_id} endpoint
def test_delete_cart():
    # First create a cart to delete
    new_cart = {
        'user_id': 2,
        'items': [{'product_id': '6777ab1a9a51b49961e628ec', 'quantity': 1}]
    }
    create_cart_response = requests.post(f'{BASE_URL}/api/carts', json=new_cart)
    cart_id = create_cart_response.json().get('cart_id')

    # Delete the cart
    response = requests.delete(f'{BASE_URL}/api/carts/{cart_id}')
    assert response.status_code == 200  # Check if status code is 200 (OK)
    message = response.json().get('message')
    assert message == 'Cart deleted'  # Check if the message is correct

# Test GET /api/products endpoint
def test_get_products():
    response = requests.get(f'{BASE_URL}/api/products')
    
    assert response.status_code == 200  # Check if status code is 200
    products = response.json()  # Convert response to JSON
    
    assert isinstance(products, list)  # Check if response is a list
    if products:
        assert '_id' in products[0]  # Check if '_id' exists in the first product

# Test GET /api/products/{product_id} endpoint
def test_get_product_by_id():
    response = requests.get(f'{BASE_URL}/api/products/6777aa9f9a51b49961e628eb')
    
    assert response.status_code == 200  # Check if status code is 200
    product = response.json()  # Convert response to JSON
    
    assert '_id' in product  # Check if 'id' exists in the product
    assert product['_id'] == '6777aa9f9a51b49961e628eb'  # Check if product ID matches

# Test GET /api/products/{product_id} endpoint for non-existent product
def test_get_non_existent_product():
    response = requests.get(f'{BASE_URL}/api/products/9999')
    
    assert response.status_code == 404  # Check if status code is 404
    message = response.json().get('message')
    assert message == 'Product not found'  # Check if the message is correct
