from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
import json

app = Flask(__name__)

# Enable CORS for all domains
CORS(app)

# Connect to MongoDB running in the Docker container
client = MongoClient('mongodb://mongodb:27017/')  # 'mongodb' is the service name in docker-compose
db = client['mydatabase']  # Use the database named 'mydatabase'
carts_collection = db['carts']  # Use the 'carts' collection

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/manage_cart')
def manage_cart_page():
    return render_template('add-to-cart.html')

# curl -X GET http://localhost:5000/api/carts
@app.route('/api/carts')
def get_carts():
    with open('data/carts.json', 'r') as file:
        data = json.load(file)
        print(data)
    return data

@app.route('/api/carts', methods=['POST', 'PUT'])
def manage_cart():
    data = request.get_json()

    # Validate input
    if 'user_id' not in data or 'items' not in data:
        return jsonify({'error': 'Invalid input. user_id and items are required.'}), 400

    # with open('data/carts.json', 'r') as file:
    #     carts_data = json.load(file)
    #     carts = carts_data["carts"]

    user_id = int(data['user_id'])
    # existing_cart = next((cart for cart in carts if cart['user_id'] == user_id), None)
    # Check if a cart for this user exists
    existing_cart = carts_collection.find_one({'user_id': user_id})

    if request.method == 'POST':
        if existing_cart:
            # If the cart exists, update it
            carts_collection.update_one(
                {'user_id': user_id},
                {'$set': {'items': data['items']}}
            )
            return jsonify({'message': 'Cart updated'}), 200
        else:
            # If the cart doesn't exist, create a new one
            new_cart = {
                'user_id': user_id,
                'items': data['items']
            }
            carts_collection.insert_one(new_cart)
            return jsonify({'message': 'Cart created'}), 201

    # if request.method == 'POST':
    #     # Remove any previous cart for the customer
    #     carts = [cart for cart in carts if cart['user_id'] != user_id]

    #     # Create cart
    #     new_cart = {
    #         'user_id': user_id,
    #         'cart_id': carts.count,
    #         'items': data['items']
    #     }
    #     carts.append(new_cart)
    #     response = new_cart
    #     status_code = 201  # Created

    # elif request.method == 'PUT':
    #     if not existing_cart:
    #         return jsonify({'error': 'Cart not found for the specified customer_id.'}), 404
        
    #     existing_cart['items'] = data['items']
    #     response = existing_cart
    #     status_code = 200  # OK

    # with open('data/carts.json', 'w') as file:
    #     json.dump(carts, file)

    # return jsonify(response), status_code

# curl -X DELETE http://localhost:5000/api/carts/1
@app.route('/api/carts/<int:cart_id>', methods=['DELETE'])
def delete_cart(cart_id):
    with open('data/carts.json', 'r') as file:
        carts = json.load(file)

    carts = [cart for cart in carts if cart['user_id']!= cart_id]

    with open('data/carts.json', 'w') as file:
        json.dump(carts, file)

    return jsonify({'message': 'Cart deleted'})

# get products
# curl -X GET http://localhost:5000/api/products
@app.route('/api/products')
def get_products():
    with open('data/products.json', 'r') as file:
        data = json.load(file)
        print(data)
    return data

# get product by id
# curl -X GET http://localhost:5000/api/products/1
@app.route('/api/products/<int:product_id>')
def get_product(product_id):
    with open('data/products.json', 'r') as file:
        data = json.load(file)

    for product in data:
        if product['id'] == product_id:
            return product

    return jsonify({'message': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)