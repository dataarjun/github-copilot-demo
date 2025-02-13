from app.models.product import Product

class ProductService:
    def __init__(self, db):
        self.db = db

    def create_product(self, data):
        new_product = Product(
            name=data['name'],
            description=data.get('description'),
            price=data['price'],
            quantity=data['quantity']
        )
        self.db.session.add(new_product)
        self.db.session.commit()
        return new_product

    def get_all_products(self):
        return Product.query.all()

    def get_product_by_id(self, product_id):
        return Product.query.get(product_id)

    def update_product(self, product_id, data):
        product = Product.query.get(product_id)
        if product:
            product.name = data['name']
            product.description = data.get('description')
            product.price = data['price']
            product.quantity = data['quantity']
            self.db.session.commit()
        return product

    def delete_product(self, product_id):
        product = Product.query.get(product_id)
        if product:
            self.db.session.delete(product)
            self.db.session.commit()
        return product