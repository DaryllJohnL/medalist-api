Medalist API and CSV Processing Service
Overview
This application consists of two main parts:

Laravel API: Handles CSV file uploads.
Python Service: Processes the uploaded CSV files and stores the data into a MongoDB database.
Requirements
For Laravel API:
PHP 7.4 or higher
Composer
MongoDB
For Python Service:
Python 3.x
MongoDB
Installation and Setup
1. Set up the Laravel API (handles CSV upload):
Clone the repository:

git clone https://github.com/DaryllJohnL/medalist-api.git
Navigate to the project directory:

cd medalist-api
Install the required Composer dependencies:


composer install
Copy the environment file:


cp .env.example .env
Update the .env file to set up MongoDB credentials:


DB_CONNECTION=mongodb
DB_HOST=127.0.0.1
DB_PORT=27017
DB_DATABASE=your_database_name
DB_USERNAME=your_username (if required)
DB_PASSWORD=your_password (if required)
Generate the application key:

php artisan key:generate
Run the Laravel development server:

php artisan serve
The server will be running at http://localhost:8000.

2. Set up the Python service (handles processing and saving to MongoDB):
Navigate to the service directory:


cd service
Install the required Python dependencies:

pip install -r requirements.txt
Run the Python service to start listening for uploaded CSV files:

python csv_directory_watcher.py
The Python service will process any CSV files uploaded to the Laravel API.

Using the Application
Step 1: Upload a CSV file using the Laravel API
Method: POST
Endpoint: /api/upload-csv
Request: Upload a CSV file via a form or Postman with the file field.
Example:
curl -X POST -F "file=@path_to_your_file.csv" http://localhost:8000/api/upload-csv
Step 2: The Python Service processes the uploaded CSV
The Python service running in the background will pick up the uploaded CSV file and process it.
The data will be saved into the MongoDB database, as configured in the .env file of the Laravel API.
Step 3: View the stored data
After the CSV is processed and the data is stored in MongoDB, you can query the MongoDB collection to verify the data.
