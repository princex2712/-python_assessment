from BankApplication import *

def user():
    choice = input("Greetings! Which is Your Role\n1)Banker\n2)Customer\nEnter Your Choice: ")
    if choice == '1':
        banker.Banker()
    elif choice == '2':
        customer.Customer()
    else:
        print("Invalid Choice!")
        yn = input("Want To Reset Operation(y/n): ")
        if yn.lower() == 'y':
            user()
        else:
            print("Thanks For Using Bank Application! Peace Off.")
user()





