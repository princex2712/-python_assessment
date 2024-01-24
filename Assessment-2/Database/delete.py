# Importing Module Which Are Necessary
from .connect_db import cursor,db_config
from datetime import datetime
from Database import update,database_log

# Funtion to Delete User
def delete_user(banker_no):
    acc_no = input("Enter Account Number to Delete: ")
    while not update.is_customer_valid(acc_no):
        acc_no = input("Invalid Detail! Enter Valid Account Number: ")
    delete_query = f"DELETE FROM users WHERE account_no='{acc_no}'"
    cursor.execute(delete_query)
    log = {f'Account_no: {acc_no}, Operation: Delete User, Date_Time: {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}, Banker_no: {banker_no}'}
    database_log.save_logs(log)
    db_config.commit()