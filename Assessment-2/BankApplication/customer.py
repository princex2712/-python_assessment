from Database.connect_db import cursor,db_config
from Database import *


class Customer:

    def __init__(self):
        choice = input("1)New User\n2)Already Registered User\nEnter Your Choice: ")
        if choice == '1':
            self.new_user()
        elif choice == '2':
            self.user_acc_no = input("Enter Customer Account Number: ")
            self.user_phone = input("Enter Customer Phone: ")
            self.is_customer_valid()
        else:
            print("Invalid Choice! Enter Valid Choice")
            self.__init__()

    def new_user(self):
        
        insert.insert_into_table_user()

    def is_customer_valid(self):
        valid_user_query = f"SELECT account_no,phone FROM users"
        cursor.execute(valid_user_query)
        list_of_users = cursor.fetchall()
        if (self.user_acc_no,self.user_phone) in list_of_users:
            self.welcome_user()
        else:
            print("Invalid Details!")
        db_config.commit()

    def widthdraw(self):
        update.widthdraw(self.user_acc_no)
        yn = input("Want To Perform Another Operation(y/n): ")
        if yn.lower() == 'y':
            self.welcome_user()
        else:
            print("Thanks For Using Bank Application! Peace Off.")

    def deposite(self):
        update.deposite(self.user_acc_no)
        yn = input("Want To Perform Another Operation(y/n): ")
        if yn.lower() == 'y':
            self.welcome_user()
        else:
            print("Thanks For Using Bank Application! Peace Off.")
    
    def view_balance(self):
        balance_query = f"SELECT balance FROM users WHERE account_no={self.user_acc_no}"
        cursor.execute(balance_query)
        balance = cursor.fetchone()[0]
        print("Current Balance: "+ str(balance))
        yn = input("Want To Perform Another Operation(y/n): ")
        if yn.lower() == 'y':
            self.welcome_user()
        else:
            print("Thanks For Using Bank Application! Peace Off.")
        
    def welcome_user(self):
        user_choice = int(input(f"WELCOME TO CUSTOMER'S SIDE APPLICATION\n1)Widthdraw Amount\n2)Deposite Amount\n3)View Balance\nEnter Your Choice: "))

        match user_choice:
            case 1:
                self.widthdraw()
            case 2:
                self.deposite()
            case 3:
                self.view_balance()
            case _:
                print("Invalid Choice!")
        