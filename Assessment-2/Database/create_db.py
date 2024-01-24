import mysql.connector


def create_database():
    db_name = input('Enter Your Database Name: ')
    db_config = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
        )
    cursor = db_config.cursor()
    cursor.execute(f"CREATE DATABASE {db_name}")