# FILE: /products-app-python/products-app-python/tests/test_product.py

import unittest
from app import main
from app.models.product import Product
from app.services.product_service import ProductService

class TestProductService(unittest.TestCase):

    def setUp(self):
        self.app = main.app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.product_service = ProductService()

    def test_create_product(self):
        response = self.client.post('/products', json={
            'name': 'Test Product',
            'description': 'This is a test product.',
            'price': 10.99,
            'quantity': 100
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Test Product', response.get_data(as_text=True))

    def test_get_product(self):
        response = self.client.get('/products/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Product', response.get_data(as_text=True))

    def test_update_product(self):
        response = self.client.put('/products/1', json={
            'name': 'Updated Product',
            'description': 'This is an updated test product.',
            'price': 12.99,
            'quantity': 150
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Updated Product', response.get_data(as_text=True))

    def test_delete_product(self):
        response = self.client.delete('/products/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()