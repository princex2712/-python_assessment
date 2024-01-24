# Importing Module Which Are Necessary
from .connect_db import cursor,db_config
from Database import database_log
from datetime import datetime

# Function to check customer is valid or not
def is_customer_valid(acc_no):
    valid_user_query = f"SELECT account_no FROM users"
    cursor.execute(valid_user_query)
    list_of_users = cursor.fetchall()
    if acc_no in [i[0] for i in list_of_users]:
        return True
    return False

# Function to take input for data to update
def data_to_update(banker_no):
    choice = int(input("1)Update Name\n2)Update Phone\nEnter Your Choice: "))
    acc_no = input("Enter Account Number: ")
    while not is_customer_valid(acc_no):
        acc_no = input("Invalid Detail! Enter Valid Account Number: ")
    update_data(choice,acc_no,banker_no)

# Function to update user name
def update_name(acc_no,banker_no):
    user_name = input("Enter Updated Name: ")
    update_query = f"UPDATE users SET name='{user_name}' WHERE account_no='{acc_no}'"
    cursor.execute(update_query)
    log = {f'Account_no: {acc_no}, Operation: Update User Name, Date_Time: {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}, Banker_no: {banker_no}'}
    database_log.save_logs(log)
    db_config.commit()

# Function to update user phone
def update_phone(acc_no,banker_no):
    user_phone = input("Enter Updated Phone Number: ")
    update_query = f"UPDATE users SET phone='{user_phone}' WHERE account_no='{acc_no}'"
    log = {f'Account_no: {acc_no}, Operation: Update User Phone, Date_Time: {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}, Banker_no: {banker_no}'}
    database_log.save_logs(log)
    cursor.execute(update_query)
    db_config.commit()

# Funtion to widthdraw amount
def widthdraw(acc_no):
    balance_query = f"SELECT balance FROM users WHERE account_no={acc_no}"
    cursor.execute(balance_query)
    current_balance = cursor.fetchone()[0]
    amount = int(input("Enter Amount to Widthdraw: "))
    if amount > current_balance:
        print("Widthdraw amount is greater than Amount in Account Balance")
    else:
        current_balance -= amount
    update_balance_query = f"UPDATE users SET balance ={current_balance} WHERE account_no='{acc_no}'"
    cursor.execute(update_balance_query)
    log = {f'Account_no: {acc_no}, Operation: Widthdraw Amount, Amount: {amount}, Date_Time: {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}'}
    database_log.save_logs(log)
    db_config.commit()

# Fucntion to Deposite Amount
def deposite(acc_no):
    balance_query = f"SELECT balance FROM users WHERE account_no={acc_no}"
    cursor.execute(balance_query)
    current_balance = cursor.fetchone()[0]
    amount = int(input("Enter Amount to Deposite: "))
    current_balance += amount
    update_balance_query = f"UPDATE users SET balance ={current_balance} WHERE account_no='{acc_no}'"
    log = {f'Account_no: {acc_no}, Operation: Deposite Amount, Amount: {amount}, Date_Time: {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}'}
    database_log.save_logs(log)
    cursor.execute(update_balance_query)
    db_config.commit()
    
# Calling funtion based on users choice
def update_data(choice,acc_no,banker_no):
    match choice:     
        case 1:
            update_name(acc_no,banker_no)
        case 2:
            update_phone(acc_no,banker_no)
        case _:
            choice = input('Invalid Choice! Enter Valid Choice: ')
            update_data(choice)

