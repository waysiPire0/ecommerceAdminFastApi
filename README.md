## E-Commerce Admin Dashboard API

### Requirements
1. Python 3.10 or higher
2. MYSQL Database

### Installation
1. Make sure you have Python 3.10 or higher installed.
2. Set up a MYSQL database.
3. Clone the repository:
   ```
   git clone https://github.com/your-repository/ecommerceAdminFastApi.git
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