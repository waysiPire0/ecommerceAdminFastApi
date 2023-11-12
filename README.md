## E-Commerce Admin Dashboard API

### Requirements
1. Python 3.10 or higher
2. MYSQL Database

### Installation
1. Make sure you have Python 3.10 or higher installed.
2. Set up a MYSQL database.
3. Clone the repository:
   ```
   git clone https://github.com/waysiPire0/ecommerceAdminFastApi.git
   ```
4. Navigate to the project directory:
   ```
   cd ecommerceAdminFastApi
   ```
5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
6. Create a .env file in the project root with the following contents:
   ```
    API_VERSION=v1
    APP_NAME=E-Commerce Admin Dashboard API
    DB_NAME=your_db_name
    DB_USER=your_db_username
    DB_PASSWORD=your_db_password
    DB_HOST=localhost
    DB_PORT=3306
   ```
7. Initialize and Populate the Database:
   ```
   python zpopulate.py
   ```
8. Run the Application:
   ```
   uvicorn main:app --reload
   ```
7. Open your browser and navigate to `http://localhost:8000/docs`.
8. Explore the features of the application.



### API Endpoints

#### Admin
* /admin/login: Admin login endpoint.
* /admin/signup: Admin signup endpoint.

#### Auth
* /token: Endpoint for token generation and authentication.

#### Product
* GET /product/products: Get all products.
* POST /product/: Create/Register a new product.
* GET /product/{product_id}: Get product by id
* PUT /product/{product_id}: Update product
* DELETE /product/{product_id}: Delete a product

#### Category
* GET /category/categories: Get all categories.
* POST /category/: Create a new category.
* GET /category/{category_id}: Get category by ID.
* PUT /category/{category_id}: Update category.
* DELETE /category/{category_id}: Delete a category.

#### Inventory
* GET /inventory/inventories: Get all inventories.
* GET /inventory/low-stock: Get low stock alerts.
* POST /inventory/: Create a new inventory.
* GET /inventory/{inventory_id}: Get inventory by ID.
* PUT /inventory/{inventory_id}: Update inventory.
* DELETE /inventory/{inventory_id}: Delete an inventory.

#### Sales
* GET /sale/sales: Get sales with optional filters for start date, end date, product ID, and category ID.
* GET /sale/revenue: Get revenue analysis based on a specified timeframe (daily, weekly, monthly, or annual).
* POST /sale/: Create a new sale.
* GET /sale/{sale_id}: Get sale by ID.
* PUT /sale/{sale_id}: Update sale.
* DELETE /sale/{sale_id}: Delete a sale.

#### Customers
* GET /customer/customers: Get all customers.
* POST /customer/: Create a new customer.
* GET /customer/{customer_id}: Get customer by ID.
* PUT /customer/{customer_id}: Update customer.
* DELETE /customer/{customer_id}: Delete a customer.