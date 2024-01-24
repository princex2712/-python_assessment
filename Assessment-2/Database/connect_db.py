import mysql.connector


db_config = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "root",
    database = "bank_application"
)
cursor = db_config.cursor()