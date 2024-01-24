# Importing Module Which Are Necessary
import mysql.connector

# Script to connect with database
db_config = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "root",
    database = "bank_application"
)
cursor = db_config.cursor()