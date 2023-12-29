from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

from dotenv import load_dotenv, find_dotenv
import os

# Load environment variables from .env file
load_dotenv(find_dotenv())

app = Flask(__name__)

# Database Configuration
DB_HOST = os.getenv("DB_HOST")  
DB_USER = os.getenv("DB_USER")  
DB_PASS = os.getenv("DB_PASS")  
DB_NAME = os.getenv("DB_NAME")  

# Get the list of services and their corresponding image
@app.route('/api/service', methods=['GET'])
def list_services():
    """
    Get all services and their corresponding image.
    """
    # List all services and their corresponding image on the DB
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(host=DB_HOST,
                                             database=DB_NAME,
                                             user=DB_USER,
                                             password=DB_PASS)
        if connection.is_connected():
            db_cursor = connection.cursor(dictionary=True)
            db_cursor.execute("SELECT id, name, image FROM services")
            services = db_cursor.fetchall()
            return jsonify(services)
        
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if connection.is_connected():
            db_cursor.close()
            connection.close()


@app.route('/api/service/<int:service_id>', methods=['GET'])
def get_service_and_sub_services(service_id):
    """
    Get the service and its sub-services [all tables].
    """
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(host=DB_HOST,
                                             database=DB_NAME,
                                             user=DB_USER,
                                             password=DB_PASS)
        if connection.is_connected():
            db_cursor = connection.cursor(dictionary=True)
            
            # Query to get the service
            db_cursor.execute("SELECT id, name FROM services WHERE id = %s", (service_id,))
            service = db_cursor.fetchone()

            # If the service is found, get its sub-services
            if service:
                db_cursor.execute("SELECT * FROM sub_services WHERE service_id = %s", (service['id'],))
                sub_services = db_cursor.fetchall()
                service['sub_services'] = sub_services
            else:
                return jsonify({"error": "Service not found"}), 404
            
            return jsonify(service)
        
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if connection.is_connected():
            db_cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)
