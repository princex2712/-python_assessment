from Database.connect_db import db_config,cursor
from Database import *

class Banker:

    def __init__(self):
        choice = input("1)New Banker\n2)Already Registered Banker\nEnter Your Choice: ")
        if choice == '1':
            insert.insert_into_table_banker()
        elif choice == '2':
            self.banker_no = int(input("Enter Banker No: "))
            self.banker_pass = input("Enter Banker Password: ")
            self.is_banker_valid()
        else:
            print("Invalid Detail")
    
    def is_banker_valid(self):
        valid_banker_query = f"SELECT banker_no,banker_password FROM bankers"
        cursor.execute(valid_banker_query)
        list_of_bankers = cursor.fetchall()

        if (self.banker_no,self.banker_pass) in list_of_bankers:
            self.welcome_banker()
        else:
            print("Invalid Details!")
        db_config.commit()
    
    def view_all_users(self):
        view_customers_query = f"SELECT * FROM users"
        cursor.execute(view_customers_query)
        customers = cursor.fetchall()
        for customer in customers:
            print("ID: {}, Name: {}, Account-No: {}, Phone: {}, Balance: {}\n".format(customer[0],customer[1],customer[2],customer[3],customer[4]))
        yn = input("Want To Perform Another Operation(y/n): ")
        if yn.lower() == 'y':
            self.welcome_banker()
        else:
            print("Thanks For Using Bank Application! Peace Off.")
    
    def update_user(self):
        update.data_to_update(self.banker_no)
        yn = input("Want To Perform Another Operation(y/n): ")
        if yn.lower() == 'y':
            self.welcome_banker()
        else:
            print("Thanks For Using Bank Application! Peace Off.")

    def delete_user(self):
        delete.delete_user(self.banker_no)
        yn = input("Want To Perform Another Operation(y/n): ")
        if yn.lower() == 'y':
            self.welcome_banker()
        else:
            print("Thanks For Using Bank Application! Peace Off.")
        

    def welcome_banker(self):
        banker_choice = int(input(f"WELCOME TO BANKER'S SIDE APPLICATION\n1)Update Customer\n2)View Customers\n3)Delete Customers\nEnter Your Choice: "))

        match banker_choice:
            case 1:
                self.update_user()
            case 2:
                self.view_all_users()
            case 3:
                self.delete_user()
            case _:
                print("Invalid Choice!")
