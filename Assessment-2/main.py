# Importing Module Which Are Necessary
from BankApplication import *

# Creating user funtion to welcome user and choose there role
def user():
    choice = input("Greetings! Which is Your Role\n1)Banker\n2)Customer\nEnter Your Choice: ")
    if choice == '1':
        banker.Banker() # Creating instance of Class for Banker
    elif choice == '2':
        customer.Customer() # Creating instance of Class for Customer
    else:
        print("Invalid Choice!") # If Invalid Choice inputed by user and asking that want to repeat operation/
        yn = input("Want To Reset Operation(y/n): ")
        if yn.lower() == 'y':
            user()
        else:
            print("Thanks For Using Bank Application! Peace Off.")
user() # Calling Funtion user()





