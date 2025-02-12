
# Products App Python

This is a simple Python application that supports CRUD operations for a product entity. The application exposes RESTful endpoints to manage products and stores data persistently in a database.

## Project Structure

```
products-app-python
└── products-app-python
    ├── app
    │   ├── __init__.py
    │   ├── main.py
    │   ├── models
    │   │   └── product.py
    │   ├── routes
    │   │   └── product_routes.py
    │   ├── services
    │   │   └── product_service.py
    │   └── database
    │       ├── __init__.py
    │       └── db.py
    ├── tests
    │   ├── __init__.py
    │   └── test_product.py
    ├── requirements.txt
    └── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd products-app-python
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   python app/main.py
   ```
5. Create a new git repo and push the changes to your github.

```
git init
git add .
git commit -m "{python demo flask app}"
gh repo create {ex: github-copilot-demo} --public --source=. --remote=origin
git push -u origin main
```

## Usage

The application exposes the following RESTful endpoints for managing products:

- `POST /products` - Create a new product
- `GET /products` - Retrieve all products
- `GET /products/<id>` - Retrieve a product by ID
- `PUT /products/<id>` - Update a product by ID
- `DELETE /products/<id>` - Delete a product by ID

## Testing

To run the unit tests, use the following command:

```
pytest tests/
```


## License

This project is licensed under the MIT License.