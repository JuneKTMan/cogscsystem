
from flask import Flask, request, jsonify  #flask function
import json
import product_dao
import uom_dao
import producttype_dao
import order_dao
from sql_connection import get_sql_connection
# in line 14: HTTP headers: response header indicates whether the response can be shared with requesting code from the given origin, '*" = wildcard

app = Flask(__name__)
# install in a globa veriable to call connection to sql server
connection = get_sql_connection()
# Get data use keyword 'GET'
@app.route('/getProduct', methods=['GET'])
def get_product():
    product = product_dao.get_all_product(connection)
    response = jsonify(product)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

# Update data use keyword 'POST'
@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = product_dao.delete_product(connection, request.form['product_id']) #supply data from front end to backend
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = product_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = order_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id' : order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/getProducttype', methods=['GET'])
def get_producttype():
    response = producttype_dao.get_producttype(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/getAllOrder', methods=['GET'])
def get_all_order():
    response = order_dao.get_all_order(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == "__main__":
    print("Start Python Flask Server For COGS Cafeteria Management System")
    app.run(port=5000)