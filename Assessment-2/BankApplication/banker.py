# Importing Module Which Are Necessary
from Database.connect_db import db_config,cursor
from Database import *

# Creating class and then defining function to follow standard format
class Banker:

    def __init__(self): # Constructor of class which used to take input from user
        choice = input("1)New Banker\n2)Already Registered Banker\nEnter Your Choice: ") # taking input 
        if choice == '1':
            insert.insert_into_table_banker() # based on choice calling function 
        elif choice == '2':
            self.banker_no = int(input("Enter Banker No: ")) # Taking input from user to login 
            self.banker_pass = input("Enter Banker Password: ")
            self.is_banker_valid() # based on choice calling function 
        else:
            print("Invalid Detail") # if user enters invalid detail 

    # Funtion to check banker is valid or not
    def is_banker_valid(self): 
        valid_banker_query = f"SELECT banker_no,banker_password FROM bankers"
        cursor.execute(valid_banker_query)
        list_of_bankers = cursor.fetchall()
        if (self.banker_no,self.banker_pass) in list_of_bankers:
            self.welcome_banker() # if banker valid then let them  access there operation
        else:
            print("Invalid Details!")
        db_config.commit()
    
    # Funtion to view all users
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
    
    # Function to update user
    def update_user(self):
        update.data_to_update(self.banker_no)
        yn = input("Want To Perform Another Operation(y/n): ")
        if yn.lower() == 'y':
            self.welcome_banker()
        else:
            print("Thanks For Using Bank Application! Peace Off.")

    # Function to delete user
    def delete_user(self):
        delete.delete_user(self.banker_no)
        yn = input("Want To Perform Another Operation(y/n): ")
        if yn.lower() == 'y':
            self.welcome_banker()
        else:
            print("Thanks For Using Bank Application! Peace Off.")
        
    # Function to welcome user
    def welcome_banker(self):
        banker_choice = int(input(f"WELCOME TO BANKER'S SIDE APPLICATION\n1)Update Customer\n2)View Customers\n3)Delete Customers\nEnter Your Choice: "))

        match banker_choice: # calling function based on choice
            case 1:
                self.update_user()
            case 2:
                self.view_all_users()
            case 3:
                self.delete_user()
            case _:
                print("Invalid Choice!")
