from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

carts = []
with open('data/carts.json', 'r') as file:
    data = json.load(file)
    carts = data['carts']


@app.route('/')
def home():
    return render_template('index.html')

# Get history
# curl -X GET http://localhost:5000/api
@app.route('/api')
def get_all():
    return records
