from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService

product_routes = Blueprint('product_routes', __name__)
product_service = ProductService()

@product_routes.route('/products', methods=['POST'])
def create_product():
    data = request.json
    product = product_service.create_product(data)
    return jsonify(product), 201

@product_routes.route('/products', methods=['GET'])
def get_products():
    products = product_service.get_all_products()
    return jsonify(products), 200

@product_routes.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = product_service.get_product(product_id)
    if product:
        return jsonify(product), 200
    return jsonify({'message': 'Product not found'}), 404

@product_routes.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    updated_product = product_service.update_product(product_id, data)
    if updated_product:
        return jsonify(updated_product), 200
    return jsonify({'message': 'Product not found'}), 404

@product_routes.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    success = product_service.delete_product(product_id)
    if success:
        return jsonify({'message': 'Product deleted'}), 204
    return jsonify({'message': 'Product not found'}), 404