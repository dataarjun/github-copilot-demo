from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService
from app.database.db import db

product_routes = Blueprint('product_routes', __name__)
product_service = ProductService(db)

@product_routes.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = product_service.create_product(data)
    return jsonify(new_product.to_dict()), 201

@product_routes.route('/products', methods=['GET'])
def get_all_products():
    products = product_service.get_all_products()
    return jsonify([product.to_dict() for product in products]), 200

@product_routes.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = product_service.get_product_by_id(product_id)
    if product:
        return jsonify(product.to_dict()), 200
    return jsonify({'message': 'Product not found'}), 404

@product_routes.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    updated_product = product_service.update_product(product_id, data)
    if updated_product:
        return jsonify(updated_product.to_dict()), 200
    return jsonify({'message': 'Product not found'}), 404

@product_routes.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    deleted_product = product_service.delete_product(product_id)
    if deleted_product:
        return jsonify({'message': 'Product deleted'}), 200
    return jsonify({'message': 'Product not found'}), 404