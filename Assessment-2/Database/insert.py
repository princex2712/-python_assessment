# Importing Module Which Are Necessary
from datetime import datetime
from .connect_db import cursor,db_config
from Database import database_log
from dotenv import load_dotenv
import os

# Function to check account number is unique or not
def is_acc_no_unq(account_no):
    cursor.execute("SELECT account_no FROM users")
    sql = cursor.fetchall()
    if str(account_no) in [i[0] for i in sql]:
        return False
    return True

# Function to check banker number is unique or not
def is_banker_no_unq(account_no):
    cursor.execute("SELECT banker_no FROM bankers")
    sql = cursor.fetchall()
    if account_no in [i[0] for i in sql]:
        return False
    return True

# Function to insert query to insert user
def  insert_into_table_user():
    user_name = input('Enter Username: ')
    user_account_no = input('Enter Account Number: ')
    while not is_acc_no_unq(user_account_no):
        print("Account Number Already Taken! Please Enter Another Account Number: ")
        user_account_no = input('Enter Account Number: ')
    user_phone = input('Enter User Phone Number: ')
    user_opening_balance = float(input('Enter User Opening Balance: '))
    insert_query = f"INSERT INTO users (name,account_no,phone,balance) VALUES('{user_name}','{user_account_no}','{user_phone}','{user_opening_balance}')"
    cursor.execute(insert_query)
    log = {f'Account_no: {user_account_no}, Operation: Registered User, Date_Time: {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}'}
    database_log.save_logs(log)
    db_config.commit()
    print("Created Successfully!")
    
# Function to insert query to insert banker
def  insert_into_table_banker():
    dotenv_path = os.path.join(os.path.dirname(__file__),'..','.env')
    load_dotenv(dotenv_path)
    banker_unq_key = os.environ.get('BANKER_KEY')
    banker_unq_key_input = input("Enter Banker Key To Register As A new Banker: ")
    if banker_unq_key_input == banker_unq_key:
        banker_no = int(input('Enter Banker Number: '))
        banker_password = input('Enter Banker Password: ')

        while not is_banker_no_unq(banker_no):
            print("Number Already Taken! Please Enter Another Banker Number: ")
            banker_no = int(input('Enter Account Number: '))
        
        insert_query = f"INSERT INTO bankers(banker_no,banker_password) VALUES({banker_no},'{banker_password}')"
        cursor.execute(insert_query)
        log = {f'Banker_no: {banker_no}, Operation: Registered Banker, Date_Time: {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}'}
        database_log.save_logs(log)
        db_config.commit()
        print("Created Successfully!")
    else:
        print("Wrong Banker Key! You can not Register As Banker")